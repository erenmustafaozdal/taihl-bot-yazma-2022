liste = [1, 2, 3]
tuple = ("bir", "iki", "üç")

# tuple'ı ekrana yazıralım
# print(liste)
# print(type(liste))
# print(tuple)
# print(type(tuple))

# belirli bir elemanı ekrana yazdıralım
# print(tuple[0])

# listenin ve tupleın bir elemanını değiştirelim
liste[0] = 7
# print(liste)
# 👇 TypeError: 'tuple' object does not support item assignment
# tuple[0] = "yedi"  hata verdi
# print(tuple)

# tuple içindeki belirli bir elemanın indeksini bulalım: index()
# print(tuple.index("iki"))

# 2 tuple'ı birleştirelim
tuple1 = (1, 2, 3)
tuple2 = "bir", "iki", "üç"
print(tuple1 + tuple2)
