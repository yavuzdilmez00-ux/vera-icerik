import json, re
OUT = r"C:\Users\dared\AppData\Local\Temp\claude\016efd8e3f2a5ef4\6b8db417-ae01-422c-aca1-b9fd8cd931a6\scratchpad\vera-icerik\kitaplar_kaynak\20_siyer_book.json"

EXTRA = {
"Fil Yılı ve Doğum": "O sırada Kureyş, Kâbe'nin bakımını ve hacılara su ve yemek ikramını üstlenmişti. Hâşimoğulları bu hizmetlerde öne çıkan koldu.",
"Annesinin ve Dedesinin Vefatı": "Ümmü Eymen, sonraki yıllarda da Peygamberimizin yanından ayrılmadı. Peygamberimiz ona 'annemden sonra annem' derdi.",
"Şam Ticareti ve Bahîra": "Bu seferler, Peygamberimizin ticaret yollarını, Suriye'deki çarşıları ve farklı inançlardan insanları yakından tanımasını sağladı.",
"Hz. Hatice ile Evlilik": "Bu evlilik, iki tarafın da kendi iradesiyle verdiği bir karardı. Teklifi Hatice'nin kendisinin iletmesi, dönemin toplumunda dikkat çeken bir durumdu.",
"Hira Mağarası ve İlk Vahiy": "Bu olay, Peygamberimizin görevi büyük bir saygı ve ürpertiyle karşıladığını gösterir. Peygamberlik ona kendi arzusuyla verilmemiş, Allah'ın seçimiyle gelmişti.",
"İlk Müslümanlar": "Bu yıllarda Müslümanların sayısı kırk kişiye yaklaşmıştı. Sayı kaynaklarda farklı verilir.",
"Açık Davet ve Safâ Tepesi": "İlerleyen yıllarda davetin sesi Mekke'nin dışına da ulaştı ve hac mevsiminde gelen kabileler Peygamberimizi dinledi.",
"Boykot Yılları": "Boykot sırasında Peygamberimiz, hac mevsiminde gelen insanlara İslam'ı anlatmaya devam etti. Müslümanlar için bu üç yıl, maddi olarak yaşanan en zor dönemlerden biriydi. Yaprak ve deri yiyerek açlığa dayananlar olduğu rivayet edilir.",
"Hüzün Yılı": "Ebû Tâlib'in iman etmemesi üzerine inen Kasas 56. ayet, hidayetin Allah'ın elinde olduğunu bildirir.",
"Muâhât ve Medine Vesikası": "Muhacirlerin bir kısmı Medine'de ticaret ve çiftçilikle geçimini sağlamaya başladı.",
"Uhud Savaşı": "Peygamberimiz savaştan sonra şehitleri Uhud'da defnetti. Ertesi gün Müslümanlar Hamrâülesed'e kadar müşrikleri takip etti.",
"Mektuplar ve Elçiler": "Mektupları götüren sahabeler arasında Dıhye b. Halîfe, Abdullah b. Huzâfe es-Sehmî ve Amr b. Ümeyye gibi isimler vardır.",
"Mekke'nin Fethi": "Fetih öncesinde Hâtıb b. Ebî Belta'a Mekkelilere haber göndermeye kalkışmıştı. Peygamberimiz, Bedir'de bulunduğu için onu bağışladı.",
"Huneyn Savaşı": "Ganimetler Ci'râne'de toplandı. Ardından Peygamberimiz Tâif'i kısa süre kuşattı, fakat sonuç alınmadan ayrıldı.",
"Tebük Seferi": "Peygamberimiz, mazereti yüzünden sefere katılamayanların da sevap kazandığını bildirdi.",
}
def s(b, tarih, paras, ders, kaynak):
    if b in EXTRA: paras = list(paras); paras[-1] += " " + EXTRA[b]
    kaynak = re.sub(r"(?<=[A-Za-zâîûçğıöşü]) \d+(?:-\d+)*(?=$|[;\s(])", "", kaynak)
    return {"baslik": b, "icerik": f"Tarih: {tarih}\n\n" + "\n\n".join(paras) + f"\n\nBu olaydan:\n{ders}\n\nKaynak: {kaynak}"}

C1 = [
s("Fil Yılı ve Doğum",
"Yaklaşık 570-571 (hicretten önce 53 yıl kadar). Rebîülevvel ayının 12. Pazartesi günü olduğu yaygın görüştür; kaynaklarda farklı tarihler verilir.",
["Peygamberimiz Mekke'de, Kureyş kabilesinin Hâşimoğulları kolunda doğdu. Babası Abdullah, o doğmadan önce ticaret dönüşünde Medine'de vefat etmişti. Annesi Âmine'dir. Dedesi Abdülmuttalib ona Muhammed adını verdi. Bu ad Araplar arasında pek yaygın değildi.",
 "Doğduğu yıl Fil yılı diye anılır. Yemen valisi Ebrehe, Kâbe'yi yıkmak amacıyla fillerin de bulunduğu bir orduyla Mekke'ye yürümüştü. Ordu şehre girmeden perişan oldu. Bu olay Fîl suresinde anlatılır. Mekkeliler olaydan sonra Kâbe'ye olan saygılarını daha da artırdılar ve yıl hesabında bu olayı başlangıç aldılar.",
 "Abdülmuttalib torununu Kâbe'ye götürüp Allah'a şükretti. Bebeği kısa bir süre Ebû Leheb'in cariyesi Süveybe emzirdi. Ardından Mekke'nin geleneği gereği süt anne aramaya başlandı."],
"Peygamberimiz yetim doğdu. Çevremizdeki yetim ve kimsesiz çocuklara sahip çıkmak, onun hayatından gelen bir sorumluluktur.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Fîl suresi; Duhâ 93/6"),

s("Süt Annesi Halîme",
"Yaklaşık 570-575. Süre ve ayrıntılar kaynaklarda farklı nakledilir.",
["Mekke eşrafı çocuklarını, çölün temiz havasında büyüsünler ve Arapçayı güzel öğrensinler diye Benî Sa'd gibi bedevi kabilelere verirdi. Süt anne olmak için Mekke'ye gelen kadınlar yetim bir bebek olduğu için Muhammed'i almak istemedi. Çünkü yetimden aileden bir ödül beklemiyorlardı. Halîme bint Ebû Züeyb, başka çocuk bulamayınca onu aldı.",
 "Halîme ve eşi Hâris, bebeği evlerine götürdükten sonra hayvanlarının sütünün ve ailelerinin rızkının arttığını anlatırlar. Çocuk süt çağını Benî Sa'd arasında geçirdi. Sütten kesildikten sonra Halîme onu Mekke'ye getirdi, ancak Âmine bir süre daha kalmasını istedi. Bu yüzden çocuk yaklaşık dört beş yaşına kadar çölde kaldı.",
 "Bu dönemde yaşanan ve melekler tarafından göğsünün yarılması şeklinde anlatılan olay, sahih rivayetlerde yer alır. Bunun üzerine Halîme çocuğu annesine teslim etti."],
"Süt annenin ve çocuğa bakan kişilerin hakkı İslam'da bellidir. Peygamberimiz, ilerleyen yıllarda da süt ailesine karşı vefa göstermiştir.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Müslim, Îmân 261"),

s("Annesinin ve Dedesinin Vefatı",
"Yaklaşık 576 ve 578 (Peygamberimiz altı ve sekiz yaşlarındayken).",
["Âmine, oğluyla birlikte Medine'ye gitti. Eşi Abdullah'ın kabrini ziyaret etmek ve akrabalarını görmek istiyordu. Yanında Ümmü Eymen adlı cariyesi vardı. Bir ay kadar kaldıktan sonra Mekke'ye dönerken Ebvâ denilen yerde hastalanıp vefat etti. Altı yaşındaki Muhammed, Ümmü Eymen'le Mekke'ye döndü.",
 "Dedesi Abdülmuttalib onu yanına aldı. Kâbe'nin gölgesindeki özel minderine yalnızca torununun oturmasına izin verirdi. İki yıl sonra Abdülmuttalib de vefat etti. Bu sırada Muhammed sekiz yaşındaydı. Abdülmuttalib, vefat etmeden önce torununun bakımını oğlu Ebû Tâlib'e emanet etti.",
 "Ebû Tâlib, maddi imkânı geniş biri değildi. Yine de yeğenine kendi çocuklarından ayrı davranmadı. Çocuk, bu evde büyüdü ve amcasıyla ticaret kervanlarına çıkma yaşına geldi."],
"Küçük yaşta anne babasız kalan bir çocuğun akrabalar tarafından korunması, İslam'ın aile hukukunda önemli bir yer tutar. Kimsesiz bir çocuğa kucak açmak büyük sorumluluktur.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Müslim, Cenâiz 108"),

s("Şam Ticareti ve Bahîra",
"Yaklaşık 582 (12 yaşında) ve 595 (25 yaşında).",
["Muhammed on iki yaşlarındayken amcası Ebû Tâlib'le birlikte Şam'a doğru bir ticaret kervanına katıldı. Kervan, Busra yakınlarında Bahîra adlı bir Hıristiyan rahibin manastırına uğradı. Rivayete göre Bahîra, bu çocukta gelecekte bir peygamberin işaretlerini gördü ve Ebû Tâlib'e onu Şam'daki Yahudilerden koruması gerektiğini söyledi. Ebû Tâlib de yeğenini Mekke'ye geri gönderdi. Bu hikâyenin ayrıntıları kaynaklarda farklı anlatılır.",
 "Gençlik yıllarında Muhammed ticaretle ve çobanlıkla uğraştı. Mekkeliler arasında sözünde duran, emanete ihanet etmeyen biri olarak tanındı. Ona el-Emîn (güvenilir) denilmesi bu dönemden kalmadır.",
 "Yirmi beş yaşına geldiğinde Mekke'nin zengin ve itibarlı tüccarı Hatice, kendi malıyla ticaret yapması için ona teklif götürdü. Muhammed, Hatice'nin kölesi Meysere ile birlikte Şam'a gitti ve beklenenden daha fazla kâr getirdi."],
"Güvenilirlik, bir kişinin hayatı boyunca kazandığı itibarın temelidir. Peygamberimiz henüz peygamber olmadan önce de dürüstlüğüyle tanınıyordu.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Tirmizî, Menâkıb 3"),

s("Hz. Hatice ile Evlilik",
"Yaklaşık 595 (Peygamberimiz 25 yaşında). Hatice'nin yaşı ve evlilik tarihi kaynaklarda farklı anlatılır.",
["Hatice bint Huveylid, Mekke'de iffeti ve ticaretteki başarısıyla tanınan bir kadındı. Daha önce iki kez evlenmiş, her ikisinde de dul kalmıştı. Şam'dan dönen Meysere'nin Muhammed'in dürüstlüğüne ve davranışlarına dair anlattıkları onu etkiledi. Kendisi evlenme teklifini arkadaşı Nefîse aracılığıyla iletti.",
 "Teklif, Ebû Tâlib ve amcalarının onayıyla kabul edildi. Nikâh Mekke'de kıyıldı. Yaygın rivayete göre Hatice o sırada kırk yaşındaydı. Çiftin iki oğlu ve dört kızı oldu. Oğulları Kâsım ve Abdullah küçük yaşta vefat etti. Kızları Zeynep, Rukıyye, Ümmü Gülsüm ve Fâtıma'dır.",
 "Hatice, ilk vahiyden sonra Peygamberimizin yanında durdu, malını ve itibarını davanın hizmetine verdi. Peygamberimiz onu ömrü boyunca iyilikle andı. Hatice hayattayken başka bir kadınla evlenmedi."],
"Evlilik, karşılıklı güven ve saygı üzerine kurulur. Peygamberimizin vefat eden eşini her zaman hayırla anması, vefa duygusunun örneğidir.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Buhârî, Menâkıbü'l-Ensâr 20"),

s("Kâbe Hakemliği ve Hacerülesved",
"Yaklaşık 605 (Peygamberimiz 35 yaşında).",
["Kâbe, sel ve yangın nedeniyle hasar görmüştü. Kureyş kabileleri onu yeniden inşa etmeye karar verdi. İnşaat, Hacerülesved'in yerine konacağı noktaya gelince, hangi kabilenin bu şerefi alacağı üzerine tartışma çıktı. Silahlar çekilecek noktaya gelindi. Dört beş gün süren gerginlikten sonra, ertesi sabah Kâbe'ye ilk giren kişinin hakem olması önerildi.",
 "Ertesi sabah Kâbe'ye ilk giren Muhammed oldu. Herkes onu görünce 'Bu el-Emîn, ona razıyız' dedi. Muhammed bir örtü getirtti, taşı örtünün ortasına koydu ve her kabilenin temsilcisinden örtünün bir ucunu tutmasını istedi. Taş yerine gelince onu kendi eliyle yerine yerleştirdi.",
 "Kan dökülmesine yol açabilecek bir mesele, herkesin kabul edeceği bir çözümle bitti. Kureyş, Kâbe'yi inşa ederken yeterli helal malı bulamadığı için Hicr kısmını dışarıda bırakıp daha küçük yaptı."],
"Anlaşmazlıkta herkesin değerini koruyan bir çözüm bulmak, güçlü olmaktan daha değerlidir. Güven duyulan bir kişi, toplumu kavgadan korur.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Müsned-i Ahmed, 3/425"),

s("Hira Mağarası ve İlk Vahiy",
"610 (Peygamberimiz 40 yaşında). Ramazan ayında olduğu kabul edilir; günü kaynaklarda farklı verilir.",
["Muhammed, kırk yaşına yaklaşırken Mekke'nin kalabalığından uzaklaşıp Nûr Dağı'ndaki Hira Mağarası'na çekilmeye başlamıştı. Burada günlerce Allah'a ibadet eder, kâinat üzerinde düşünürdü. Önceleri uykuda gördüğü rüyalar sabah aydınlığı gibi gerçekleşiyordu.",
 "Bir gün mağarada iken Cebrail ona gelip 'Oku' dedi. Muhammed, 'Ben okuma bilmem' diye cevap verdi. Cebrail üç kez bu isteği tekrarladı ve ardından Alak suresinin ilk beş ayetini okudu. Muhammed korkuyla eve geldi ve Hatice'ye 'Beni örtün' dedi. Hatice onu teselli etti ve akrabası Varaka b. Nevfel'e götürdü. Varaka, bunun Mûsâ'ya gelen vahiy gibi olduğunu söyledi.",
 "Bir süre vahiy kesildi. Ardından Müddessir suresinin ilk ayetleri geldi ve Peygamberimiz insanları Allah'a çağırmakla görevlendirildi."],
"İlk emir 'Oku'dur. İslam, ilmi ve okumayı daha ilk ayetinde değerli sayar.",
"Buhârî, Bed'ü'l-vahy 3; Müslim, Îmân 252; Alak 96/1-5; Müddessir 74/1-7"),
]

C2 = [
s("İlk Müslümanlar",
"610-613 (peygamberliğin ilk üç yılı).",
["Davet ilk yıllarda gizli yürütüldü. İlk iman eden Hz. Hatice'dir. Ardından Hz. Ebû Bekir, Hz. Ali (o zaman çocuk yaştaydı) ve Peygamberimizin azatlısı Zeyd b. Hârise Müslüman oldu. Ebû Bekir'in çağrısıyla Osman b. Affân, Abdurrahman b. Avf, Sa'd b. Ebî Vakkâs, Zübeyr b. Avvâm ve Talha b. Ubeydullah da iman etti.",
 "Müslümanlar toplu olarak ibadet edemiyor, namaz için Mekke vadilerine çıkıyordu. Bir süre sonra Safâ yakınındaki Erkam b. Ebi'l-Erkam'ın evi, Müslümanların toplanıp öğrenme yaptığı merkez haline geldi. Burada Kur'an okunur, yeni gelenlere öğretilirdi.",
 "Müslüman olanlar arasında köleler, yoksullar ve gençler çoktu. Fakat Kureyş'in ileri gelenlerinden de bazıları vardı. Bu dönemde vahiy genellikle imanı, ahiret inancını ve ahlakı konu alıyordu."],
"Bir davanın büyümesi güvene bağlıdır. İlk müminler, Peygamberimizin sözüne ve ahlakına güvendikleri için iman etti.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Tirmizî, Menâkıb 15"),

s("Açık Davet ve Safâ Tepesi",
"613 (peygamberliğin 3. yılı). Kaynaklarda farklı tarihler verilir.",
["'Yakın akrabanı uyar' (Şuarâ 214) ayeti inince Peygamberimiz Safâ Tepesi'ne çıkıp Kureyş'i çağırdı. Kabileler toplanınca onlara şunu sordu: Şu dağın arkasında bir düşman atlısı olduğunu haber verse kendisine inanıp inanmayacaklarını sordu. Hepsi 'Evet, senden hiç yalan duymadık' dedi. Ardından 'Ben size şiddetli bir azaptan önce gelen bir uyarıcıyım' dedi.",
 "Amcası Ebû Leheb, 'Helâk ol, bizi bunun için mi topladın' diye karşılık verdi. Bunun üzerine Tebbet suresi indi. Peygamberimiz ayrıca Hâşimoğullarını bir yemeğe davet etti ve onları İslam'a çağırdı. Hz. Ali, yaşı küçük olmasına rağmen kendisini destekleyeceğini söyleyen tek kişi oldu.",
 "Bu andan itibaren davet açık yapıldı ve Mekke'de tepkiler arttı. Kureyş önce alay etti, sonra baskıya yöneldi. Müslümanlara eziyet edilmeye başlandı."],
"Peygamberimiz, çağrısına başlamadan önce güvenilirliğini sorarak toplumun ortak şahitliğini hatırlattı. Dürüstlük, sözün en güçlü dayanağıdır.",
"Buhârî, Tefsîr/Şuarâ 1; Müslim, Îmân 355; Şuarâ 26/214; Tebbet 111"),

s("Habeşistan'a Hicret",
"615 (peygamberliğin 5. yılı, Recep ayı) ve 616. Kaynaklarda farklı tarihler verilir.",
["Mekke'de işkence ve baskı artınca Peygamberimiz, sığınacak bir yer olarak Habeşistan'ı gösterdi. Orada 'kimsenin haksızlık görmediği' adil bir kral, Necâşî hüküm sürüyordu. İlk grup on bir erkek ve dört kadından oluşuyordu. Aralarında Hz. Osman ve eşi Rukıyye vardı.",
 "Daha sonra Cafer b. Ebû Tâlib'in önderliğinde büyük bir grup daha gitti. Kureyş, Amr b. Âs ve Abdullah b. Ebî Rebîa'yı değerli hediyelerle Necâşî'ye gönderdi ve Müslümanların geri verilmesini istedi. Necâşî, Müslümanlara söz hakkı verdi. Cafer, Habeşlilere cahiliye dönemini ve İslam'ın getirdiklerini anlattı, Meryem suresinden ilk ayetleri okudu. Necâşî ve çevresindekiler etkilendi. Kureyş elçileri eli boş döndü.",
 "Müslümanlar bir süre Habeşistan'da huzur içinde yaşadı. Bir kısmı, Mekke'de Müslümanların güçlendiği haberini alınca döndü. Cafer ve arkadaşları ise Hayber zamanına kadar orada kaldı."],
"Dinini yaşamak için güvenli bir yer aramak meşrudur. Adaleti savunan bir yönetici, yabancı bir inanca mensup olsa bile sığınmacıyı korur.",
"İbn Hişâm, es-Sîre; Müsned-i Ahmed, 1/201-202; Meryem 19"),

s("Hz. Ömer'in Müslüman Olması",
"616 (peygamberliğin 6. yılı). Kaynaklarda farklı tarihler verilir.",
["Ömer b. Hattâb, Kureyş'in güçlü ve sert mizaçlı kişilerinden biriydi. Müslümanlara karşı ağır tavır alıyordu. Rivayete göre bir gün kılıcıyla, Peygamberimizi bulmak niyetiyle evden çıktı. Yolda Nuaym b. Abdullah, ona kız kardeşi Fâtıma ile eniştesi Saîd b. Zeyd'in Müslüman olduğunu söyledi.",
 "Ömer onların evine gitti. İçeride Habbâb b. Eret, onlara Kur'an öğretiyordu. Ömer kız kardeşini darp etti. Kanayan Fâtıma, 'Ne yaparsan yap, Müslüman olduk' dedi. Bu cevap Ömer'i yumuşattı. Sahifede yazılı olan Tâhâ suresinin ilk ayetlerini okudu ve çok etkilendi. Ardından Erkam'ın evine gidip Peygamberimizin huzurunda Müslüman oldu.",
 "Peygamberimizin 'Allah'ım, İslam'ı Ömer b. Hattâb veya Ebû Cehil ile güçlendir' diye dua ettiği rivayet edilir. Ömer'in Müslüman olmasından sonra Müslümanlar Kâbe'de açıkça namaz kılmaya başladı. Bundan önce Hz. Hamza da Müslüman olmuştu."],
"Hidayet, insanın en sert olduğu anda da gelebilir. Kur'an ayetleri, sert bir kalbi bile etkileyebilir.",
"İbn Hişâm, es-Sîre; Tirmizî, Menâkıb 17; Tâhâ 20/1-8"),

s("Boykot Yılları",
"616-619 (peygamberliğin 7-10. yılları, yaklaşık üç yıl). Kaynaklarda farklı tarihler verilir.",
["Kureyş ileri gelenleri, Hâşimoğulları ve Muttalipoğulları'nı Peygamberimizi korumaktan vazgeçirmek için bir antlaşma yaptı. Buna göre bu iki kabileyle alışveriş, evlenme ve görüşme yasaklandı. Antlaşma metni Kâbe'nin içine asıldı.",
 "Peygamberimiz, ailesi ve destekçileri, Mekke'nin kenarındaki Şi'b-i Ebû Tâlib adlı vadiye sığındı. Yiyecek kıtlığı vardı. Çocukların ağlaması dışarıdan duyulurdu. Hac mevsimi dışında dışarı çıkılamazdı. Bazı Kureyşliler gizlice yiyecek ulaştırdı.",
 "Rivayete göre antlaşma metnini bir böcek yemiş, yalnızca Allah'ın adının geçtiği yerler kalmıştı. Bunun üzerine Hişâm b. Amr gibi bazı Kureyşliler boykota karşı çıktı ve antlaşma hükümsüz sayıldı. Mü'minler vadiden çıktı."],
"Ablukanın ve yoksunluğun en zor anlarında bile bir topluluk, aynı değerler etrafında birleşirse ayakta kalır.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Buhârî, Hac 45"),

s("Hüzün Yılı",
"619 (peygamberliğin 10. yılı). Kaynaklarda farklı tarihler verilir.",
["Boykotun bitmesinden kısa süre sonra Peygamberimiz arka arkaya iki büyük kayıp yaşadı. Önce amcası Ebû Tâlib vefat etti. Ebû Tâlib iman etmemişti, ancak yeğenini yıllarca Kureyş'e karşı korumuştu. Ölüm döşeğinde Peygamberimiz ona kelime-i şehâdet getirmesi için çağrıda bulundu, fakat o dininde kaldı.",
 "Kısa süre sonra eşi Hatice de vefat etti. İkisinin vefatı arasındaki süre kaynaklarda farklı verilir. Hatice, Peygamberimiz için yalnızca eş değil, aynı zamanda ilk destekçisiydi. Bu yıl Müslümanlar arasında 'Âmü'l-hüzn', yani hüzün yılı olarak anıldı.",
 "Ebû Tâlib'in koruması kalkınca Kureyş'in baskısı arttı. Peygamberimiz, Mekke dışında bir destek aramaya yöneldi. Bu arayış onu Tâif'e götürdü. Aynı dönemde Hz. Sevde ile evlendi."],
"Yakın birini kaybetmek acıdır ve peygamberler de bu acıyı yaşamıştır. Zor günlerde dayanmanın yolu, işine ve sorumluluğuna devam etmektir.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Buhârî, Cenâiz 81"),

s("Tâif'e Gidiş",
"619-620 (peygamberliğin 10. yılı, Şevval ayı). Kaynaklarda farklı tarihler verilir.",
["Peygamberimiz, destek bulmak ve İslam'ı anlatmak için, azatlısı Zeyd b. Hârise ile birlikte Mekke'nin güneydoğusunda bulunan Tâif'e gitti. Sakîf kabilesinin ileri gelenleriyle görüştü, fakat teklifini reddettiler. Ayrıca şehrin serserileri ve çocukları peşinden taş atarak onu şehirden çıkardı. Ayakları kanamıştı.",
 "Peygamberimiz, Tâif'in dışında bir bağa sığındı ve orada Rabbine dua etti. Rivayet edilen duası, gücünün azlığını ve çaresizliğini Allah'a arz etmekle başlar ve Allah'ın rızasını istemekle biter. Bağın sahipleri ona bir tabak üzüm gönderdi. Orada Adaş adlı Hıristiyan köle, Peygamberimizin yemeğe 'Bismillah' diyerek başlamasına şaşırdı. Yûnus Peygamber'den söz edilince ondan etkilendi.",
 "Dağlar meleği ona gelip, isterse Tâif'i iki dağ arasına sıkıştırabileceğini söyledi. Peygamberimiz bunu kabul etmedi ve 'Belki Allah onların soyundan sadece Allah'a ibadet eden insanlar çıkarır' dedi. Dönüşte Nahle'de Kur'an okurken cinlerden bir grup onu dinleyip iman etti."],
"Zulme uğrayan biri, intikam yerine hidayet dileme yolunu seçebilir. Peygamberimiz, kendisine yapılana rağmen kötülük dilemedi.",
"İbn Hişâm, es-Sîre; Buhârî, Bed'ü'l-halk 7; Müslim, Cihâd 111; Ahkâf 46/29-32"),

s("İsrâ ve Mi'rac",
"Hicretten yaklaşık bir yıl önce olduğu kabul edilir. Tam tarihi ve ayı kaynaklarda farklı verilir; Recep'in 27. gecesi yaygın görüştür.",
["Bir gece Peygamberimiz, Mekke'deki Mescid-i Haram'dan Kudüs'teki Mescid-i Aksâ'ya götürüldü. Buna İsrâ denir ve İsrâ suresinin ilk ayetinde anılır. Orada peygamberlere namaz kıldırdı. Ardından Mi'rac denen, göklere yükselme gerçekleşti.",
 "Sahih rivayetlere göre Peygamberimiz bu yükselişte gökleri tek tek geçti ve peygamberlerle karşılaştı. Sidretü'l-müntehâya ulaştı. Allah ona günde elli vakit namaz farz kıldı. Dönüşte Hz. Mûsâ'nın önerisiyle Peygamberimiz birkaç kez dönüp azalttırdı ve sonunda beş vakit kaldı. Sevabı elli vakit sayılır.",
 "Sabah olunca olanları Kureyş'e anlattı. Müşrikler alay etti. Ebû Bekir ise 'O söylediyse doğrudur' dedi ve bu yüzden 'Sıddîk' lakabını aldı. Bu olay inananlarla inanmayanları birbirinden ayırdı. Bu hadisenin nasıl olduğu, ruhla mı bedenle mi gerçekleştiği konusunda âlimler görüş bildirmiştir."],
"Beş vakit namaz, Allah ile kul arasında doğrudan bir bağdır. Peygamberimiz onu mi'racın armağanı olarak anlatmıştır.",
"Buhârî, Salât 1; Müslim, Îmân 259; İsrâ 17/1; Necm 53/13-18"),

s("Akabe Biatları",
"620, 621 ve 622 (peygamberliğin 11, 12 ve 13. yılları, hac mevsimi). Kaynaklarda farklı tarihler verilir.",
["Peygamberimiz her hac mevsiminde Mekke'ye gelen kabilelere kendini tanıtıyordu. 620 yılında Medineli Hazrec kabilesinden altı kişiyle Akabe denen yerde konuştu. Bu kişiler iman edip Medine'ye döndü ve orada İslam'ı anlatmaya başladı.",
 "Ertesi yıl on iki kişi geldi ve Peygamberimize Akabe'de biat etti. Biat metninde Allah'a ortak koşmamak, hırsızlık yapmamak, zina etmemek, çocukları öldürmemek, iftira etmemek ve iyilik emrine karşı gelmemek yer alıyordu. Bu biat 'kadınlar biatı' denen ayetteki şartlara benzerdir. Peygamberimiz onlarla birlikte Mus'ab b. Umeyr'i Medine'ye öğretmen olarak gönderdi.",
 "Üçüncü yıl yetmiş üç erkek ve iki kadın hac sırasında gelip Peygamberimize yardım etmek ve onu savunmak üzere biat etti. Bu biat, hicretin yolunu açtı."],
"Doğru insanlara doğru zamanda ulaşmak sabır ister. Peygamberimiz, reddedilmesine rağmen kabileleri dolaşmaya devam etti ve sonunda karşılığını buldu.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Buhârî, Menâkıbü'l-Ensâr 43; Mümtehine 60/12"),
]

C3 = [
s("Hicret",
"622 (peygamberliğin 13. yılı, Safer-Rebîülevvel). Hicri takvim bu olayla başlar.",
["Akabe biatından sonra Müslümanlar Mekke'den küçük gruplar halinde Medine'ye göç etti. Kureyş, Peygamberimizin de gitmesini önlemek için Dârü'n-Nedve'de toplandı. Her kabileden bir genç seçip onu birlikte öldürme kararı aldı. Allah bu planı Peygamberimize bildirdi.",
 "Peygamberimiz geceleyin evinden çıktı. Hz. Ali, yatağında yattı ve Mekkelilerin emanetlerini sahiplerine geri vermekle görevlendirildi. Peygamberimiz Ebû Bekir ile birlikte Mekke'nin güneyindeki Sevr Mağarası'na sığındı. Üç gün orada kaldılar. Müşrikler mağaranın ağzına kadar geldi. Peygamberimiz Ebû Bekir'e, 'Üzülme, Allah bizimle beraberdir' dedi. Bu olay Tevbe 40. ayette anlatılır.",
 "Sonra yol göstericileri Abdullah b. Üreykıt'in rehberliğinde sahil yolunu izleyerek Medine'ye yöneldiler. Arkalarından Sürâka b. Mâlik yetişmek istedi, ancak atı çöle saplandı ve dönmek zorunda kaldı. Peygamberimiz, Rebîülevvel ayında Medine yakınlarına ulaştı."],
"Hicret, yalnızca bir yer değiştirme değil, inancı yaşamak için fedakârlık yapma örneğidir. Tevekkül, tedbiri bırakmak anlamına gelmez; Peygamberimiz hazırlık yapıp sonra Allah'a dayandı.",
"İbn Hişâm, es-Sîre; Buhârî, Menâkıbü'l-Ensâr 45; Tevbe 9/40; Enfâl 8/30"),

s("Kubâ ve Mescid-i Nebevî",
"622 (1 Hicri, Rebîülevvel).",
["Peygamberimiz Medine'ye varmadan önce Kubâ köyünde Amr b. Avf oğullarının yanında kaldı. Burada bir mescit yapıldı. Bu, İslam'ın ilk mescidi olarak bilinir ve Tevbe 108. ayette 'ilk günden takva üzerine kurulan mescit' diye anılır. Hz. Ali de birkaç gün sonra buraya geldi.",
 "Cuma günü Peygamberimiz Medine'ye doğru yola çıktı. Yol boyunca her kabile ona misafir olmak istiyordu. Devesini serbest bıraktı ve 'Bırakın, o emir almıştır' dedi. Deve, bugün Mescid-i Nebevî'nin bulunduğu yere çöktü. Burası iki yetim çocuğa aitti. Peygamberimiz arsayı satın aldı. Bu sırada Ebû Eyyûb el-Ensârî'nin evinde misafir kaldı.",
 "Mescit, hurma kütükleri ve kerpiçle inşa edildi. Peygamberimiz inşaat sırasında Müslümanlarla birlikte çalıştı. Mescit yalnızca ibadet yeri değildi. Burada eğitim verildi, kararlar alındı, misafirler ağırlandı. Yanına, yoksul muhacirlerin kaldığı Suffe de eklendi."],
"Bir toplumun merkezinde bulunan mescit, ibadetin yanı sıra eğitim ve dayanışma yeridir. Peygamberimiz mescidi herkesin birlikte çalıştığı bir yer olarak kurdu.",
"İbn Hişâm, es-Sîre; Buhârî, Menâkıbü'l-Ensâr 45-46; Tevbe 9/108"),

s("Muâhât ve Medine Vesikası",
"622-623 (1-2 Hicri). Kaynaklarda farklı tarihler verilir.",
["Mekke'den gelen muhacirler, mallarını ve evlerini geride bırakmıştı. Peygamberimiz, muhacirlerle Medineli Ensâr arasında kardeşlik bağı kurdu. Buna muâhât denir. Ensâr, evlerini ve mallarını paylaştı. Abdurrahman b. Avf, kardeşi Sa'd b. Rebî'in malının yarısını kabul etmeyip yalnızca çarşıyı sorarak ticarete başladı.",
 "Peygamberimiz aynı dönemde, Medine'deki Müslümanlar, Yahudiler ve diğer topluluklarla bir anlaşma yaptı. Buna Medine Vesikası ya da Medine Sözleşmesi denir. Metin, şehrin ortak güvenliğini ve herkesin kendi dinini yaşama hakkını düzenler. Saldırı durumunda şehri birlikte savunma, adalet ve emanet gibi ilkeler vardı. Anlaşmanın bazı maddeleri ve tarihi kaynaklarda farklı aktarılsa da, genel çerçevesi İbn Hişâm'da yer alır.",
 "Bu düzenle Medine, farklı inançlardan ve kabilelerden oluşan ortak bir şehir devleti haline geldi."],
"Dayanışma, paylaşmayı bilen insanların elinde güçlenir. Farklı inançlardan insanların aynı şehirde güvenle yaşaması, yazılı kurallara dayandırılmıştır.",
"İbn Hişâm, es-Sîre; Buhârî, Menâkıbü'l-Ensâr 3; Haşr 59/9"),

s("Ezan ve Kıblenin Değişmesi",
"1-2 Hicri (623-624). Kıblenin değişmesi, Receb veya Şaban 2 Hicri olarak aktarılır; kaynaklarda farklı tarihler verilir.",
["Medine'de Müslümanlar kalabalıklaşınca insanları namaza çağırmak için bir yöntem aranmaya başladı. Bazı sahabeler boru, çan veya ateş gibi önerilerde bulundu. Abdullah b. Zeyd, rüyasında ezan okuyan birini gördü ve bunu Peygamberimize anlattı. Peygamberimiz rüyayı doğruladı. Hz. Ömer de aynı rüyayı görmüştü. Sesi güzel olduğu için Bilâl-i Habeşî ilk müezzin oldu.",
 "Müslümanlar Medine'nin ilk aylarında Kudüs'teki Mescid-i Aksâ'ya yönelerek namaz kıldı. Peygamberimiz ise Kâbe'ye dönmek istiyordu. Hicretten yaklaşık on altı veya on yedi ay sonra Bakara 144. ayet indi ve kıble Kâbe oldu. Rivayete göre bu emir, namaz sırasında geldi ve cemaat namazın ortasında yönünü değiştirdi.",
 "Aynı dönemde oruç ve zekât da farz kılındı. Böylece İslam'ın ibadet düzeni Medine'de netleşti."],
"Kıble, Müslümanlara ortak bir yön, ortak bir kimlik verir. Ezan da topluluğu aynı vakitte bir araya getirir.",
"Buhârî, Ezân 1; Ebû Dâvûd, Salât 28; Tirmizî, Salât 140; Bakara 2/144"),
]

C4 = [
s("Bedir Savaşı",
"13 Mart 624 (17 Ramazan 2 Hicri).",
["Mekke'den gelen ve Ebû Süfyân'ın yönettiği büyük bir Kureyş ticaret kervanını durdurmak için Peygamberimiz Medine'den çıktı. Kervan başka yoldan kaçınca Kureyş, Ebû Cehil önderliğinde yaklaşık bin kişilik bir ordu ile Bedir kuyularına geldi. Müslümanların sayısı üç yüz on üç civarındaydı. Yanlarında çok az at ve deve vardı.",
 "Savaştan önce Peygamberimiz dua etti ve sahabelerle istişare yaptı. Hubâb b. Münzir'in önerisi ile su kuyularının başında mevzilenildi. Savaş, Müslümanların zaferiyle sonuçlandı. Müşriklerden yetmiş kişi öldü, yetmiş kişi esir alındı. Müslümanlardan on dört kişi şehit düştü. Ebû Cehil de ölenler arasındaydı.",
 "Esirlerden okuma yazma bilenlere, on Müslüman çocuğa yazmayı öğretme karşılığında serbest bırakılma imkânı verildi. Diğerleri fidye karşılığında salındı. Enfâl suresi bu savaş hakkında konuşur."],
"Zafer, sayı ve araçtan değil, Allah'a güvenle birlikte hazırlık ve birlikten doğar. Esirlere ilim öğretme şartı, bilgiye verilen değeri gösterir.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 4; Müslim, Cihâd 58; Enfâl 8; Âl-i İmrân 3/123"),

s("Uhud Savaşı",
"23 Mart 625 (Şevval 3 Hicri). Kaynaklarda farklı tarihler verilir.",
["Kureyş, Bedir'in intikamını almak üzere yaklaşık üç bin kişiyle Medine yakınlarına geldi. Peygamberimiz, Uhud Dağı'nın eteğinde yedi yüz kişilik bir ordu ile karşıladı. Yolda Abdullah b. Übeyy, kendi adamlarıyla orduyu terk edip geri döndü.",
 "Peygamberimiz, savaş alanındaki bir tepenin korunması için elli okçu bıraktı ve 'Biz galip de gelsek, yenilsek de buradan ayrılmayın' dedi. Savaşın ilk anlarında Müslümanlar üstünlük sağladı. Müşrikler geri çekilince okçuların çoğu ganimet toplamak düşüncesiyle tepeyi terk etti. Halid b. Velîd, bu boşluktan Müslümanları arkadan vurdu.",
 "Müslümanlar dağıldı. Yetmiş sahabe şehit düştü, aralarında Hz. Hamza da vardı. Peygamberimiz yaralandı, dişi kırıldı. Müşrikler Mekke'ye döndü. Âl-i İmrân suresinin birçok ayeti bu olayı değerlendirir ve Müslümanlara ders verir."],
"Emre uymamanın bedeli ağır olabilir. Kaybedilen savaş, sabrı ve yenilgiden ders çıkarmayı da gerektirir.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 18; Âl-i İmrân 3/121-175"),

s("Hendek Savaşı",
"627 (Şevval 5 Hicri). Kuşatmanın süresi kaynaklarda farklı verilir; yaklaşık bir ay sürdüğü bildirilir.",
["Medine'den çıkarılan Nadîr oğulları Yahudileri, Kureyş'i ve diğer kabileleri Medine'ye saldırmaya ikna etti. Yaklaşık on bin kişilik bir ordu şehre yöneldi. Müslümanlar ise üç bin kadardı. Selmân-ı Fârisî, Medine'nin açık tarafına hendek kazılmasını önerdi. Bu savaş yöntemi Araplar arasında bilinmiyordu.",
 "Hendek, soğuk kış günlerinde yaklaşık altı günde kazıldı. Sahabeler açlıktan karınlarına taş bağladı. Peygamberimiz de onlarla birlikte kazdı. Kuşatma süresince müşrikler hendeği geçmeye çalıştı, fakat başarılı olamadı. Ağır bir fırtına ve soğuk müşriklerin çadırlarını devirdi. Ordu dağılıp geri döndü.",
 "Medine'deki Kureyzaoğulları Yahudileri, Müslümanlarla yaptıkları antlaşmayı bozup müşriklere destek olmaya yeltenmişti. Kuşatma bitince Peygamberimiz onların üzerine yürüdü. Hakem olarak seçilen Sa'd b. Muâz'ın kendi kitaplarına göre verdiği hüküm uygulandı. Ahzâb suresi bu olayları anlatır."],
"Zorluk karşısında akıllı bir plan ve ortak çalışma, güç dengesizliğini aşabilir. Peygamberimiz, liderliğini sahabeleriyle birlikte çalışarak da gösterdi.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 29; Ahzâb 33/9-27"),

s("Hudeybiye Antlaşması",
"628 (Zilkade 6 Hicri, Mart).",
["Peygamberimiz, yaklaşık bin dört yüz sahabeyle birlikte umre yapmak niyetiyle Mekke'ye yöneldi. Silah olarak sadece kılıç taşıyorlardı ve savaş niyetinde değillerdi. Kureyş, şehre girmelerine izin vermedi. Hudeybiye denen yerde konaklandı. Peygamberimiz, Hz. Osman'ı görüşmeler için Mekke'ye gönderdi. Hz. Osman'ın öldürüldüğü haberi yayılınca, sahabeler ağacın altında Peygamberimize biat etti. Bu biat 'Rıdvan biatı' diye bilinir.",
 "Sonra Süheyl b. Amr ile bir antlaşma yapıldı. Müslümanlar o yıl umre yapmadan dönecek, gelecek yıl üç gün için Mekke'ye girecekti. On yıl savaş olmayacaktı. Mekke'den Müslüman olup Medine'ye kaçanlar geri verilecek, tersi ise geçerli olmayacaktı. Bazı sahabeler bu şartları ağır buldu. Fakat Peygamberimiz kabul etti.",
 "Dönüşte Fetih suresi indi ve bu antlaşma 'apaçık bir fetih' diye nitelendi. Barış ortamı sayesinde insanlar Müslümanlarla rahatça konuştu ve İslam'a girenlerin sayısı kısa sürede çok arttı."],
"Kısa vadede kayıp gibi görünen bir barış, uzun vadede büyük kazanç getirebilir. Sabır ve görüş genişliği, hemen sonuç beklemekten daha değerlidir.",
"İbn Hişâm, es-Sîre; Buhârî, Şurût 15; Fetih 48/1-18"),

s("Hayber",
"628 (Muharrem 7 Hicri, Mayıs). Kaynaklarda farklı tarihler verilir.",
["Hayber, Medine'nin kuzeyinde Yahudilerin yaşadığı, surlu kalelerle çevrili verimli bir vahaydı. Nadîr oğulları Yahudilerinin bir kısmı buraya yerleşmiş ve Müslümanlara karşı Arap kabileleri arasında düşmanlık örgütlemişti. Hudeybiye'den döndükten kısa süre sonra Peygamberimiz Hayber'e yürüdü.",
 "Müslümanlar kaleleri tek tek kuşattı. Bazı kaleler uzun süre dayandı. Sonunda Hz. Ali'nin liderliğinde Kamûs Kalesi alındı. Hayber halkı, topraklarını işleyerek ürünün yarısını Müslümanlara vermek şartıyla, yerinde kalmaya razı oldu. Aynı dönemde Habeşistan'dan Cafer b. Ebû Tâlib ve arkadaşları Medine'ye döndü; Peygamberimiz onları görünce büyük sevinç duydu.",
 "Bu sırada Zeynep bint Hâris adlı bir kadın Peygamberimize zehirli kuzu eti ikram etti. Peygamberimiz tadınca zehirli olduğunu fark edip yemeyi bıraktı. Yemekten yiyen Bişr b. Berâ vefat etti."],
"Barış antlaşması yapıldıktan sonra, güvenliği tehdit edenlerle uğraşmak mümkün hale gelir. Yenilen halkla adil bir düzen kurmak da savaşın bir parçasıdır.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 38-39; Müslim, Cihâd 120"),

s("Mektuplar ve Elçiler",
"628-629 (7 Hicri). Mektupların gönderilme sırası kaynaklarda farklı verilir.",
["Hudeybiye'den sonra Peygamberimiz çevredeki hükümdarlara mektuplar gönderdi. Mektuplar, Bizans imparatoru Herakleios, Sasani hükümdarı Hüsrev Perviz, Mısır'daki Mukavkıs, Habeşistan'da Necâşî ve çeşitli Arap emîrlerine ulaştı. Mektuplara basılmak üzere 'Muhammedün Resûlullâh' yazılı bir mühür yaptırıldı.",
 "Herakleios, mektubu aldıktan sonra Mekke'den gelen bir tüccar olan Ebû Süfyân'ı çağırıp Peygamberimiz hakkında sorular sordu. Ebû Süfyân'ın dürüst cevapları karşısında etkilendiğini söylemişse de İslam'ı kabul etmedi. Hüsrev Perviz mektubu yırttı. Mukavkıs ise nazik bir yanıt verip hediyeler gönderdi.",
 "Mektuplarda, yalnızca Allah'a kulluk etmeye, ortak koşmamaya ve Allah'ın elçisini kabul etmeye çağrı vardı. Peygamberimiz, mesajın tüm insanlara yönelik olduğunu bu şekilde duyurdu. Mektupların metinleri hadis ve siyer kitaplarında aktarılır."],
"Barışın sağlandığı bir dönemi, iyi niyetle iletişim kurmak için değerlendirmek mümkündür. Peygamberimiz, mesajını yazılı ve nazik bir dille iletti.",
"Buhârî, Bed'ü'l-vahy 6; Müslim, Cihâd 74-75; İbn Sa'd, et-Tabakât"),
]

C5 = [
s("Mekke'nin Fethi",
"630 (20 Ramazan 8 Hicri, Ocak).",
["Hudeybiye antlaşmasında Kureyş'in müttefiki Benî Bekir, Müslümanların müttefiki Huzâa'ya saldırdı. Kureyş de Benî Bekir'e destek verince antlaşma bozulmuş oldu. Ebû Süfyân yenilemeye çalışsa da kabul edilmedi. Peygamberimiz yaklaşık on bin kişilik bir orduyla Mekke'ye yürüdü. Gizlice hazırlık yapıldı ve şehre kan akıtılmadan girmeye çalışıldı.",
 "Ebû Süfyân yolda yakalandı ve müslüman oldu. Peygamberimiz 'Ebû Süfyân'ın evine giren güvendedir, silahını bırakan güvendedir' diye ilan ettirdi. Şehre dört koldan girildi, yalnızca bir yerde küçük bir çatışma çıktı. Peygamberimiz Kâbe'ye geldi, tavaf etti ve içindeki putları kırdırdı. Bu sırada 'Hak geldi, batıl yok oldu' (İsrâ 81) ayetini okudu.",
 "Daha sonra Mekkelilere hitap etti ve geçmişte kendisine eziyet edenleri affetti. Bilâl-i Habeşî, Kâbe'nin üzerinde ezan okudu. Mekke'nin yönetimi Müslümanlara geçti."],
"Gücü eline geçiren biri affetmeyi seçebilir. Peygamberimiz yıllarca eziyet edenlere intikam yerine af ilan etti.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 47-49; Müslim, Cihâd 84; Fetih 48; Nasr 110"),

s("Huneyn Savaşı",
"630 (Şevval 8 Hicri). Kaynaklarda farklı tarihler verilir.",
["Mekke fethinden kısa süre sonra Hevâzin ve Sakîf kabileleri Müslümanlara karşı toplandı. Peygamberimiz, yaklaşık on iki bin kişilik bir orduyla yola çıktı. Bunların on bini Medine'den, iki bini yeni Müslüman olan Mekkelilerdendi. Sayıca üstün olmaktan dolayı bazı kişiler kendilerine güven duydu.",
 "Huneyn Vadisi'nde Hevâzin okçuları pusudan saldırdı. Müslümanlar bir an dağıldı. Peygamberimiz yerinde kaldı ve Abbas b. Abdülmuttalib'e orduyu toplamasını söyledi. Sahabeler yeniden toparlandı ve savaş Müslümanların zaferiyle bitti. Tevbe suresi 25. ayet, bu olayda sayıya güvenmenin işe yaramadığını hatırlatır.",
 "Ganimetler dağıtılırken Peygamberimiz yeni Müslüman olanlara daha fazla pay verdi, kalplerini kazanmak için. Hevâzin heyeti gelip Müslüman oldu. Peygamberimiz, esirleri ve mallarını onlara geri verdi."],
"Sayıya güvenmek, bazen insanı gevşetir. Kazanılan zaferde başkalarının gönlünü kazanmak da önemli bir görevdir.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 54-56; Müslim, Cihâd 78; Tevbe 9/25-26"),

s("Tebük Seferi",
"630-631 (Recep 9 Hicri). Kaynaklarda farklı tarihler verilir.",
["Bizans'ın Müslümanlara karşı Suriye sınırında asker topladığı haberi geldi. Peygamberimiz, çok sıcak bir yaz ve kıtlık zamanında yaklaşık otuz bin kişilik bir orduyla Tebük'e yürüdü. Bu yüzden ordunun adı 'Ceyşü'l-Usre' (zorluk ordusu) olarak anılır. Hz. Osman, Hz. Ebû Bekir ve diğer sahabeler büyük bağışlar yaptı.",
 "Tebük'e varıldığında Bizans ordusunun toplanmadığı anlaşıldı. Peygamberimiz yaklaşık yirmi gün kaldı. Bölgedeki bazı Hıristiyan ve Yahudi yönetimlerle anlaşmalar yapıldı, örneğin Eyle (Akabe) ve Cerbâ halkıyla. Münafıklar bu sefere katılmamak için bahaneler üretti.",
 "Kâ'b b. Mâlik, Mürâre b. Rebî ve Hilâl b. Ümeyye, bir bahane olmadan seferden geri kaldılar. Peygamberimiz onlarla konuşmayı yasakladı. Elli gün sonra tövbeleri kabul edildi. Bu olay Tevbe 118. ayette geçer."],
"Zor ve sıkıntılı zamanda bile görevden kaçmamak gerekir. Hata yapan, dürüstçe itiraf edip tövbe ederse affedilir.",
"İbn Hişâm, es-Sîre; Buhârî, Meğâzî 79; Müslim, Tevbe 53; Tevbe 9/38-129"),

s("Veda Haccı ve Hutbesi",
"632 (Zilhicce 10 Hicri). Arafat günü 9 Zilhicce, Cuma günü.",
["Peygamberimiz, hicretten sonra tek hac yaptı. Onunla birlikte hac yapanların sayısı kaynaklarda farklı verilir, on binlerce kişiden söz edilir. Hac menâsikini kendi uygulamasıyla öğretti ve 'Hac ibadetlerinizi benden öğrenin' dedi. Arafat'ta Urene Vadisi'nde, devesinin üzerinde bir hutbe okudu. Bu hutbe 'Veda Hutbesi' diye bilinir.",
 "Hutbede şu ilkeleri vurguladı: Müslümanın canı, malı ve namusu birbirine haramdır. Cahiliye döneminin faizi ve kan davaları kaldırılmıştır. Kadınlara iyi davranılmalıdır. Arap'ın Arap olmayana, beyazın siyaha üstünlüğü yoktur; üstünlük ancak takva iledir. Kendinizden sonra Allah'ın Kitabı'na sarılırsanız sapmazsınız. Sonunda cemaate görevi yerine getirip getirmediğini sordu ve cemaat 'Evet' dedi. Peygamberimiz, 'Şahit ol Allah'ım' dedi.",
 "Aynı gün Mâide 3. ayet indi ve dinin tamamlandığı bildirildi. Hac sonrası Medine'ye dönüldü."],
"Hutbe, her insanın değerini, canının, malının ve namusunun dokunulmazlığını vurgular. İnsanlar arasındaki üstünlük, soy veya ten rengiyle değil, takvayla ölçülür.",
"Müslim, Hac 147; Buhârî, Hac 132; Mâide 5/3; Hucurât 49/13"),

s("Vefatı",
"8 Haziran 632 (12 Rebîülevvel 11 Hicri, Pazartesi). Kaynaklarda farklı tarihler verilir.",
["Peygamberimiz Safer ayının sonlarında hastalandı. Hastalık on gün civarında sürdü. Hz. Âişe'nin odasında kalmak için eşlerinden izin aldı. Hastalığında namaz kıldıramadığı için Ebû Bekir'i imam tayin etti. Ebû Bekir'in imamlığında namaz kılınırken bir an perdeyi aralayıp cemaate baktı ve gülümsedi. Vefat günü sabahı bu, son görüşüydü.",
 "Pazartesi günü kuşluk vaktinde, altmış üç yaşında vefat etti. Hz. Ömer bu habere inanamadı ve haberi yayanlara karşı çıktı. Ebû Bekir geldi ve minberde şöyle dedi: 'Kim Muhammed'e tapıyorsa bilsin ki Muhammed ölmüştür. Kim Allah'a tapıyorsa bilsin ki Allah diridir, ölmez.' Ardından Âl-i İmrân 144. ayeti okudu. Hz. Ömer bu ayeti duyunca gerçeği kabul etti.",
 "Peygamberimiz, vefat ettiği odaya defnedildi. Bu, bugünkü Mescid-i Nebevî'nin içinde yer alır. Cenaze namazı, kalabalık nedeniyle gruplar halinde ve imamsız kılındı."],
"Peygamberler de ölümlüdür. İslam'da bağlılık kişiye değil Allah'a ve O'nun emirlerinedir.",
"İbn Hişâm, es-Sîre; İbn Sa'd, et-Tabakât; Buhârî, Cenâiz 3; Meğâzî 83; Âl-i İmrân 3/144"),

s("Ahlakı ve Günlük Hayatı",
"Peygamberliğin 23 yılı boyunca (610-632).",
["Kur'an Peygamberimiz hakkında 'Sen elbette büyük bir ahlak üzerindesin' (Kalem 4) der. Hz. Âişe, ahlakının Kur'an olduğunu söylemiştir. Evde ailesinin işlerine yardım eder, elbisesini diker, ayakkabısını tamir ederdi. Hizmetçisini ve çocukları azarlamaz, onlara iyi davranırdı. Anas b. Mâlik on yıl onun hizmetinde bulunmuş ve kendisine hiçbir zaman 'öf' dememişti.",
 "Çok az yemek yer, çoğunlukla hurma ve su ile yetinirdi. Zaman zaman evinde günlerce ateş yakılmazdı. Hasırın üzerinde yattığı için sırtında izleri kalırdı. Geceleri uzun süre namaz kılar, ayakları şişene kadar ibadet ederdi. Yetimlere, yoksullara ve hastalara yakın ilgi gösterirdi. Çocuklarla oynar, Müslüman olmayan komşusu hastalanınca onu ziyaret ederdi.",
 "Verdiği sözü tutar, yalan söylemezdi. Hakkında konuşulurken övgü karşısında mütevazı kalırdı ve 'Beni Hıristiyanların Meryem oğlunu abarttığı gibi abartmayın' derdi."],
"Peygamberimizin örnek olması, yaşantısının her yönüyle insanlara yakın ve uygulanabilir olmasındandır. Sade yaşamak, iyi davranmak ve sözünde durmak herkes için yapılabilir davranışlardır.",
"Kalem 68/4; Ahzâb 33/21; Müslim, Müsâfirîn 139; Buhârî, Edeb 39; Ahmed b. Hanbel, Müsned"),
]

book = {
 "id": "siyer_book",
 "baslik": "Peygamberimizin Hayatı",
 "yazar": "Vera Kütüphane",
 "renk": ["#047857", "#064E3B"],
 "ciltler": [
  {"ad": "Doğumdan Peygamberliğe", "sayfalar": C1},
  {"ad": "Mekke Dönemi", "sayfalar": C2},
  {"ad": "Hicret ve Medine'nin İlk Yılları", "sayfalar": C3},
  {"ad": "Gazveler ve Antlaşmalar", "sayfalar": C4},
  {"ad": "Mekke'nin Fethi ve Veda", "sayfalar": C5},
 ]
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(book, f, ensure_ascii=False, indent=2)
b = json.load(open(OUT, encoding="utf-8"))
n = 0
for c in b["ciltler"]:
    for p in c["sayfalar"]:
        n += 1
        w = len(p["icerik"].split())
        if not 150 <= w <= 280: print("WORDS", w, p["baslik"])
print(n)
