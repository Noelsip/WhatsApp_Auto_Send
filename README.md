# WhatsApp Auto Sender

Program ini digunakan untuk mengirim **pesan WhatsApp otomatis** ke **banyak nomor** menggunakan Python.
---

## Persyaratan

- Python 3.8 atau lebih baru
- Browser Chrome
- Akun WhatsApp aktif
- Koneksi internet stabil

---

## Langkah Penggunaan

### 1. Clone Repository
Clone project ini ke komputer kamu:

```bash
git clone https://github.com/Noelsip/WhatsApp_Auto_Send.git
cd WhatsApp_Auto_Send
```

### 2. Aktifkan Virtual Environment
ketik perintah berikut pada terminal

```bash
.\env\Scripts\activate
```

Kalau berhasil, terminalmu akan muncul (env) di depannya, contoh:

```bash
(env) C:\Users\user\Documents>
```

### 3. Lakukan Instalasi Library
Lakukan penginstalan library dengan perintah berikut:

```bash
pip install -r requirements.txt
```

### 4. 📝 Persiapan Data
Lakukan penginputan nomor dengan cara:
- Buka file Json pada repository ini
- Masukan nomor tujuan pada array dibawah ini

```bash
"numbers": [
        "+628123567890"
    ]
```

### 5. ✏️ Ubah Pesan yang Ingin Dikirim
Di dalam file Python, ubah variabel pesan sesuai kebutuhan:

```bash
pesan = "Halo, ini pesan otomatis. Semoga harimu menyenangkan!"
```

### 6. ▶️ Cara Menjalankan Program
- Pastikan kamu sudah login ke [WhatsApp Web](https://web.whatsapp.com/)
 di browser (minimal 1x sebelumnya dan mencentang tetap login).
- Buka terminal dan jalankan perintah berikut

```bash
python main.py
```

- Program akan membuka tab WhatsApp Web, mengirimkan pesan ke setiap nomor satu per satu, dan menutup tab setelah selesai.
- Program menggunakan pyautogui untuk klik otomatis, jadi **JANGAN GERAKAN MOUSE ATAU KURSOS SAAT MENGIRIM PESAN.**
