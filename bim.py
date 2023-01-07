"""
1. Aktüel ürünler sayfasına git
    https://www.bim.com.tr/Categories/100/aktuel-urunler.aspx
2. Gelecek Hafta'ya tıkla
3. Tarihlere tıklayarak aşağıdaki işlemleri yap
    3.1. Ürünler içinde aşağıdaki işlemleri
        3.1.1. Ürün resmini kaydet
        3.1.2. Ürün bilgilerini oku
        3.1.3. Ürün fiyatını oku
"""
from moduller.tarayici import Tarayici
from selenium.webdriver.common.by import By
from time import sleep

# Tarayıcıyı oluştur
tarayici_nesne = Tarayici()
tarayici = tarayici_nesne.al()

# 1. Aktüel ürünler sayfasına git
tarayici.get("https://www.bim.com.tr/Categories/100/aktuel-urunler.aspx")
sleep(2)

# Çerezleri kabul et
# tarayici.find_element(By.XPATH, '//*[@id="form1"]/div/footer/div/div[5]/button[1]').click()
tarayici.find_element(By.XPATH, "//button[contains(text(), 'Kabul Et')]").click()

# 2. Gelecek Hafta'ya tıkla
tarayici.find_element(By.XPATH, "//span[normalize-space()='GELECEK HAFTA']").click()

# 3. Tarihlere tıklayarak aşağıdaki işlemleri yap
tarihler = tarayici.find_elements(By.XPATH, "//div[@class='subButtonArea subButtonArea-5 active']//a")

# tarihlerdeki işlemleri for içinde yapacağız
for i, tarih in enumerate(tarihler):
    # tarayici.execute_script("window.scrollTo(0, 0);")  yukarı kaydırma hatayı gidermedi

    # sayfa yenilenince elemanlar tekrar oluşturuluyor.
    # Bu sebeple döngü içinde sıradaki elemanı yeniden seçmemiz gerekiyor.
    tarih = tarayici.find_element(By.XPATH, f"//div[@class='subButtonArea subButtonArea-5 active']//a[{i+1}]")

    # ekran görüntüleri alındığında sayfa aşağı iniyor ve tarih tıklamada üst çubuk engel oluyor. Javascript ile tıklama yapacağız
    tarayici.execute_script("arguments[0].click();", tarih)
    # tarih.click()  # sayfa yenileniyor
    sleep(2)

    # 3.1. Ürünler içinde aşağıdaki işlemleri
    urunler = tarayici.find_elements(By.XPATH, "//div[contains(@class, 'product')]")
    for urun in urunler:
        try:
            # ürünün adını alalım
            ad = urun.find_element(By.XPATH, ".//h2[@class='title']")
        except:
            # ürün adını alırken hata alırsa; ürün adı yoktur demektir
            continue

        try:
            # 3.1.1. Ürün resmini kaydet
            urun.find_element(By.TAG_NAME, "img").screenshot(f"./gorseller/{ad.text}.png")
        except:
            # görünmeyen ürünlerin ekran görüntüsü alınırken hata alırsa geç
            continue

        # 3.1.2. Ürün bilgilerini oku
        # ürün markasını varsa alalım
        try:
            marka = urun.find_element(By.XPATH, ".//h2[@class='subTitle']").text
        except:
            marka = ""

        # ürünün açıklaması varsa alalım
        try:
            aciklama = urun.find_element(By.XPATH, ".//div[@class='textArea']").text
        except:
            aciklama = ""

        # 3.1.3. Ürün fiyatını oku
        fiyat = urun.find_element(By.XPATH, ".//a[@class='gButton triangle']").text

        print("-"*50)
        print("Ad:", ad.text)
        print("Marka:", marka)
        print("Açıklama:", aciklama)
        print("Fiyat:", fiyat.replace("\n", ""))
