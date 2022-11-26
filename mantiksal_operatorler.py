"""
MANTIKSAL OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
Python'da birden fazla koşulu beraber değerlendirmek için kullanırız.
+----------+----------+-----------------+
| Operatör | Açıklama |    Kullanımı    |
+----------+----------+-----------------+
|    and   | ve       | (x<y) and (a>b) |
+----------+----------+-----------------+
|    or    | veya     |  (x<y) or (a>b) |
+----------+----------+-----------------+
|    not   | değil    |    not (x<y)    |
+----------+----------+-----------------+
"""

# Futbolcuların 5 gol ve 8 asist üzerinde olanları başarılı sayalım
futbolcu1 = {
    "gol": 5,
    "asist": 9
}
futbolcu2 = {
    "gol": 8,
    "asist": 10
}
print(f"1. futbolcu: {(futbolcu1['gol'] > 5 and futbolcu1['asist'] > 8)}")
print(f"2. futbolcu: {(futbolcu2['gol'] > 5 and futbolcu2['asist'] > 8)}")

# Futbolcuların golü 5'ten fazlaysa veya asisti 8'den fazlaysa başarılı sayalım
print(f"1. futbolcu: {(futbolcu1['gol'] > 5 or futbolcu1['asist'] > 8)}")
print(f"2. futbolcu: {(futbolcu2['gol'] > 5 or futbolcu2['asist'] > 8)}")

# Futbolcunun golü 5'ten büyük değilse başarısız olsun
print(f"1. futbolcu: {not(futbolcu1['gol'] > 5)}")
print(f"2. futbolcu: {not(futbolcu2['gol'] > 5)}")
