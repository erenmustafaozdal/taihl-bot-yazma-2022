url = "https://teknolojiaihl.meb.k12.tr"

# 1- "url" içinde kaç karakter olduğunu yazdır.
print(len(url))

# 2- "url" içindeki "meb" sözcüğünü ekrana yazdırın.
print(f"{url[22]}{url[23]}{url[24]}")

# 3- "url" içindeki "k12" sözcüğünü ekrana yazdırın.
print(url[26]+url[27]+url[28])

# 4- Kullanıcıdan adını, en sevdiği yemeği alın ve cümle içinde yazdırın.
# ÖRNEK CÜMLE: Adınız: Eren. En sevdiğiniz yemek: Pırasa
name = input("isminiz:")
yemek = input("en sevdiğiniz yemek:")
print(f"adınız {name} en sevdiğiniz yemek {yemek}")

# 5- Öğrencinin 2 sınav notunu alın. Notunu hesaplayıp cümle içinde yazdırın.
# 1. sınav oranı: %35
# 2. sınav oranı: %65
# ÖRNEK CÜMLE: 1. sınav: 70 puan, 2. sınav: 90 puan, Notunuz: 83.0
sinav1_yuzde = 0.35
sinav2_yuzde = 0.65
sinav1 = float(input("1. sınav: "))
sinav2 = float(input("2. sınav: "))
print(f"1. sınav: {sinav1} puan, 2. sınav: {sinav2} puan, Notunuz: {(sinav1*sinav1_yuzde)+(sinav2*sinav2_yuzde)}")

# 6- Kullanıcının adını alın ve yan yana 100 defa yazdırın.
isim = input("isminiz:")
print(isim*100)
