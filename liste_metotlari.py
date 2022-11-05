sayilar = [9, 12, 85, 3, 16, 34, 42, 99, 165, 15]
harfler = ["t", "c", "a", "e", "z", "m", "h", "g"]

# listelerin eleman sayısını bulalım: len(liste)
# print(len(sayilar))
# print(len(harfler))

# listenin en küçük değerli elemanını bulalım: min()
# print(min(sayilar))
# print(min(harfler))

# listenin en büyük değerli elemanını bulalım: max()
# print(max(sayilar))
# print(max(harfler))

# metin ve sayılardan oluşan listeleri birleştirip en büyüğünü bulalım
birlesmis = sayilar + harfler
# 👇 TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(birlesmis))  hata verdi

# listenin sonuna yeni eleman ekleyelim: append()
sayilar.append(95)
# print(sayilar)

# listenin istediğimiz konumuna yeni eleman ekleyelim: insert()
harfler.insert(3, "b")
# print(harfler)

# listenin sonundaki elemanı silelim: pop()
harfler.pop()
# print(harfler)
harfler.pop(3)  # belirli konumdaki b harfi silinir
# print(harfler)

# listede belirli bir değere sahip elemanları silelim: remove("değer")
harfler.append("a")
# print(harfler)
harfler.remove("a")
# print(harfler)

# listedeki elemanları sıralayalım: sort()
# print(sayilar)
sayilar.sort()  # artan sıralama yapar
# print(sayilar)
sayilar.sort(reverse=True)  # azalan sıralama yapar
# print(sayilar)
# print("-"*50)  # ayıraç
# print(harfler)
harfler.sort()  # artan sıralama yapar
# print(harfler)
harfler.sort(reverse=True)  # azalan sıralama yapar
# print(harfler)

# Listedeki isimleri alfabetik sıraya göre sıralayalım
isimler = ["Eren", "Ersin", "Ahmet", "Kaan", "Kemal", "Hüseyin"]
isimler.sort()
# print(isimler)

# listeyi temizleyelim: clear()
isimler.clear()
print(isimler)
