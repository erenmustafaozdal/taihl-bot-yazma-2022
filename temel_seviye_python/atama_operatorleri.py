"""
ATAMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlere veri ataması yaparken kullanırız.
+----------+-----------+----------------+
| Operatör | Kullanımı | Uzun Kullanımı |
+----------+-----------+----------------+
| =        | x = y     |                |
+----------+-----------+----------------+
| +=       | x += y    | x = x + y      |
+----------+-----------+----------------+
| -=       | x -= y    | x = x - y      |
+----------+-----------+----------------+
| *=       | x *= y    | x = x * y      |
+----------+-----------+----------------+
| /=       | x /= y    | x = x / y      |
+----------+-----------+----------------+
| %=       | x %= y    | x = x % y      |
+----------+-----------+----------------+
| **=      | x **= y   | x = x ** y     |
+----------+-----------+----------------+
| //=      | x //= y   | x = x // y     |
+----------+-----------+----------------+
"""

# sayısal verilere sahip 3 değişken oluşturalım
a = 2
b = 3
c = 4

# üç değişkeni tek satırda tanımlayalım
x, y, z = 5, 6, 7
print(x, y, z)

# değişkendeki verileri yer değiştirelim
x, y, z = y, z, x
print(x, y, z)

# değişken içindeki değere 10 ekleyelim
x = x + 10
y += 10
print(x, y)

# x ve y değişkenlerinde değeri 5 azaltalım (x: uzun yol, y: kısa yol)
x = x - 5
y -= 5
print(x, y)
