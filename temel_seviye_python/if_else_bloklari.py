"""
if ve else blokları ile mantıksal operatörler kullanılarak
programın akışı değiştirilebilir
"""

# Kullanıcıdan iki sayı alalım.
# Bu sayılardan hangisinin büyük olduğunu ekrana yazalım.
# ÖRNEK: 1. sayı (5), 2. sayıdan (3) büyüktür.
# ÖRNEK: 2. sayı (9), 1. sayıdan (4) büyüktür.
sayi1 = int(input("1. sayıyı yazın: "))
sayi2 = int(input("2. sayıyı yazın: "))

if sayi1 > sayi2:
    print(f"1. sayı ({sayi1}), 2. sayıdan ({sayi2}) büyüktür.")
else:
    print(f"2. sayı ({sayi2}), 1. sayıdan ({sayi1}) büyüktür.")
