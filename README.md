# vera-icerik

Vera Android uygulamasının indirilebilir içerik deposu. Uygulama bu depodan yalnızca **okur**;
içerik APK'ya gömülmediği için uygulama küçük kalır ve içerik güncellemesi için yeni sürüm gerekmez.

## Yapı

| Klasör | Ne içerir | Kim yazar |
|---|---|---|
| `vera_kutuphane/manifest.json` | Kütüphanedeki uzak kitaplar ve sürümleri | Sadece derleyici |
| `vera_kutuphane/kitaplar/*.json` | Kitapların ciltleri ve sayfaları | Sadece derleyici |
| `ezan_sesleri/katalog.json` | İndirilebilir ezan sesleri listesi | Elle |
| `scripts/kutuphane_derle.py` | Ham bot verisini süzen derleyici | — |
| `.github/workflows/kutuphane.yml` | Derleyiciyi her gün çalıştıran iş akışı | — |

## Çakışma kuralları

- Ham veri üreten botlar bu depoya **yazmaz**; kendi depolarında çalışır
  (`KJSASAUDHAu-j`, `jsnjksQSHUnhr-ya`). Bu depo onları sadece kaynak olarak okur.
- `vera_kutuphane/` klasörünü yalnızca derleyici üretir. Aynı anda tek derleme çalışır.
- Bir kitabın `surum` değeri yalnızca içeriği gerçekten değişince artar.
- Önce kitaplar, **en son** manifest yazılır. Uygulama yarım güncelleme görmez;
  bozuk veya boş kitap gelirse önbellekteki eski sürümü kullanmaya devam eder.
- Uzak kitabın `id`'si uygulamadaki gömülü bir kitapla aynıysa onun yerine geçer (çift görünmez).

## Kitap biçimi

```json
{"id": "kitap_id", "ciltler": [{"ad": "Cilt adı", "sayfalar": [{"baslik": "Başlık", "icerik": "Metin…"}]}]}
```

Derleyici; 200 karakterden kısa, site menüsü/çerez metni içeren, `Sayfa | Site` biçimli başlığı olan
ve tekrar eden kayıtları atar. Otomatik kazınan `Otomatik_Toplananlar` dosyası alınmaz.

## Ezan sesi ekleme

1. Ses dosyasını (MP3, en fazla 15 MB, **kullanım hakkınız olan** bir kayıt) `ezan_sesleri/` klasörüne yükleyin.
2. `ezan_sesleri/katalog.json` dosyasına ekleyin:

```json
[
  {
    "id": "hicaz_1",
    "ad": "Hicaz Makamı Ezan",
    "aciklama": "Müezzin adı",
    "url": "https://raw.githubusercontent.com/yavuzdilmez00-ux/vera-icerik/main/ezan_sesleri/hicaz_1.mp3",
    "boyut_kb": 1800
  }
]
```

`id` küçük harf, rakam ve `_` içermeli; `cihaz` kullanılamaz (telefondan seçilen sese ayrılmıştır).

## Elle derleme

```bash
python scripts/kutuphane_derle.py --kaynak1 ../KJSASAUDHAu-j --kaynak2 ../jsnjksQSHUnhr-ya
```
