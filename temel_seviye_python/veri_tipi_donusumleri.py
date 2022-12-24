# Kullanıcıdan 2 sayı alıp toplama işlemi yapan program
# sayi1 = input("1. sayıyı yazın: ")
# sayi2 = input("2. sayıyı yazın: ")

# print( type(sayi1) )
# print( type(sayi2) )
# print( float(sayi1) + float(sayi2) )

# Farklı veri tiplerine bakalım: type()
x = 1  # integer
y = 1.2  # float
ad = "Eren"  # string
sinav_basarili_mi = True  # boolean
# print(type(x))
# print(type(y))
# print(type(ad))
# print(type(sinav_basarili_mi))

# TİP DÖNÜŞTÜRME

# int'ten float'a
print(float(x))

# float'tan int'e
print(int(y))

# bool'dan str'ye
print(sinav_basarili_mi)  # bool olarak True
print(str(sinav_basarili_mi))  # str olarak "True"

# bool'dan int'e
print(int(sinav_basarili_mi))

# int'ten str'ye
print(str(x))  # str olarak "1"

# str'den int'e
# print(int(ad))  # metin int'e dönüşmez
sayi = "36"
print(int(sayi))  # sayı değeri taşıyan str dönüşebilir
