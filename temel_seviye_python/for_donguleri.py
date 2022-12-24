"""
Python'da kullanabileceğimiz 2 tane döngü tipinden biri for'dur.
Tekrarlayacak işlemlerimizde döngüleri kullanırız.
"for" döngüsü bir eleman her elemana sırayla ulaşmak için kullanılır.
"""

# öğrenci isimlerinden oluşan bir liste oluşturalım
ogrenciler = ["Eren", "Mustafa", "Zeynep"]

# Her öğrencinin adını ekrana yazdıralım
# ÖRNEK: Öğrencinin adı: Eren
for ogrenci in ogrenciler:
    print(f"Öğrencinin adı: {ogrenci}")

# İçinde ikili sayılardan oluşan tuple verilerinin olduğu bir liste oluşturalım
sayilar = [(1, 2), (3, 4), (5, 6)]
for a, b in sayilar:
    print(f"1.sayı: {a}, 2. sayı: {b}")

# Okulumuzun adının yer aldığı bir değişkeni kelimelere
# bölüp her kelimeyi döngü içinde ekrana yazdıralım.
okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
for kelime in okul.split():
    print(kelime)

# öğrencilerin yer aldığı bir dict veri tipi oluşturalım
ogrenciler = {
    1: {
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": True,
        "dersler": ["Türkçe", "Matematik", "Hayat Bilgisi"]
    },
    45: {
        "ad": "Zeynep",
        "soyad": "Özdal",
        "cinsiyet": False,
        "dersler": ["Görsel Sanatlar", "Matematik", "Fen Bilimleri"]
    }
}

# öğrencilerin numaralarını ve adlarını yazdıralım
for no, ogrenci in ogrenciler.items():
    print(f"{no} numaralı öğrenci: {ogrenci['ad']}")
