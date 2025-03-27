# Behave Automation - Saucedemo

## 📌 Deskripsi
Proyek ini adalah automasi pengujian UI untuk situs [Saucedemo](https://www.saucedemo.com) menggunakan **Selenium** dan **Behave**.

## 🛠️ Instalasi
Pastikan Python dan `pip` sudah terinstal, lalu jalankan perintah berikut untuk menginstal dependensi:
```sh
pip install -r requirements.txt
```

## 🚀 Cara Menjalankan Tes
1. Pastikan semua dependensi telah diinstal.
2. Jalankan perintah berikut untuk menjalankan semua tes:
```sh
behave
```

## 📂 Struktur Proyek
```
saucedemo-behave-test/
│-- features/
│   │-- saucedemo.feature       # File skenario Gherkin
│   │-- environment.py          # Setup & teardown WebDriver
│   │-- steps/
│   │   │-- saucedemo_steps.py  # Implementasi langkah pengujian
│-- requirements.txt            # Dependensi proyek
│-- README.md                   # Dokumentasi proyek
```

## 📜 Skenario Pengujian
- Login ke aplikasi.
- Menambahkan produk ke keranjang.
- Melakukan checkout.

## 🔧 Teknologi yang Digunakan
- Python
- Selenium WebDriver
- Behave (BDD Framework)
- ChromeDriver

