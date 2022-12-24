"""
Python'da kullanabileceğimiz 2 tane döngü tipinden diğer "while"dır.
Belirttiğimiz koşul doğru (True) olduğu sürece devam eden döngü tipidir.
"""

# 0'dan 100'e kadar olan tek ve çift sayıları yazdıralım
# ÖRNEK: 1 tek sayıdır
# ÖRNEK: 2 çift sayıdır
# sayi = 0
# while sayi < 100:
#     if sayi % 2 == 0:
#         print(f"{sayi} çift sayıdır.")
#     # elif sayi % 2 == 1:  buna gerek yok
#     else:
#         print(f"{sayi} tek sayıdır.")
#
#     sayi += 1

# WorldCupPlayers Excel dosyasındaki verileri okuyalım.
# Hangi oyuncuların kaçıncı dakikada gol attıklarına bakalım.

# Excel okuma modülünü içeri aktaralım
import xlrd

# Excel dosyasını açalım
ck = xlrd.open_workbook("veriler/WorldCupPlayers.xls")

# Excel çalışma sayfasını alalım
cs = ck.sheet_by_index(0)

# Toplam satır ve sütun sayılarını alalım
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols
print(f"Satır sayısı: {satir_sayisi}")
print(f"Sütun sayısı: {sutun_sayisi}")

# ilk başlık satırını okuyalım
a1 = cs.cell(0, 0)
print(a1)

# tüm futbolcuların isimlerini yazdıralım
satir = 1  # başlıkları es geçmek için 1. indeksten başlıyoruz
while satir < satir_sayisi:
    futbolcu = cs.cell_value(satir, 6)

    # if futbolcu.startswith("R"):  # R harfi ile başlayan futbolcular
    #     print(f"Futbolcu: {futbolcu}")

    # Bir olaya yaşamış futbolcular yazdıralım
    olay = cs.cell_value(satir, 8)
    if olay != "":
        print(f"Futbolcu: {futbolcu} - Olay: {olay}")

    satir += 1
