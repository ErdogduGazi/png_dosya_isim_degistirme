import os

# PNG dosyalarının bulunduğu dizin
directory = r'D:\Mezuniyet Projesi\datasets\samples\malware\CDCGANmalware\CDCgan_malwmanifestdeneme'

# Dizin içindeki dosyaları listele
for filename in os.listdir(directory):
    # Sadece PNG dosyalarını işlemek için
    if filename.endswith(".png"):
        # Yeni dosya adı oluştur
        new_filename = filename[:-4] + "mm.png"
        # Dosyanın tam yolunu oluştur
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Dosya adını değiştir
        os.rename(old_file, new_file)

print("Dosya adları başarıyla değiştirildi.")
