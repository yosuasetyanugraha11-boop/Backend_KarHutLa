# 🚒 Backend Sistem Informasi Kebakaran (KarHutLa)

Backend API untuk sistem informasi pelaporan dan pemantauan kebakaran hutan dan lahan. Dibangun menggunakan **Flask (Python)** dan
terhubung dengan **Supabase PostgreSQL** sebagai basis data, serta dideploy secara publik menggunakan **Vercel**.

## 📌 Deskripsi Singkat Project
Project ini dikembangkan untuk memenuhi tugas pengembangan aplikasi web/backend. Sistem ini menyediakan layanan RESTful API lengkap untuk mengelola
data laporan kebakaran, data pengguna, wilayah kejadian, serta penugasan petugas secara *real-time*.

---

## 🌐 Link Deployment
* **Live API URL (Vercel):** https://backend-kar-hut-la.vercel.app
* **Repository GitHub:** https://github.com/yosuasetyanugraha11-boop/Backend_KarHutLa

---

## 📊 Skema Database & ERD
Struktur basis data dirancang menggunakan relasi antar tabel (*Foreign Key*) di Supabase PostgreSQL,
yang mencakup tabel `pengguna`, `profil_pengguna`, `wilayah`, `laporan_kebakaran`, dan `petugas_laporan`.

*(Catatan: Anda dapat melampirkan screenshot Supabase Schema Visualizer di bagian ini)*

---

## 🔌 Daftar Endpoint API

Berikut adalah daftar lengkap *endpoint* beserta contoh format *request* dan *response* pada aplikasi backend ini:

### 1. Cek Status API
* **Method:** `GET`
* **Endpoint:** `/`
* **Deskripsi:** Memeriksa apakah server API aktif dan menampilkan daftar rute yang tersedia.
* **Contoh Response (JSON):**
  ```json
  {
    "message": "API Sistem Informasi Kebakaran Aktif",
    "endpoints": {
      "get_laporan": "/laporan (GET)",
      "tambah_laporan": "/laporan (POST)"
    }
  }

### 2. Menampilkan Seluruh Laporan
* **Method:** `GET`
* **Endpoint:** `/laporan`
* **Deskripsi:** Mengambil seluruh data laporan kebakaran dari database Supabase.
* **Contoh Response (JSON):**
  ```json
  [
  {
    "id_laporan": 1,
    "id_pengguna": 2,
    "id_wilayah": 1,
    "deskripsi": "Kebakaran lahan kosong di dekat permukiman",
    "status": "proses",
    "tanggal_lapor": "2026-10-25T10:00:00"
  }
  ]
