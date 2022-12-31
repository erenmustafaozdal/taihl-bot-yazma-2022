# tarayıcı nesnemizi import edelim
from moduller.tarayici import Tarayici
from selenium.webdriver.common.by import By

tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()

# okulun internet sitesine gidelim
tarayici.get("https://teknolojiaihl.meb.k12.tr")
tarayici.maximize_window()

# class seçici kullanarak bir elemana ulaşalım
baslik = tarayici.find_element(By.CLASS_NAME, "container")
# başlığın ekran görüntüsünü alalım
baslik.screenshot("./gorseller/baslik.png")
