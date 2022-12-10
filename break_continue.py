"""
break: döngüyü sonlandırır
continue: döngünün ilgili turunu sonlandırır
"""

# 0'dan 10'a kadar olan sayıları 5 hariç ekrana yazdıralım
for sayi in range(10):
    if sayi == 5:
        continue

    print(sayi)

# 0'dan 10'a kadar sayıları ekrana yazdıralım.
# Ancak 5'e gelince döngüden çıkalım.
for sayi in range(10):
    if sayi == 5:
        break

    print(sayi)

# 1'den 100'e kadar olan tek sayıları ekrana yazdırın
for sayi in range(1, 100):
    # 1. yöntem
    if sayi % 2 == 0:
        continue

    print(sayi)

    # 2. yöntem
    # if sayi % 2 == 0:
    #     pass
    # else:
    #     print(sayi)
