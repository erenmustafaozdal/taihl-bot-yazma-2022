# selenium ve diğer paketler içeri aktaralım
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

tarayici = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Tarayıcıda gezinme
tarayici.get("https://teknolojiaihl.meb.k12.tr")
print(tarayici.current_url)
sleep(1)

# yeni adrese gidelim
tarayici.get("https://teknolojiaihl.meb.k12.tr/34/40/766892/teskilat_semasi.html")
print(tarayici.title)
sleep(1)

# geri dönelim
tarayici.back()
print(tarayici.title)
sleep(1)

# ileri gidelim
tarayici.forward()
print(tarayici.title)
sleep(1)

# pencere boyutunu yazdıralım
print(tarayici.get_window_size())

# pencere boyutu ayarlayalım
tarayici.set_window_size(500, 300)
sleep(2)

# pencerenin pozisyonunu yazdıralım
print(tarayici.get_window_position())

# pencerenin pozisyonunu ayarlayalım
tarayici.set_window_position(100, 500)
sleep(2)

# penceremizi tam ekran yapalım
tarayici.maximize_window()
sleep(2)

# pencereyi simge durumuna küçültelim
tarayici.minimize_window()
sleep(2)

# pencereyi tam ekran yapalım
tarayici.fullscreen_window()
sleep(2)

# ekran görüntüsü alalım
tarayici.save_screenshot("./gorseller/bot-yazma.png")
