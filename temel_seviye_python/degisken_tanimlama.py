# Değişkenler olmadan 2 öğrencinin sınav notlarını hesaplayalım
# print( (80*0.4) + (75*0.6) )
# print( (45*0.4) + (60*0.6) )

# Değişkenlerle 2 öğrencinin sınav notlarını hesaplayalım
sinav1_yuzde = 0.4
sinav2_yuzde = 0.6

# print( (80*sinav1_yuzde) + (75*sinav2_yuzde) )
# print( (45*sinav1_yuzde) + (60*sinav2_yuzde) )

# DEĞİŞKEN TANIMLAMA KURALLARI

# Rakam ile başlayamaz
# 1sayi = 85  hata verdi
sayi1 = 85
# print(sayi1)

# Büyük küçük harfe duyarlıdır
number = 12
NUMBER = 15
# print(number)
# print(NUMBER)

# Türkçe karakter kullanılamaz
# yaş = 18 hatalı kullanım
yas = 18  # Türkçe karakter olmadan Türkçe yazmak (tavsiye edilmez)
age = 17
# print(yas)
# print(age)

# DEĞİŞKENLERDEKİ VERİLERİ BİRLEŞTİRME
x = 1  # integer
y = 1.2  # float
ad = "Eren"  # string
sinav_basarili_mi = True  # boolean

print(x+y)
# print(x+ad)  hata verdi
print(x+sinav_basarili_mi)
# print(ad+sinav_basarili_mi)  hata verdi
