"""
KARŞILAŞTIRMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlerin içindeki verileri karşılaştırmak için kullanırız
+----------+----------------+-----------+
| Operatör | Açıklama       | Kullanımı |
+----------+----------------+-----------+
|    ==    | eşit mi?       |   x == y  |
+----------+----------------+-----------+
|    !=    | eşit değil mi? |   x != y  |
+----------+----------------+-----------+
|     >    | büyük mü?      |   x > y   |
+----------+----------------+-----------+
|     <    | küçük mü?      |   x < y   |
+----------+----------------+-----------+
|    >=    | büyük eşit mi? |   x >= y  |
+----------+----------------+-----------+
|    <=    | küçük eşit mi? |   x <= y  |
+----------+----------------+-----------+
"""

# VERİTABANI
kullanici_adi = "eren"
sifre = "1234"

# Kullanıcıdan "kullanıcı adı" ve "şifre" bilgilerini alalım ve veritabanını
# temsil eden değişkenler içindeki veri ile eşitliğini kontrol edelim.
# k_kadi = input("Kullanıcı adınızı yazın: ")
# k_sifre = input("Şifrenizi yazın: ")
# print(f"Kullanıcı adı doğru mu: {kullanici_adi == k_kadi}")
# print(f"Şifre doğru mu: {sifre == k_sifre}")

# Kullanıcıdan 2 sayı alalım. Birbirine "eşit değil mi?" kontrolü yapalım.
# sayi1 = int(input("1. sayı: "))
# sayi2 = int(input("2. sayı: "))
# print(f"Eşit değil mi: {sayi1 != sayi2}")

# iki kişinin yaşını karşılaştıralım (Büyük mü? Küçük mü?)
yas1 = 36
yas2 = 25
print("Büyük mü: " + str(yas1 > yas2))
print("Küçük mü: {}".format(yas1 < yas2))
