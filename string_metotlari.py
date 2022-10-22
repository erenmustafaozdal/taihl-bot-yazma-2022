okul = "sancaktepe TEKNOLOJİ anadolu imam HATİP lisesi"

# Tüm karakterleri büyük harf yapalım: upper()
print(okul.upper())

# Tüm karakterleri küçük harf yapalım: lower()
print(okul.lower())

# Her kelimenin ilk harfini büyük yapalım: title()
print(okul.title())

# Karakter dizisinin ilk karakterini büyük,
# diğer karakterlerini küçük harf yapalım: capitalize()
print(okul.capitalize())

# Belirli bir ifadenin kaç defa yer aldığını bulalım: count()
makale = "Teknolojinin hızla geliştiği ve günlük hayatımızın her alanına sirayetettiği bir çağda kalkınma ile teknolojik gelişme arasında doğru orantı kurmakmümkündür. Bu yüzden teknoloji okur-yazarlığı ve teknoloji öğretimi kavramları giderek önem kazanmıştır. Kalkınmış ülkeler eğitim programlarını teknolojiye çabuk uyum sağlayabilen, teknolojiyi verimli kullanabilen ve yeni teknolojiler üretebilen bireyler yetiştirebilmeyi hedefleyecek şekilde geliştirmişlerdir.Bu çalışmada ABD, İngiltere ve Fransa gibi kalkınmış ülkelerde uygulanan eğitim programları içerisinde teknoloji öğretiminin yerinin saptaması veTürkiye’deki mevcut durumla karşılaştırılması amaçlanmıştır. Yapılan karşılaştırmada adı geçen ülkelerin teknoloji öğretimi açısından genel bir bilinç geliştirdikleri ve eğitim sistemlerini de buna göre geliştirdikleri görülmüştür.Türkiye’de ise bu bilinç nispeten geç gelişmiş ve diğer örneklerde olduğu gibisivil kurum ve kuruluşlardan yeterince destek alınamamıştır. Ayrıca teknolojidersleriyle diğer dersler arasındaki yatay kaynaşıklığın yaratılması açısından dafarklılıklar gözlenmiştir"
# Metni önce lower ile küçük harflere çeviriyoruz.
# Ardından ifadenin kaç defa yer aldığını buluyoruz.
# ❗ Büyük - küçük harfe duyarlı
print(makale.lower().count("teknoloji"))

# Soldaki ve sağdaki boşluk karakterlerini temizleyelim: strip()
ad = input("Adınız: ")
print(ad + "|")
print(ad.strip() + "|")

# Soldaki ve sağdaki belirli karakterleri temizleyelim: strip("ifade")
urun_kodu = "HEP20221022HEP"
print(urun_kodu.strip("HEP"))

# Soldaki boşluk veya belirli ifadeyi temizleyelim: lstrip()
print(ad + "|")  # adı boşlukla gönderelim
print(ad.lstrip() + "|")
print(urun_kodu.lstrip("HEP"))

# Sağdaki boşluk veya belirli ifadeyi temizleyelim: rstrip()
print(ad + "|")  # adı boşlukla gönderelim
print(ad.rstrip() + "|")
print(urun_kodu.rstrip("HEP"))

# Karakter dizisini bölelim: split()
print(makale.split("."))
print(okul.split())

# Böldüğümüz ve listeye dönüşen ifadeleri birleştirelim: join()
kelimeler = okul.split()
print(kelimeler)
print("---".join(kelimeler))

# Ortalayıp çıktı verme: center()
print("Eren".center(25, "-"))
