# 100-200 arasındaki sayıları "numaralar" değişkenine aktaralım
numaralar = []
for sayi in range(100, 200):
    numaralar.append(sayi)

print(numaralar)

# Yukarıdaki işlemi list comprehensions şeklinde yapalım
numaralar2 = [sayi for sayi in range(100, 200)]
print(numaralar2)

# 100-200 arasındaki çift sayılara bir listeye aktaralım
cift_sayilar = [sayi for sayi in range(100, 200) if sayi % 2 == 0]
print(cift_sayilar)

# 100-200 arasındaki tek sayıları "{sayi} TEK", çift sayıları "{sayi} ÇİFT"
# şeklinde listeye aktaralım
numaralar3 = [f"{sayi} TEK" if sayi % 2 == 1 else f"{sayi} ÇİFT" for sayi in range(100, 200)]
print(numaralar3)

# Aşağıdaki işlemi list comprehensions ile yapalım
liste = []
for x in range(3):
    for y in range(3):
        liste.append((x, y))

print(liste)

liste2 = [(x, y) for x in range(3) for y in range(3)]
print(liste2)
