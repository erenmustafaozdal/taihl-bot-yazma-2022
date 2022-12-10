# METOT: range()
# range() fonksiyonunu belli bir aralıkta bulunan sayıları
# döndürmek için kullanırız

# 1-10 arasındaki sayılardan oluşan bir liste
liste = list(range(1, 10))
print(liste)

# Ekrana 50 defa Python yazdıralım
# ÖRNEK: 1. Python
for sayi in range(50):
    print(f"{sayi+1}. Python")

# METOT: enumerate()
# İngilizce'de enumerate kelimesi "numaralandırmak" anlamına gelir.
# Fonksiyonun görevi nesne elemanlarını numaralandırarak döndürmek.

# "python" kelimesinin karakterlerini enumerate
# ile numaralanadırıp ekrana yazalım
kelime = "python"
kelime_enum = list(enumerate(kelime))
print(kelime_enum)

for index, harf in enumerate(kelime):
    print(index, harf)

# METOT: zip()
# zip listeleri birleştirme işlemi yapar

# sayılardan ve o sayıların okunuşlarından oluşan 2 liste oluşturalım
sayilar = [1, 2, 3]
okunuslar = ["bir", "iki", "üç"]

# Bu listeleri zip() ile birleştirelim
sayilar_zip = list(zip(sayilar, okunuslar))
print(sayilar_zip)

# for döngüsü içinde sayıları ve okunuşları ekrana yazdıralım
for sayi, okunus in zip(sayilar, okunuslar):
    print(sayi, okunus)
