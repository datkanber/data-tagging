import os

klasor_yolu = r'C:\Users\pc\Desktop\uploads'
hatali_dosyalar = []

for dosya in os.listdir(klasor_yolu):
    if dosya.endswith('.png') and len(dosya) != 9:  # 5 karakter + 4 karakter (.png)
        hatali_dosyalar.append(dosya)

if hatali_dosyalar:
    print("Hatalı isimlendirilmiş dosyalar:")
    for dosya in hatali_dosyalar:
        print(dosya)
else:
    print("Tüm dosyalar doğru isimlendirilmiş.")
