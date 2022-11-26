"""
DİĞER OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
+----------+------------------+-----------+
| Operatör | Açıklama         | Kullanımı |
+----------+------------------+-----------+
| is       | kimlik operatörü | x is y    |
+----------+------------------+-----------+
| in       | üyelik operatörü | "a" in x  |
+----------+------------------+-----------+
"""

# tek liste ile 2 farklı değişken ve ayrı bir liste ile 3. değişken oluşturalım
a = b = [1, 2, 3]
c = [1, 2, 3]

# değişkenlerin değer eşitliğini (==) ve kimlik eşitliğini (is) kontrol edelim
print(a == b)
print(a == c)
print(a is b)
print(a is c)

# bir eleman listenin içindeki bir eleman mıdır kontrol edelim
print(3 in a)
print(4 in a)
