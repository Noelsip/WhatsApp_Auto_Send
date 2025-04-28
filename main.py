import json
import pywhatkit
import time
from tqdm import tqdm

# Baca daftar nomor dari file JSON
with open('list_numbers.json', 'r') as file:
    data = json.load(file)
    nomor_list = data['numbers']

# Pesan yang ingin dikirim
pesan = "Halo, ini pesan otomatis. Semoga harimu menyenangkan!"

# Waktu tunggu WA Web membuka (detik)
wait_time_for_web = 10

# Delay antar pengiriman pesan (detik)
delay_antar_pesan = 10

# Kirim pesan ke setiap nomor dengan progress bar
print("🚀 Mulai mengirim pesan...\n")

for i, nomor in enumerate(tqdm(nomor_list, desc="Mengirim Pesan", unit="nomor")):
    print(f"\n📨 Mengirim ke {nomor}...")

    try:
        pywhatkit.sendwhatmsg_instantly(
            nomor,
            pesan,
            wait_time_for_web,
            tab_close=True,
            close_time=3
        )

        print(f"✅ Pesan ke {nomor} telah terkirim!")
    except Exception as e:
        print(f"❌ Gagal mengirim ke {nomor}. Error: {e}")

    # Tunggu sebelum kirim ke nomor berikutnya
    if i < len(nomor_list) - 1:
        print(f"⏳ Menunggu {delay_antar_pesan} detik sebelum lanjut...")
        time.sleep(delay_antar_pesan)

print("\n🎉 Semua pesan telah dikirim!")
