# Boş bir liste tanımlayalım: []
liste = []
print(liste)
print(type(liste))

okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
kelimeler = okul.split()
print(kelimeler)

# Belirli sıradaki kelimeleri yazdıralım
print(kelimeler[0])  # ilk kelime
print(kelimeler[1])
print(kelimeler[2])
print(kelimeler[3])
print(kelimeler[4])
print(kelimeler[5])
# print(kelimeler[6])  # hata verdi
print(kelimeler[-1])  # son kelime
print(kelimeler[-6])

ad = "Eren Mustafa Özdal"
print(ad[0])  # E
print(ad[5:12])  # Mustafa
print(ad[5:12:2])  # Msaa
print(ad[-7:-14:-1])  # afatsuM
print(ad[::-1])  # ladzÖ afatsuM nerE

# Listeler içerisinde farklı türden veriler olabilir
liste = [1, 12.3, "Python", True, [1, 2, 3]]
print(liste[-1][-1])  # 3
print(liste[4][-1])  # 3
print(liste[4][2])  # 3

# İki listeyi birleştirme
liste2 = [1, 2, 3]
liste3 = [4, 5, 6]
liste4 = liste2 + liste3
liste5 = liste3 + liste2
print(liste4)
print(liste5)
