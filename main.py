sepet = []

print("--- ALIŞVERİŞ LİSTESİ ---")

# 1. Veri Toplama Aşaması
while True:
    # .strip().capitalize() ile 'elma' yazsa bile 'Elma' olarak kaydederiz.
    urun = input("Sepete ne eklemek istersin? (Çıkış 'q'): ").strip().capitalize()

    if urun == "Q" or urun == "q":
        print("Alışveriş tamamlandı. İşte listeniz:")
        break  # Döngüyü kırıp dışarı çıkıyoruz.

    sepet.append(urun)  # Listeye ekleme yapıyoruz.
    print(f"'{urun}' sepete eklendi.")

# 2. Raporlama Aşaması (Döngüden çıktıktan sonra çalışır)
print("-" * 30)  # Görsel ayraç

# enumerate fonksiyonu: Hem sıra numarasını (i) hem ürünü verir.
# start=1 dedik ki saymaya 0'dan değil 1'den başlasın.
for i, eleman in enumerate(sepet, start=1):
    print(f"{i}. {eleman}")
