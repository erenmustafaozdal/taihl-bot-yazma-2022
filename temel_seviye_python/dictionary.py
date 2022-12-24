"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "Eren"
    "soyad": "Özdal"
"""

# belirli bir numaraya sahip öğrenciyi bulma işlemini liste ile yapalım
# numaralar = [66, 75]
# isimler = ["Ahmet", "Mehmet"]
# numara = int(input("Öğrenci numarası yazınız: "))
# konum = numaralar.index(numara)
# print(isimler[konum])

# belirli bir numaraya sahip öğrenciyi bulma işlemini dictionary ile yapalım
# ogrenciler = {66: "Ahmet", 75: "Mehmet"}
# print(ogrenciler[numara])

# detaylı örnek
kisiler = {
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

# 45 numaralı öğrencinin derslerini yazdıralım
print(kisiler[45]["dersler"])
