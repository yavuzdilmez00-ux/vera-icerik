import json, re
OUT = r"C:\Users\dared\AppData\Local\Temp\claude\016efd8e3f2a5ef4\6b8db417-ae01-422c-aca1-b9fd8cd931a6\scratchpad\vera-icerik\kitaplar_kaynak\19_kuran_sunnet_dualari_book.json"

def d(b, o, a, z, k):
    k = re.sub(r"(?<=[A-Za-zâîûçğıöşü]) \d+(?:-\d+)*(?=$|[;\s(])", "", k)
    return {"baslik": b, "icerik": f"Okunuşu:\n{o}\n\nAnlamı:\n{a}\n\nNe zaman okunur:\n{z}\n\nKaynak: {k}"}

K = []
K.append(d("Rabbenâ Tekabbel Minnâ (Bakara 127-128)",
"Rabbenâ tekabbel minnâ, inneke entes-semîul-alîm. Rabbenâ vec'alnâ müslimeyni leke ve min zürriyyetinâ ümmeten müslimeten leke ve erinâ menâsikenâ ve tüb aleynâ, inneke entet-tevvâburrahîm.",
"Ey Rabbimiz, bizden kabul buyur. Şüphesiz sen işitirsin, bilirsin. Ey Rabbimiz, bizi sana teslim olmuş kıl, soyumuzdan da sana teslim olmuş bir ümmet çıkar. Bize ibadet usullerimizi göster ve tövbemizi kabul et. Şüphesiz tövbeleri çokça kabul eden, çok merhametli olan sensin.",
"Bir ibadeti ya da hayırlı bir işi tamamladıktan sonra, kabul olması için okunur.",
"Bakara suresi, 127-128. ayetler (Hz. İbrahim ve Hz. İsmail'in Kâbe'yi inşa ederken yaptığı dua)"))
K.append(d("Dünya ve Ahiret İyiliği (Bakara 201)",
"Rabbenâ âtinâ fid-dünyâ haseneten ve fîl-âhirati haseneten ve kınâ azâben-nâr.",
"Ey Rabbimiz, bize dünyada da iyilik ver, ahirette de iyilik ver ve bizi ateş azabından koru.",
"Hac ve umrede Rükn-i Yemânî ile Hacerülesved arasında okunur; her zaman da okunabilir.",
"Bakara suresi, 201. ayet; Buhârî, Daavât 55 (Peygamberimizin en çok okuduğu dualardandır)"))
K.append(d("Sabır ve Sebat Duası (Bakara 250)",
"Rabbenâ efrığ aleynâ sabran ve sebbit akdâmenâ vensurnâ alel-kavmil-kâfirîn.",
"Ey Rabbimiz, üzerimize sabır yağdır, ayaklarımızı sağlam bastır ve kâfirler topluluğuna karşı bize yardım et.",
"Zor bir imtihanda ya da haksızlığa karşı dayanma gücü istenirken okunur.",
"Bakara suresi, 250. ayet (Câlût'la karşılaşan Tâlût'un askerlerinin duası)"))
K.append(d("Bakara Suresi'nin Son Duası (Bakara 286)",
"Rabbenâ lâ tüâhıznâ in nesînâ ev ahta'nâ. Rabbenâ ve lâ tahmil aleynâ ısran kemâ hameltehû alellezîne min kablinâ. Rabbenâ ve lâ tühammilnâ mâ lâ tâkate lenâ bih. Va'fü annâ, vağfir lenâ, verhamnâ, ente mevlânâ fensurnâ alel-kavmil-kâfirîn.",
"Ey Rabbimiz, unutursak ya da yanılırsak bizi sorumlu tutma. Ey Rabbimiz, bizden öncekilere yüklediğin gibi ağır bir yük yükleme. Ey Rabbimiz, gücümüzün yetmediği şeyi bize taşıtma. Bizi affet, bizi bağışla, bize merhamet et. Sen bizim sahibimizsin; kâfirler topluluğuna karşı bize yardım et.",
"Günün sonunda, hata ve unutkanlık için af dilerken okunur.",
"Bakara suresi, 286. ayet; Buhârî, Fezâilü'l-Kur'ân 10 (geceleyin bu iki ayeti okuyana kâfi gelir)"))
K.append(d("Kalbin Doğrudan Ayrılmaması İçin (Âl-i İmrân 8)",
"Rabbenâ lâ tüziğ kulûbenâ ba'de iz hedeytenâ ve heb lenâ min ledünke rahmeh, inneke entel-vehhâb.",
"Ey Rabbimiz, bizi doğru yola ilettikten sonra kalplerimizi eğriltme. Bize katından bir rahmet bağışla. Şüphesiz çok bağışlayan sensin.",
"Hidayet üzere kalabilmek için okunur.",
"Âl-i İmrân suresi, 8. ayet"))
K.append(d("İman ve Mağfiret Duası (Âl-i İmrân 16)",
"Rabbenâ innenâ âmennâ fağfir lenâ zünûbenâ ve kınâ azâben-nâr.",
"Ey Rabbimiz, biz iman ettik; günahlarımızı bağışla ve bizi ateş azabından koru.",
"Günahtan tövbe ederken ve geceleyin istiğfar sırasında okunur.",
"Âl-i İmrân suresi, 16. ayet"))
K.append(d("Salih Evlat Duası (Âl-i İmrân 38)",
"Rabbi heb lî min ledünke zürriyyeten tayyibeh, inneke semîud-duâ.",
"Rabbim, bana katından temiz bir nesil bağışla. Şüphesiz sen duayı işitensin.",
"Hayırlı evlat isteyen anne babalar tarafından okunur.",
"Âl-i İmrân suresi, 38. ayet (Hz. Zekeriyyâ'nın duası)"))
K.append(d("Ayakların Kaymaması İçin (Âl-i İmrân 147)",
"Rabbeğfir lenâ zünûbenâ ve isrâfenâ fî emrinâ ve sebbit akdâmenâ vensurnâ alel-kavmil-kâfirîn.",
"Ey Rabbimiz, günahlarımızı ve işimizdeki taşkınlıklarımızı bağışla, ayaklarımızı sağlam bastır ve kâfirler topluluğuna karşı bize yardım et.",
"Zorlu bir işe girerken ya da hata yaptığını fark edince okunur.",
"Âl-i İmrân suresi, 147. ayet"))
K.append(d("Tefekkür Duası (Âl-i İmrân 191-192)",
"Rabbenâ mâ halakte hâzâ bâtılâ, sübhâneke fekınâ azâben-nâr. Rabbenâ inneke men tüdhılin-nâre fekad ahzeytehû, ve mâ liz-zâlimîne min ensâr.",
"Ey Rabbimiz, sen bunu boşuna yaratmadın. Seni tenzih ederiz; bizi ateşin azabından koru. Ey Rabbimiz, sen kimi ateşe sokarsan onu rezil etmiş olursun. Zalimlerin hiçbir yardımcısı yoktur.",
"Gece uyanınca ya da gökyüzüne ve yaratılışa bakıp düşünürken okunur.",
"Âl-i İmrân suresi, 191-192. ayetler; Buhârî, Tefsîr (Peygamberimiz gece kalkınca bu ayetleri okurdu)"))
K.append(d("Vaadin Gerçekleşmesi Duası (Âl-i İmrân 193-194)",
"Rabbenâ innenâ semi'nâ münâdiyen yünâdî lil-îmâni en âminû bi-rabbikum fe-âmennâ. Rabbenâ fağfir lenâ zünûbenâ ve keffir annâ seyyiâtinâ ve teveffenâ meal-ebrâr. Rabbenâ ve âtinâ mâ veadtenâ alâ rusulike ve lâ tuhzinâ yevmel-kıyâmeh, inneke lâ tuhliful-mî'âd.",
"Ey Rabbimiz, biz 'Rabbinize iman edin' diye çağıran bir davetçiyi işittik ve iman ettik. Ey Rabbimiz, günahlarımızı bağışla, kötülüklerimizi ört ve canımızı iyilerle beraber al. Ey Rabbimiz, peygamberlerin aracılığıyla bize vadettiğini ver ve kıyamet günü bizi rezil etme. Şüphesiz sen sözünden dönmezsin.",
"Ahiretteki kurtuluşu dilerken okunur.",
"Âl-i İmrân suresi, 193-194. ayetler"))
K.append(d("Kendimize Zulmettik Duası (A'râf 23)",
"Rabbenâ zalemnâ enfusenâ ve in lem tağfir lenâ ve terhamnâ lenekûnenne minel-hâsirîn.",
"Ey Rabbimiz, biz kendimize zulmettik. Eğer bizi bağışlamaz ve bize merhamet etmezsen mutlaka ziyana uğrayanlardan oluruz.",
"Hata ve günah sonrası pişmanlıkla okunur.",
"A'râf suresi, 23. ayet (Hz. Âdem ve Hz. Havvâ'nın duası)"))
K.append(d("Sabır ve Müslüman Ölüm Duası (A'râf 126)",
"Rabbenâ efrığ aleynâ sabran ve teveffenâ müslimîn.",
"Ey Rabbimiz, üzerimize sabır yağdır ve bizi Müslüman olarak vefat ettir.",
"Baskı ve zorlukla karşılaşıldığında, imanla ölmek için okunur.",
"A'râf suresi, 126. ayet (Firavun'un sihirbazlarının duası)"))
K.append(d("Tevekkül Duası (Yûnus 85-86)",
"Alallâhi tevekkelnâ, Rabbenâ lâ tec'alnâ fitneten lil-kavmiz-zâlimîn. Ve neccinâ bi-rahmetike minel-kavmil-kâfirîn.",
"Allah'a dayandık. Ey Rabbimiz, bizi zalimler topluluğu için bir imtihan konusu yapma. Rahmetinle bizi kâfirler topluluğundan kurtar.",
"Haksızlık ve baskı altında Allah'a güvenerek okunur.",
"Yûnus suresi, 85-86. ayetler (Hz. Mûsâ'nın kavminin duası)"))
K.append(d("Bilmediğin Şeyi İstememek (Hûd 47)",
"Rabbi innî eûzu bike en es'eleke mâ leyse lî bihî ilm, ve illâ tağfir lî ve terhamnî ekün minel-hâsirîn.",
"Rabbim, hakkında bilgim olmayan bir şeyi senden istemekten sana sığınırım. Beni bağışlamaz ve bana merhamet etmezsen ziyana uğrayanlardan olurum.",
"Bir şeyi isterken sonucunu bilmediğini hatırlayıp Allah'a bırakmak için okunur.",
"Hûd suresi, 47. ayet (Hz. Nûh'un duası)"))
K.append(d("Namaz ve Evlat Duası (İbrâhîm 40-41)",
"Rabbic'alnî mukîmas-salâti ve min zürriyyetî, Rabbenâ ve tekabbel duâ. Rabbenâğfir lî ve li-vâlideyye ve lil-mü'minîne yevme yekûmul-hısâb.",
"Rabbim, beni namazı dosdoğru kılanlardan eyle, soyumdan da böyle kimseler çıkar. Ey Rabbimiz, duamı kabul buyur. Ey Rabbimiz, hesabın görüleceği gün beni, anne babamı ve müminleri bağışla.",
"Namazda devamlılık ve çocukların hayırlı olması için okunur.",
"İbrâhîm suresi, 40-41. ayetler (Hz. İbrahim'in duası)"))
K.append(d("Anne Baba İçin Dua (İsrâ 24)",
"Rabbirhamhümâ kemâ rabbeyânî sagîrâ.",
"Rabbim, küçükken onlar beni nasıl yetiştirdilerse sen de onlara öyle merhamet et.",
"Anne babanın hayatta ya da vefat etmiş olması fark etmeksizin, onlar için her zaman okunur.",
"İsrâ suresi, 24. ayet"))
K.append(d("Doğru Giriş ve Çıkış Duası (İsrâ 80)",
"Rabbi edhılnî mudhale sıdkın ve ahricnî muhrace sıdkın vec'al lî min ledünke sultânen nasîrâ.",
"Rabbim, beni girdiğim yere doğrulukla sok, çıktığım yerden doğrulukla çıkar ve katından bana yardımcı bir güç ver.",
"Yeni bir işe, göreve ya da yere girerken okunur.",
"İsrâ suresi, 80. ayet"))
K.append(d("Göğüs Genişliği ve Kolaylık (Tâhâ 25-28)",
"Rabbişrah lî sadrî, ve yessir lî emrî, vahlül ukdeten min lisânî, yefkahû kavlî.",
"Rabbim, göğsümü aç, işimi kolaylaştır, dilimdeki düğümü çöz ki sözümü anlasınlar.",
"Konuşma, ders anlatma ya da zor bir göreve başlamadan önce okunur.",
"Tâhâ suresi, 25-28. ayetler (Hz. Mûsâ'nın duası)"))
K.append(d("İlim Artırma Duası (Tâhâ 114)",
"Rabbi zidnî ilmâ.",
"Rabbim, ilmimi artır.",
"Ders çalışmadan ve bir şey öğrenmeden önce okunur.",
"Tâhâ suresi, 114. ayet"))
K.append(d("Hastalık ve Dert Duası (Enbiyâ 83)",
"Innî messeniyed-durru ve ente erhamür-râhimîn.",
"Başıma bu dert geldi; sen merhametlilerin en merhametlisisin.",
"Hastalıkta ve sıkıntıda Allah'a sığınırken okunur.",
"Enbiyâ suresi, 83. ayet (Hz. Eyyûb'un duası)"))
K.append(d("Yûnus Duası (Enbiyâ 87)",
"Lâ ilâhe illâ ente sübhâneke innî küntü minez-zâlimîn.",
"Senden başka ilah yoktur. Seni eksikliklerden uzak tutarım. Ben kendime zulmedenlerden oldum.",
"Sıkıntıda ve dar bir durumda okunur.",
"Enbiyâ suresi, 87. ayet; Tirmizî, Daavât 82 (Peygamberimiz bu duanın kabul edildiğini bildirmiştir)"))
K.append(d("Tek Başına Kalmamak İçin (Enbiyâ 89)",
"Rabbi lâ tezernî ferden ve ente hayrul-vârisîn.",
"Rabbim, beni tek başıma bırakma. Sen varislerin en hayırlısısın.",
"Evlat ve destek isteyenler tarafından okunur.",
"Enbiyâ suresi, 89. ayet (Hz. Zekeriyyâ'nın duası)"))
K.append(d("Şeytanın Vesvesesinden Korunma (Mü'minûn 97-98)",
"Rabbi eûzu bike min hemezâtiş-şeyâtîn. Ve eûzu bike Rabbi en yahdurûn.",
"Rabbim, şeytanların kışkırtmalarından sana sığınırım. Rabbim, yanımda bulunmalarından da sana sığınırım.",
"Öfke, vesvese ve kötü düşünce anında okunur.",
"Mü'minûn suresi, 97-98. ayetler"))
K.append(d("Bağışlanma ve Merhamet (Mü'minûn 118)",
"Rabbiğfir verham ve ente hayrur-râhimîn.",
"Rabbim, bağışla ve merhamet et. Sen merhametlilerin en hayırlısısın.",
"Kısa ve her zaman okunabilen bir istiğfar duasıdır.",
"Mü'minûn suresi, 118. ayet"))
K.append(d("Cehennem Azabından Korunma (Furkân 65)",
"Rabbenasrif annâ azâbe cehenneme, inne azâbehâ kâne ğarâmâ.",
"Ey Rabbimiz, cehennem azabını bizden uzaklaştır. Çünkü onun azabı yakasını bırakmayan bir musibettir.",
"Ahirete dair korku ve tövbe duygusuyla okunur.",
"Furkân suresi, 65. ayet (Rahmân'ın kullarının sıfatları arasında)"))
K.append(d("Aile İçin Dua (Furkân 74)",
"Rabbenâ heb lenâ min ezvâcinâ ve zürriyyâtinâ kurrate a'yünin vec'alnâ lil-müttakîne imâmâ.",
"Ey Rabbimiz, eşlerimizi ve çocuklarımızı bize göz aydınlığı kıl ve bizi takva sahiplerine önder yap.",
"Eş ve çocuklar için hayır dilerken okunur.",
"Furkân suresi, 74. ayet"))
K.append(d("Şükür Duası (Neml 19)",
"Rabbi evzi'nî en eşkure ni'metekelletî en'amte aleyye ve alâ vâlideyye ve en a'mele sâlihan terdâhü ve edhılnî bi-rahmetike fî ibâdikes-sâlihîn.",
"Rabbim, bana ve anne babama verdiğin nimete şükretmemi, senin razı olacağın salih amel işlememi bana ilham et ve beni rahmetinle salih kulların arasına kat.",
"Bir nimete kavuşunca okunur.",
"Neml suresi, 19. ayet (Hz. Süleyman'ın duası)"))
K.append(d("Pişmanlık Duası (Kasas 16)",
"Rabbi innî zalemtü nefsî fağfir lî.",
"Rabbim, ben kendime zulmettim, beni bağışla.",
"Yapılan bir hatanın ardından hemen okunur.",
"Kasas suresi, 16. ayet (Hz. Mûsâ'nın duası)"))
K.append(d("İhtiyaç Duası (Kasas 24)",
"Rabbi innî limâ enzelte ileyye min hayrin fakîr.",
"Rabbim, bana indireceğin her hayra muhtacım.",
"Rızık ve iş ararken, Allah'tan hayır isterken okunur.",
"Kasas suresi, 24. ayet (Hz. Mûsâ'nın Medyen'de yaptığı dua)"))
K.append(d("Kırk Yaşı ve Salih Nesil Duası (Ahkâf 15)",
"Rabbi evzi'nî en eşkure ni'metekelletî en'amte aleyye ve alâ vâlideyye ve en a'mele sâlihan terdâhü ve aslıh lî fî zürriyyetî, innî tübtü ileyke ve innî minel-müslimîn.",
"Rabbim, bana ve anne babama verdiğin nimete şükretmemi, razı olacağın salih amel işlememi bana ilham et. Soyumu benim için salih kıl. Ben sana tövbe ettim ve ben Müslümanlardan oldum.",
"Olgunluk çağında şükür ve tövbe için, çocukların salih olması niyetiyle okunur.",
"Ahkâf suresi, 15. ayet"))
K.append(d("Müminlere Dua (Haşr 10)",
"Rabbenağfir lenâ ve li-ihvâninellezîne sebekûnâ bil-îmân ve lâ tec'al fî kulûbinâ gıllen lillezîne âmenû, Rabbenâ inneke raûfür-rahîm.",
"Ey Rabbimiz, bizi ve bizden önce iman etmiş kardeşlerimizi bağışla. Kalplerimizde müminlere karşı kin bırakma. Ey Rabbimiz, şüphesiz sen çok şefkatlisin, çok merhametlisin.",
"Geçmiş müminler ve Müslüman kardeşler için dua ederken okunur.",
"Haşr suresi, 10. ayet"))
K.append(d("Nurun Tamamlanması Duası (Tahrîm 8)",
"Rabbenâ etmim lenâ nûrenâ vağfir lenâ, inneke alâ külli şey'in kadîr.",
"Ey Rabbimiz, nurumuzu tamamla ve bizi bağışla. Şüphesiz sen her şeye gücü yetersin.",
"Samimi tövbe ardından ahirette kurtuluş için okunur.",
"Tahrîm suresi, 8. ayet"))

P = []
P.append(d("Seyyidü'l-İstiğfâr",
"Allâhümme ente Rabbî lâ ilâhe illâ ente, halaktenî ve ene abdüke ve ene alâ ahdike ve va'dike mesteta'tü, eûzü bike min şerri mâ sana'tü, ebûü leke bi-ni'metike aleyye ve ebûü bi-zenbî fağfir lî fe-innehû lâ yağfirüz-zünûbe illâ ente.",
"Allah'ım, sen benim Rabbimsin. Senden başka ilah yoktur. Beni sen yarattın, ben senin kulunum. Gücüm yettiğince sana verdiğim söz ve ahid üzerindeyim. Yaptıklarımın şerrinden sana sığınırım. Bana verdiğin nimeti de kabul ederim, günahımı da kabul ederim. Beni bağışla; günahları ancak sen bağışlarsın.",
"Sabah ve akşam, inanarak okunur.",
"Buhârî, Daavât 2 (Peygamberimiz, bunu sabah inanarak okuyup o gün ölen kimsenin cennetlik olduğunu bildirmiştir)"))
P.append(d("Sabah ve Akşam Koruma Duası",
"Bismillâhillezî lâ yedurru me'asmihî şey'ün fîl-ardı ve lâ fîs-semâi ve hüves-semîul-alîm.",
"Adı anıldığında yerde ve gökte hiçbir şeyin zarar veremediği Allah'ın adıyla. O işitir, bilir.",
"Sabah ve akşam üç kez okunur.",
"Ebû Dâvûd, Edeb 110; Tirmizî, Daavât 13"))
P.append(d("Allah'ın Eksiksiz Kelimelerine Sığınma",
"Eûzü bi-kelimâtillâhit-tâmmâti min şerri mâ halak.",
"Yarattığı şeylerin şerrinden Allah'ın eksiksiz kelimelerine sığınırım.",
"Akşam olunca, bir yere inip konaklayınca ve korku anında okunur.",
"Müslim, Zikir 54-55"))
P.append(d("Sabah ve Akşam Rıza Duası",
"Radîtü billâhi Rabben ve bil-İslâmi dînen ve bi-Muhammedin nebiyyâ.",
"Rab olarak Allah'tan, din olarak İslam'dan, peygamber olarak Muhammed'den razı oldum.",
"Sabah ve akşam üç kez okunur.",
"Ebû Dâvûd, Edeb 110; Tirmizî, Daavât 14 (Peygamberimiz, bunu okuyanı Allah'ın razı edeceğini bildirmiştir)"))
P.append(d("Sabaha Çıkarken",
"Allâhümme bike esbahnâ ve bike emseynâ ve bike nahyâ ve bike nemûtü ve ileyken-nüşûr.",
"Allah'ım, seninle sabaha çıktık, seninle akşama ulaştık, seninle yaşarız, seninle ölürüz ve dönüş sanadır.",
"Sabahleyin okunur (akşam için 'esbahnâ' yerine 'emseynâ' denir).",
"Tirmizî, Daavât 14; Ebû Dâvûd, Edeb 110"))
P.append(d("Uykudan Önce",
"Bismike Allâhümme emûtü ve ahyâ.",
"Allah'ım, senin adınla ölür ve dirilirim.",
"Yatağa girip uyumadan önce okunur.",
"Buhârî, Daavât 7"))
P.append(d("Uykudan Uyanınca",
"El-hamdü lillâhillezî ahyânâ ba'de mâ emâtenâ ve ileyhin-nüşûr.",
"Bizi öldürdükten sonra dirilten Allah'a hamd olsun. Dönüş yalnız onadır.",
"Sabah uykudan kalkınca okunur.",
"Buhârî, Daavât 8"))
P.append(d("Yatmadan Önce Âyetü'l-Kürsî",
"Allâhü lâ ilâhe illâ hüvel-hayyül-kayyûm. Lâ te'huzühû sinetün ve lâ nevm. Lehû mâ fîs-semâvâti ve mâ fîl-ard. Men zellezî yeşfeu indehû illâ bi-iznih. Ya'lemü mâ beyne eydîhim ve mâ halfehüm, ve lâ yühîtûne bi-şey'in min ilmihî illâ bimâ şâ'. Vesia kürsiyyühüs-semâvâti vel-ard. Ve lâ yeûdühû hıfzuhümâ ve hüvel-aliyyül-azîm.",
"Allah, kendisinden başka ilah olmayandır. O diridir, her şeyi ayakta tutandır. Onu ne uyuklama tutar ne de uyku. Göklerdeki her şey, yerdeki her şey onundur. Onun izni olmadan katında şefaat edebilecek kimse yoktur. Onların önlerindeki ve arkalarındaki her şeyi bilir. Onlar, dilediği kadarı dışında ilminden hiçbir şeyi kavrayamazlar. Kürsüsü gökleri ve yeri kuşatmıştır. Onları korumak ona ağır gelmez. O çok yücedir, çok büyüktür.",
"Her gece yatmadan önce okunur.",
"Bakara suresi, 255. ayet; Buhârî, Vekâlet 10 (Peygamberimiz, yatarken okuyana sabaha kadar Allah'tan bir koruyucunun bulunacağını bildirmiştir)"))
P.append(d("Yatarken İhlâs, Felak ve Nâs",
"Kul hüvallâhü ehad. Allâhüs-samed. Lem yelid ve lem yûled. Ve lem yekün lehû küfüven ehad.\n\nKul eûzü bi-rabbil-felak. Min şerri mâ halak. Ve min şerri gâsikın izâ vekab. Ve min şerrin-neffâsâti fîl-ukad. Ve min şerri hâsidin izâ hased.\n\nKul eûzü bi-rabbin-nâs. Melikin-nâs. İlâhin-nâs. Min şerril-vesvâsil-hannâs. Ellezî yüvesvisü fî sudûrin-nâs. Minel-cinneti ven-nâs.",
"De ki: O, Allah'tır, tektir. Allah sameddir (her şey ona muhtaçtır, o hiçbir şeye muhtaç değildir). Doğurmamıştır, doğmamıştır. Hiçbir şey ona denk değildir.\n\nDe ki: Yarattığı şeylerin şerrinden, karanlığı çöktüğü zaman gecenin şerrinden, düğümlere üfleyenlerin şerrinden ve haset ettiği zaman hasetçinin şerrinden sabahın Rabbine sığınırım.\n\nDe ki: İnsanların Rabbine, insanların hükümdarına, insanların ilahına sığınırım. Sinsi vesvesecinin şerrinden; o, insanların göğüslerine vesvese verir; cinlerden de olur, insanlardan da.",
"Her gece yatağa girerken, avuçlara okunup üflenerek ve beden silinerek okunur.",
"Buhârî, Fezâilü'l-Kur'ân 14; İhlâs, Felak ve Nâs sureleri"))
P.append(d("Sıkıntı Anında Kerb Duası",
"Lâ ilâhe illallâhül-azîmül-halîm. Lâ ilâhe illallâhü Rabbül-arşil-azîm. Lâ ilâhe illallâhü Rabbüs-semâvâti ve Rabbül-ardı ve Rabbül-arşil-kerîm.",
"Yüce ve yumuşak huylu Allah'tan başka ilah yoktur. Büyük arşın Rabbi Allah'tan başka ilah yoktur. Göklerin Rabbi, yerin Rabbi ve değerli arşın Rabbi Allah'tan başka ilah yoktur.",
"Üzüntü ve sıkıntı anında okunur.",
"Buhârî, Daavât 26; Müslim, Zikir 83"))
P.append(d("Rahmetini Umarım Duası",
"Allâhümme rahmetike ercû, felâ tekilnî ilâ nefsî tarfete aynin ve aslıh lî şe'nî küllehû, lâ ilâhe illâ ente.",
"Allah'ım, rahmetini umuyorum. Beni göz açıp kapayıncaya kadar bile nefsime bırakma. Bütün işimi düzelt. Senden başka ilah yoktur.",
"Üzüntü ve zorluk anlarında, sabah ve akşam okunur.",
"Ebû Dâvûd, Edeb 101"))
P.append(d("Üzüntü ve Borçtan Sığınma",
"Allâhümme innî eûzü bike minel-hemmi vel-hazen, vel-aczi vel-keseli, vel-buhli vel-cübni, ve dalaid-deyni ve gaelebetir-ricâl.",
"Allah'ım, üzüntüden, kederden, acizlikten, tembellikten, cimrilikten, korkaklıktan, borç yükünden ve insanların baskısından sana sığınırım.",
"Moral bozukluğu, borç ve iş yükü altında okunur.",
"Buhârî, Daavât 36"))
P.append(d("Kalbi Sabit Tutma Duası",
"Yâ mukallibel-kulûb, sebbit kalbî alâ dînik.",
"Ey kalpleri çeviren Allah'ım, kalbimi dinin üzerinde sabit tut.",
"Peygamberimizin çokça yaptığı bir duadır; her zaman okunabilir.",
"Tirmizî, Kader 7; Daavât 89"))
P.append(d("Afiyet Duası",
"Allâhümme innî es'elükel-âfiyete fîd-dünyâ vel-âhireh.",
"Allah'ım, senden dünyada ve ahirette afiyet isterim.",
"Sabah ve akşam ve her zaman okunabilir.",
"Ebû Dâvûd, Edeb 110; İbn Mâce, Dua 4"))
P.append(d("Zikir, Şükür ve İbadet İçin Yardım",
"Allâhümme a'innî alâ zikrike ve şükrike ve hüsni ibâdetik.",
"Allah'ım, seni anmak, sana şükretmek ve sana güzel ibadet etmek için bana yardım et.",
"Her namazın sonunda okunması tavsiye edilmiştir.",
"Ebû Dâvûd, Salât 359; Nesâî, Sehv 60"))
P.append(d("Yolculuk Duası",
"Allâhü ekber, Allâhü ekber, Allâhü ekber. Sübhânellezî sehhara lenâ hâzâ ve mâ künnâ lehû mukrinîn. Ve innâ ilâ Rabbinâ le-münkalibûn. Allâhümme innâ nes'elüke fî seferinâ hâzâl-birre vet-takvâ ve minel-ameli mâ terdâ. Allâhümme hevvin aleynâ seferenâ hâzâ vatvi annâ bu'dehû. Allâhümme entes-sâhibü fîs-seferi vel-halîfetü fîl-ehl. Allâhümme innî eûzü bike min va'sâis-sefer ve ke'âbetil-manzar ve sûil-munkalebi fîl-mâli vel-ehl.",
"Allah en büyüktür (üç kez). Bunu bizim hizmetimize veren Allah'ı tenzih ederiz; yoksa biz buna güç yetiremezdik. Biz elbette Rabbimize döneceğiz. Allah'ım, bu yolculuğumuzda senden iyilik, takva ve razı olacağın amel isteriz. Allah'ım, bu yolculuğu bize kolaylaştır, uzaklığını bize yakın kıl. Allah'ım, yolculukta yoldaş, geride kalan ailemde vekil sensin. Allah'ım, yolculuğun zorluğundan, üzücü bir manzaradan, mal ve ailenin başına kötü bir şey gelmesinden sana sığınırım.",
"Taşıta binip yola çıkarken okunur.",
"Müslim, Hac 425; ayrıca Zuhruf suresi, 13-14. ayetler"))
P.append(d("Hastayı Ziyaret Duası",
"Lâ be's, tahûrun inşâallâh.\n\nEs'elullâhel-azîme Rabbel-arşil-azîmi en yeşfiyek.",
"Zararı yok, inşallah günahlarına kefaret olur.\n\nBüyük Allah'tan, büyük arşın Rabbinden sana şifa vermesini dilerim (yedi kez).",
"Hastayı ziyaret edince hastanın başında okunur.",
"Buhârî, Merdâ 10; Ebû Dâvûd, Cenâiz 7; Tirmizî, Tıb 32"))
P.append(d("Kabir Ziyareti Duası",
"Es-selâmü aleyküm ehled-diyâri minel-mü'minîne vel-müslimîn, ve yerhamullâhül-müstakdimîne minnâ vel-müste'hırîn, ve innâ inşâallâhü bikum lelâhikûn.",
"Ey bu yurdun mümin ve Müslüman halkı, selam sizin üzerinize olsun. Allah, bizden önce gidenlere de, geride kalanlara da rahmet etsin. Biz de inşallah size kavuşacağız.",
"Kabirleri ziyaret ederken okunur.",
"Müslim, Cenâiz 102-104"))

G = []
G.append(d("Yemeğe Başlarken",
"Bismillâh. Başlarken unutursan: Bismillâhi evvelehû ve âhırah.",
"Allah'ın adıyla. Unutursan: Başında da sonunda da Allah'ın adıyla.",
"Yemeğe başlarken okunur.",
"Buhârî, Et'ime 2; Ebû Dâvûd, Et'ime 15; Tirmizî, Et'ime 47"))
G.append(d("Yemekten Sonra",
"El-hamdü lillâhillezî et'amenâ ve sekânâ ve cealenâ müslimîn.",
"Bizi yediren, içiren ve bizi Müslüman kılan Allah'a hamd olsun.",
"Yemek ve içmeyi bitirince okunur.",
"Ebû Dâvûd, Et'ime 54; Tirmizî, Daavât 56"))
G.append(d("Yemeğe Davet Edene Dua",
"Allâhümme bârik lehüm fîmâ razaktehüm, vağfir lehüm verhamhüm.",
"Allah'ım, onlara verdiğin rızkı bereketli kıl, onları bağışla ve onlara merhamet et.",
"Bir evde yemek yedikten sonra ev sahibine dua ederken okunur.",
"Müslim, Eşribe 143"))
G.append(d("Abdestten Sonra",
"Eşhedü en lâ ilâhe illallâhü vahdehû lâ şerîke leh, ve eşhedü enne Muhammeden abdühû ve resûlüh.",
"Şahitlik ederim ki Allah'tan başka ilah yoktur, o tektir, ortağı yoktur. Yine şahitlik ederim ki Muhammed onun kulu ve elçisidir.",
"Abdest alıp bitirdikten sonra okunur.",
"Müslim, Tahâret 17"))
G.append(d("Tuvalete Girerken ve Çıkarken",
"Girerken: Bismillâh. Allâhümme innî eûzü bike minel-hubüsi vel-habâis.\n\nÇıkarken: Gufrâneke.",
"Girerken: Allah'ın adıyla. Allah'ım, erkek ve dişi şeytanlardan sana sığınırım.\n\nÇıkarken: Senden bağışlanma dilerim.",
"Tuvalete girerken ve çıkarken okunur.",
"Buhârî, Vudû 9; Ebû Dâvûd, Tahâret 17; Tirmizî, Tahâret 5"))
G.append(d("Ezandan Sonra",
"Allâhümme Rabbe hâzihid-da'vetit-tâmmeti ves-salâtil-kâimeh, âti Muhammedenil-vesîlete vel-fadîleh, veb'ashü makâmen mahmûdenillezî veadtehû.",
"Allah'ım, bu eksiksiz çağrının ve kılınmakta olan namazın sahibi. Muhammed'e vesîleyi ve fazileti ver ve onu vadettiğin makama (makâm-ı mahmûd) ulaştır.",
"Ezanı dinledikten sonra okunur.",
"Buhârî, Ezân 8"))
G.append(d("Mescide Girerken ve Çıkarken",
"Girerken: Allâhümmeftah lî ebvâbe rahmetik.\n\nÇıkarken: Allâhümme innî es'elüke min fadlik.",
"Girerken: Allah'ım, rahmetinin kapılarını bana aç.\n\nÇıkarken: Allah'ım, senden lütfunu isterim.",
"Mescide girerken sağ ayakla, çıkarken sol ayakla okunur.",
"Müslim, Müsâfirîn 68"))
G.append(d("Evden Çıkarken",
"Bismillâhi tevekkeltü alallâhi lâ havle ve lâ kuvvete illâ billâh.",
"Allah'ın adıyla. Allah'a dayandım. Güç ve kuvvet ancak Allah'tandır.",
"Evden dışarı çıkarken okunur.",
"Ebû Dâvûd, Edeb 103; Tirmizî, Daavât 34"))
G.append(d("Eve Girerken",
"Bismillâh. Ardından ev halkına selam verilir: Es-selâmü aleyküm.",
"Allah'ın adıyla. Selam sizin üzerinize olsun.",
"Eve girerken okunur ve ev halkına selam verilir.",
"Müslim, Eşribe 103; Nûr suresi, 61. ayet"))
G.append(d("Aksırınca ve Aksıranı Duyunca",
"Aksıran: El-hamdü lillâh.\nDuyan: Yerhamükallâh.\nAksıran: Yehdîkümullâhü ve yuslihu bâlekum.",
"Aksıran: Allah'a hamd olsun.\nDuyan: Allah sana merhamet etsin.\nAksıran: Allah size hidayet versin ve halinizi düzeltsin.",
"Aksırdıktan sonra ve aksıran birini duyunca okunur.",
"Buhârî, Edeb 126"))
G.append(d("Yağmur Yağarken",
"Allâhümme sayyiben nâfi'â.",
"Allah'ım, faydalı bir yağmur yağdır.",
"Yağmur yağarken okunur.",
"Buhârî, İstiskâ 22"))
G.append(d("Borçtan Kurtulma Duası",
"Allâhümmekfinî bi-halâlike an harâmik, ve ağninî bi-fadlike amman sivâk.",
"Allah'ım, helalinle beni haramdan uzak tut ve lütfunla beni senden başkasına muhtaç etme.",
"Borç ve geçim sıkıntısında okunur.",
"Tirmizî, Daavât 111"))
G.append(d("Evlenenlere Dua",
"Bârakallâhü leke ve bâreke aleyke ve cemea beynekümâ fî hayr.",
"Allah sana bereket versin, üzerine bereket yağdırsın ve ikinizi hayır üzerinde bir araya getirsin.",
"Evlenen çifti tebrik ederken söylenir.",
"Ebû Dâvûd, Nikâh 36; Tirmizî, Nikâh 7"))
G.append(d("Selam Verme",
"Es-selâmü aleyküm ve rahmetullâhi ve berekâtüh.",
"Selam, Allah'ın rahmeti ve bereketi üzerinize olsun.",
"Bir Müslümanla karşılaşınca veya yanından ayrılırken söylenir.",
"Ebû Dâvûd, Edeb 142; Tirmizî, İsti'zân 3"))
G.append(d("İstihare Duası",
"Allâhümme innî estehîruke bi-ilmike ve estakdiruke bi-kudretike ve es'elüke min fadlikel-azîm. Fe-inneke takdirü ve lâ akdir, ve ta'lemü ve lâ a'lem, ve ente allâmül-guyûb. Allâhümme in künte ta'lemü enne hâzel-emre hayrun lî fî dînî ve meâşî ve âkıbeti emrî, fakdurhü lî ve yessirhü lî, sümme bârik lî fîh. Ve in künte ta'lemü enne hâzel-emre şerrun lî fî dînî ve meâşî ve âkıbeti emrî, fasrifhü annî vasrifnî anhü, vakdur liyel-hayra haysü kâne, sümme erdınî bih.",
"Allah'ım, ilminle senden hayır dilerim, kudretinle güç isterim ve büyük lütfundan isterim. Sen güç yetirirsin, ben yetiremem. Sen bilirsin, ben bilmem. Sen gaybları bilensin. Allah'ım, bu işin dinim, geçimim ve işimin sonu için hayırlı olduğunu biliyorsan, onu bana nasip et, kolaylaştır, sonra onda bana bereket ver. Eğer bu işin dinim, geçimim ve işimin sonu için kötü olduğunu biliyorsan, onu benden uzaklaştır, beni de ondan uzaklaştır. Hayır neredeyse onu bana nasip et, sonra beni ondan razı kıl.",
"Önemli bir karar vermeden önce iki rekât istihare namazından sonra okunur.",
"Buhârî, Teheccüd 28; Daavât 48"))

book = {
 "id": "kuran_sunnet_dualari_book",
 "baslik": "Kur'an ve Sünnet'ten Dualar",
 "yazar": "Vera Kütüphane",
 "renk": ["#6D28D9", "#4C1D95"],
 "ciltler": [
  {"ad": "Kur'an'daki Dualar", "sayfalar": K},
  {"ad": "Peygamberimizin Duaları", "sayfalar": P},
  {"ad": "Günlük Hayat", "sayfalar": G},
 ]
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(book, f, ensure_ascii=False, indent=2)
b = json.load(open(OUT, encoding="utf-8"))
print([len(c["sayfalar"]) for c in b["ciltler"]], sum(len(c["sayfalar"]) for c in b["ciltler"]))
