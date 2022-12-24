"""
VALUE VERİ TİPİ (VALUE TYPES)
//////////////////////////////////////////////////////////////////////////////
✔ Verileri kendine ayrılmış bir bellekte tutar.
✔ Değişken doğrudan bir değeri tutar.
✔ Başka bir değişkene atarsanız, değer doğrudan kopyalanır.
    ⚫ İki değişken de bağımsız çalışır.
ÖR: string, int, float

REFERANS VERİ TİPİ (REFERENCE TYPES)
//////////////////////////////////////////////////////////////////////////////
✔ Gerçek verilerin bellekteki konumunu tutar.
✔ Verinin kendisini değil, adresini temsil eder.
✔ Başka bir değişkene atarsanız, veriler kopyalanmaz.
    ⚫ Orijinal verinin adresini başka değişkene atamış olursunuz.
ÖR: list, dict
"""

# VALUE TİPİ
###########################################
# iki value veri tipi oluşturalım
a = 1
b = 2

# ikinci değişkeni ilk değişkene atayalım
a = b

# ikinci değişkenin değerini değiştirelim. birinci değişken değişti mi bakalım.
b = 3
print(a, b)


# REFERANS TİPİ
###########################################
# iki tane referan tipi değişken oluşturalım
x = [1, 2, 3]
y = ["a", "b" ,"c"]

# ikinci değişkeni ilk değişkene atayalım
x = y

# ikinci değişken değişiklik yaptığımızda ilk değişken etkileniyor mu bakalım.
y[0] = "d"
print(x, y)
