# 1- "Türkçe, Hayat Bilgisi, Matematik, Fen Bilimleri" elemanlarından oluşan liste oluşturalım
dersler = ["Türkçe", "Hayat Bilgisi", "Matematik", "Fen Bilimleri"]

# 2- "Hayat Bilgisi" değerini "Sosyal Bilgiler" değeri ile değiştirelim
hb_index = dersler.index("Hayat Bilgisi")
dersler[hb_index] = "Sosyal Bilgiler"
print(dersler)

# 3- "Coğrafya" listenin bir elemanı mıdır?
print("Coğrafya" in dersler)

# 4- Listenin son 2 elemanı yerine "Görsel Sanatlar" ve "Müzik" değerlerini ekleyelim
dersler[-1] = "Görsel Sanatlar"
dersler[-2] = "Müzik"
print(dersler)

# 5- Listenin üzerine "Serbest Etkinlik" ve "Beden Eğitimi ve Oyun" değerlerini ekleyelim
dersler.append("Serbest Etkinlik")
dersler.append("Beden Eğitimi ve Oyun")
print(dersler)

# 6- Listenin son elemanını silelim
dersler.pop()
print(dersler)

# 7- Liste elemanlarını ters çevirelim
dersler.reverse()
print(dersler)

# 8- Liste elemanlarını alfabetik olarak sıralayalım
dersler.sort()
print(dersler)

# 9- 3 öğrenci için öğrenci no anahtarı ile ad, soyad, cinsiyet, yaş bilgilerinden oluşan bir dictionary oluşturalım
ogrenciler = {
    111: {
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": "erkek"
    },
    222: {
        "ad": "Zeynep",
        "soyad": "Özdal",
        "cinsiyet": "kız"
    },
    333: {
        "ad": "Sultan",
        "soyad": "Özdal",
        "cinsiyet": "kız"
    }
}

# 10- Kullanıcıdan öğrenci numarası alarak öğrenci bilgilerini ekrana yazdıralım
# ÖRNEK METİN: 100 nolu öğrencinin adı Eren Özdal ve cinsiyeti erkek
no = int(input("Öğrenci numarası yazın (111,222,333): "))
print(f"{no} nolu öğrencinin adı {ogrenciler[no]['ad']} {ogrenciler[no]['soyad']} ve cinsiyeti {ogrenciler[no]['cinsiyet']}")

# 11- Kullanıcıdan 2 sayı alalım ve bu sayıları "a" ve "b" değişkenlerine atayalım.
a = int(input("1. Sayı: "))
b = int(input("2. Sayı: "))

# 12- "a"nın "b" ile toplamını "a" değişkenine atayıp ekrana yazdıralım.
a += b
print("a += b", a)

# 13- "a"nın "b" ile farkını "a" değişkenine atayıp ekrana yazdıralım.
a -= b
print("a -= b", a)

# 14- "a"nın "b" ile çarpımını "a" değişkenine atayıp ekrana yazdıralım.
a *= b
print("a *= b", a)

# 15- "a"nın "b"ye bölümünü "a" değişkenine atayıp ekrana yazdıralım.
a /= b
print("a /= b", a)

# 16- "a"nın "b"ye bölümünden kalanı "a" değişkenine atayıp ekrana yazdıralım.
a %= b
print("a %= b", a)

# 17- "a"nın "b" üssünü "a" değişkenine atayıp ekrana yazdıralım.
a **= b
print("a **= b", a)

# 18- "a"nın "b"ye kalansız bölümünü "a" değişkenine atayıp ekrana yazdıralım.
a //= b
print("a //= b", a)

# 19- Kullanıcıdan 2 sayı alıp, 1. sayı 2. sayıdan büyük mü ekrana yazdıralım.
# ÖRNEK METİN: 1. sayı, 2. sayıdan büyük mü: True
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
print(f"1. sayı, 2. sayıdan büyük mü: {sayi1 > sayi2}")

# 20- Kullanıcıdan 1. sınav (%40) ve 2. sınav notu (%60) alıp ortalama hesaplayalım.
# Eğer ortalama 45 üzerindeyse "True", değilse "False" yazdıralım.
# ÖRNEK METİN: 1. sınav: 50, 2. sınav: 70, Ortalama: 62. Geçti mi: True
sinav1 = int(input("1. Sınav: "))
sinav2 = int(input("2. Sınav: "))
ortalama = (sinav1*0.4) + (sinav2*0.6)
print(f"1. sınav: {sinav1}, 2. sınav: {sinav2}, Ortalama: {ortalama}. Geçti mi: {ortalama > 45}")

# 21- Kullanıcıdan bir sayı alalım ve bu sayı tekse "True", değilse "False" yazdıralım.
# ÖRNEK METİN: Girilen sayı: 5. Tek mi: True
sayi1 = int(input("Sayı: "))
kalan = sayi1 % 2
print(f"Girilen sayı: {sayi1}. Tek mi: {kalan > 0}")

# 22- Kullanıcıdan bir sayı alalım ve bu sayı pozitifse "True", değilse "False" yazdıralım.
# ÖRNEK METİN: Girilen sayı: -10. Pozitif mi: False
sayi1 = int(input("Sayı: "))
print(f"Girilen sayı: {sayi1}. Pozitif mi: {sayi1 > 0}")

# 23- Kullanıcıdan alınan bir sayının 0-100 arasında olup olmadığını
# "and" operatörü ile bulup ekrana yazdıralım
# ÖRNEK METİN: Sayı: 110. 0-100 arasında mı: False
sayi1 = int(input("Sayı: "))
print(f"Sayı: {sayi1}. 0-100 arasında mı: {sayi1 > 0 and sayi1 < 100}")
