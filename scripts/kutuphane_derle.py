#!/usr/bin/env python3
"""
Vera Kütüphane derleyicisi.

Botların ham çıktısını (Hikayeler_Arsivi, md hikâye klasörleri, veriler/*.json cuma mesajları)
okur; bozuk/menü artığı/çok kısa kayıtları atar, tekrarları birleştirir ve uygulamanın okuduğu
TEK temiz klasörü üretir:

    vera_kutuphane/manifest.json
    vera_kutuphane/kitaplar/<id>.json

Çakışma kuralları:
  * Botlar bu klasöre ASLA yazmaz; sadece bu betik yazar.
  * Bir kitabın sürümü yalnızca içeriği gerçekten değiştiyse artar (içerik özeti/hash ile).
  * Önce kitaplar, EN SON manifest yazılır (uygulama yarım güncelleme görmez).

Kullanım:  python scripts/kutuphane_derle.py --kaynak1 _kaynak1 --kaynak2 _kaynak2
  (--kaynak1: KJSASAUDHAu-j, --kaynak2: jsnjksQSHUnhr-ya checkout klasörü; yoksa o kaynaklar atlanır)
"""
import argparse
import collections
import glob
import hashlib
import json
import os
import re
import tempfile

CIKTI = "vera_kutuphane"
MIN_HIKAYE = 200          # karakter
CUMA_PER_KATEGORI = 150   # kütüphane kitabı için kategori başına mesaj
COP_KELIMELER = ["KÜNYE", "HAKKIMIZDA", "ANASAYFA", "İLETİŞİM", "MENÜ", "Çerez", "cookie",
                 "İçerik Bulunamadı", "Tüm hakları saklıdır", "Abone ol", "Giriş yap"]

CUMA_ADLARI = {
    "cuma": "Cuma Mesajları", "cuma_aksami": "Cuma Akşamı", "sabah_duasi": "Sabah Duaları",
    "ramazan_ayi": "Ramazan Ayı", "ramazan_bayrami": "Ramazan Bayramı", "kurban_bayrami": "Kurban Bayramı",
    "kadir_gecesi": "Kadir Gecesi", "berat_kandili": "Berat Kandili", "mirac_kandili": "Miraç Kandili",
    "regaip_kandili": "Regaip Kandili", "mevlid_kandili": "Mevlid Kandili", "arefe_gunu": "Arefe Günü",
    "asure_gunu": "Aşure Günü", "hicri_yilbasi": "Hicri Yılbaşı",
}


def temizle(metin: str) -> str:
    metin = (metin or "").replace("\r", "")
    metin = re.sub(r"[ \t]+", " ", metin)
    metin = re.sub(r"\n{3,}", "\n\n", metin)
    return metin.strip()


BOZUK_KARAKTER = re.compile(r"Ã.|Ä.|Å.|â€|�")


def cumleler(metin: str):
    # Virgülle birleştirilmiş kalıpları da yakalamak için cümle parçası (clause) düzeyinde böl
    parcalar = [re.sub(r"\W+", " ", c.lower()).strip() for c in re.split(r"(?<=[.!?,;])\s+", metin)]
    # Son parça genelde kapanış selamıdır ("Hayırlı Arefeler."); onu sayma
    return [p for p in parcalar[:-1] if len(p) > 12] if len(parcalar) > 1 else [p for p in parcalar if len(p) > 12]


def cop_mu(baslik: str, icerik: str) -> bool:
    if len(icerik) < MIN_HIKAYE:
        return True
    # Kodlaması bozuk metin (ör. ansiklopedi dizin artıkları)
    if BOZUK_KARAKTER.search(baslik + icerik):
        return True
    # "Sayfa Adı | site adı" biçimli başlıklar: kazınmış site sayfası, hikâye değil
    if "|" in baslik or re.search(r"\.(com|net|org)\b", baslik, re.I):
        return True
    birlesik = baslik + " " + icerik[:1500]
    if sum(1 for k in COP_KELIMELER if k.lower() in birlesik.lower()) >= 1:
        return True
    satirlar = [s for s in icerik.split("\n") if s.strip()]
    # Menü/başlık listesi: çok sayıda kısa satır
    if len(satirlar) > 8 and sum(1 for s in satirlar if len(s) < 40) / len(satirlar) > 0.6:
        return True
    return False


def anahtar(baslik: str, icerik: str) -> str:
    norm = re.sub(r"\W+", "", (baslik + icerik[:150]).lower())
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()


def guzel_ad(s: str) -> str:
    return s.replace("_", " ").replace("-", " ").strip()


def hikayeleri_topla(kaynak1, kaynak2):
    ciltler = {}   # cilt adı -> [sayfa]
    gorulen = set()

    def ekle(cilt, baslik, icerik):
        baslik, icerik = temizle(baslik), temizle(icerik)
        if not baslik or cop_mu(baslik, icerik):
            return
        k = anahtar(baslik, icerik)
        if k in gorulen:
            return
        gorulen.add(k)
        ciltler.setdefault(cilt, []).append({"baslik": baslik[:140], "icerik": icerik})

    for yol in sorted(glob.glob(os.path.join(kaynak1, "Hikayeler_Arsivi", "*.json"))):
        # Otomatik kazınan dosya hikâye değil, site makalesi içeriyor -> kütüphaneye alınmaz
        if os.path.basename(yol).lower().startswith("otomatik"):
            continue
        try:
            veri = json.load(open(yol, encoding="utf-8"))
        except Exception:
            continue
        for h in veri if isinstance(veri, list) else []:
            if isinstance(h, dict):
                cilt = guzel_ad(h.get("kategori") or os.path.splitext(os.path.basename(yol))[0])
                ekle(cilt, h.get("baslik", ""), h.get("icerik", ""))

    if kaynak2 and os.path.isdir(kaynak2):
        for klasor in ["Sahabe_ve_Peygamberler", "Evliyalar_ve_Alimler", "Ahlak_ve_Erdem", "Diger_Ibretlikler", "Diğer_İbretlikler"]:
            cilt = guzel_ad(klasor).replace("Diger Ibretlikler", "Diğer İbretlikler")
            for yol in sorted(glob.glob(os.path.join(kaynak2, klasor, "*.md"))):
                metin = open(yol, encoding="utf-8", errors="ignore").read()
                m = re.match(r"\s*#\s*(.+)\n", metin)
                baslik = m.group(1) if m else guzel_ad(os.path.splitext(os.path.basename(yol))[0])
                govde = metin[m.end():] if m else metin
                govde = re.sub(r"[#*_`>]+", "", govde)
                ekle(cilt, baslik, govde)

    return [{"ad": ad, "sayfalar": s} for ad, s in sorted(ciltler.items()) if s]


def cuma_topla(kaynak2):
    if not kaynak2:
        return []
    ciltler = []
    for yol in sorted(glob.glob(os.path.join(kaynak2, "veriler", "*.json"))):
        kod = os.path.splitext(os.path.basename(yol))[0]
        try:
            veri = json.load(open(yol, encoding="utf-8"))
        except Exception:
            continue
        liste = [temizle(str(m)) for m in (veri if isinstance(veri, list) else [])[:30000]]
        # Bot, hazır cümleleri karıştırarak mesaj üretiyor. Birçok mesajda aynen geçen cümle = şablon.
        # Şablon cümleden 2+ içeren mesaj "yapay" sayılır ve alınmaz.
        sayac = collections.Counter(c for m in liste for c in set(cumleler(m)))
        sablon = {c for c, n in sayac.items() if n >= 4}
        gorulen, sayfalar, gorulen_cumle = set(), [], set()
        for metin in liste:
            k = re.sub(r"\W+", "", metin.lower())
            cs = cumleler(metin)
            if len(metin) < 60 or k in gorulen or cop_mu("", metin + " " * MIN_HIKAYE):
                continue
            if sum(1 for c in cs if c in sablon) >= 2:
                continue
            # Aynı cümle başka seçilmiş mesajda da varsa (tekrar hissi) alma
            if any(c in gorulen_cumle for c in cs):
                continue
            gorulen_cumle.update(cs)
            gorulen.add(k)
            sayfalar.append({"baslik": f"{CUMA_ADLARI.get(kod, guzel_ad(kod))} #{len(sayfalar) + 1}", "icerik": metin})
            if len(sayfalar) >= CUMA_PER_KATEGORI:
                break
        if sayfalar:
            ciltler.append({"ad": CUMA_ADLARI.get(kod, guzel_ad(kod)), "sayfalar": sayfalar})
    return ciltler


def atomik_yaz(yol, veri):
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(yol), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, yol)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kaynak1", default=".", help="KJSASAUDHAu-j checkout klasörü")
    ap.add_argument("--kaynak2", default="", help="jsnjksQSHUnhr-ya checkout klasörü")
    args = ap.parse_args()

    kitaplar = [
        # id'si uygulamadaki kitapla aynı olanlar onun yerine geçer (tekrar görünmez)
        {"id": "cuma_mesajlari_book", "baslik": "Cuma & Kandil Tebrikleri", "yazar": "Vera Tebrik Rehberi",
         "renk": ["#10B981", "#047857"], "ciltler": cuma_topla(args.kaynak2)},
        {"id": "arsiv_hikayeler_book", "baslik": "Seçme İbretlik Hikâyeler", "yazar": "Vera Arşiv",
         "renk": ["#7C3AED", "#4C1D95"], "ciltler": hikayeleri_topla(args.kaynak1, args.kaynak2)},
    ]

    # Elle hazırlanmış (uygulamadan taşınan) kitaplar: kitaplar_kaynak/<id>.json
    # Dosya adındaki sıra numarası (01_, 02_ …) Kütüphane'deki sırayı belirler; elle kitaplar önce gelir.
    uretilen = {k["id"] for k in kitaplar}
    elle = []
    for yol in sorted(glob.glob("kitaplar_kaynak/*.json")):
        try:
            k = json.load(open(yol, encoding="utf-8"))
        except Exception as e:
            print(f"ATLANDI {yol}: {e}")
            continue
        if not k.get("id"):
            continue
        ciltler = [c for c in k.get("ciltler", []) if c.get("ad") and c.get("sayfalar")]
        hedef = next((g for g in kitaplar if g["id"] == k["id"]), None)
        if hedef is not None:
            # Aynı id'li bot kitabına ek: elle yazılan sayfalar aynı adlı cildin BAŞINA eklenir
            for ec in ciltler:
                cilt = next((c for c in hedef["ciltler"] if c["ad"] == ec["ad"]), None)
                if cilt is None:
                    cilt = {"ad": ec["ad"], "sayfalar": []}
                    hedef["ciltler"].append(cilt)
                mevcut = {re.sub(r"\W+", "", s["icerik"].lower()) for s in cilt["sayfalar"]}
                yeni = [s for s in ec["sayfalar"] if re.sub(r"\W+", "", s["icerik"].lower()) not in mevcut]
                cilt["sayfalar"] = yeni + cilt["sayfalar"]
                for i, s in enumerate(cilt["sayfalar"], 1):   # başlıkları yeniden numarala
                    s["baslik"] = f"{ec['ad']} #{i}"
            continue
        if k["id"] in uretilen:
            continue
        elle.append({"id": k["id"], "baslik": k.get("baslik", ""), "yazar": k.get("yazar", "Vera Arşiv"),
                     "renk": k.get("renk", ["#0F766E", "#134E4A"]), "ciltler": ciltler})
        uretilen.add(k["id"])
    kitaplar = elle + kitaplar

    manifest_yol = os.path.join(CIKTI, "manifest.json")
    eski = {}
    if os.path.exists(manifest_yol):
        try:
            eski = {k["id"]: k for k in json.load(open(manifest_yol, encoding="utf-8")).get("kitaplar", [])}
        except Exception:
            eski = {}

    girdiler, degisti = [], False
    for k in kitaplar:
        if not k["ciltler"]:
            if k["id"] in eski:            # kaynak geçici bozuksa eski kitabı koru
                girdiler.append(eski[k["id"]])
            continue
        icerik = {"id": k["id"], "ciltler": k["ciltler"]}
        ozet = hashlib.sha1(json.dumps(icerik, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]
        onceki = eski.get(k["id"], {})
        surum = onceki.get("surum", 0) if onceki.get("ozet") == ozet else onceki.get("surum", 0) + 1
        dosya = f"kitaplar/{k['id']}.json"
        if surum != onceki.get("surum") or not os.path.exists(os.path.join(CIKTI, dosya)):
            atomik_yaz(os.path.join(CIKTI, dosya), icerik)
            degisti = True
        girdi = {"id": k["id"], "baslik": k["baslik"], "yazar": k["yazar"], "renk": k["renk"],
                 "dosya": dosya, "surum": surum, "ozet": ozet,
                 "sayfa_sayisi": sum(len(c["sayfalar"]) for c in k["ciltler"])}
        # Kapak görseli: vera_kutuphane/kapaklar/<id>.webp varsa manifeste yazılır
        kapak = f"kapaklar/{k['id']}.webp"
        if os.path.exists(os.path.join(CIKTI, kapak)):
            girdi["kapak"] = kapak
        girdiler.append(girdi)

    # Genel sürüm, manifest içeriğinin özeti: kitap, sıra veya kapak değişince uygulama manifesti yeniler
    genel = int(hashlib.sha1(json.dumps(girdiler, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:7], 16)
    onceki_genel = None
    if os.path.exists(manifest_yol):
        try:
            onceki_genel = json.load(open(manifest_yol, encoding="utf-8")).get("surum")
        except Exception:
            pass
    if degisti or onceki_genel != genel:
        atomik_yaz(manifest_yol, {"surum": genel, "kitaplar": girdiler})   # EN SON
    for g in girdiler:
        print(f"{g['id']}: sürüm {g['surum']}, {g.get('sayfa_sayisi', '?')} sayfa")


if __name__ == "__main__":
    main()
