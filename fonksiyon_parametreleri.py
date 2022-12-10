# Öğrencinin adını, soyadını ve notlarını alıp ortalamasını
# dosyaya yazdıran bir program yazalım

# Öğrenci kaydetme fonksiyonu
def ogrenci_kaydet(ad, soyad, notlar):
    # notları integer yap ve ortalamayı hesapla
    notlar_list = [int(x) for x in notlar.split(",")]
    ortalama = sum(notlar_list) / len(notlar_list)

    # dosyaya yaz
    dosya = open("öğrenciler.txt", mode="a", encoding="utf-8")
    dosya.write(f"Ad: {ad}, Soyad: {soyad}, Notlar: {notlar}, Ortalama: {ortalama}\n")
    dosya.close()


while True:
    ne_yapilacak = input("Ne yapacaksınız? (1: Kaydet, 0: Çık): ")

    if ne_yapilacak == "0":
        break

    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    notlar = input("Sınav notları (virgülle ayrılmış): ")
    ogrenci_kaydet(ad, soyad, notlar)
