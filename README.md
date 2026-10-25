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

Berikut adalah daftar *endpoint* utama yang tersedia pada aplikasi backend ini:

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| GET | `/` | Mengecek status keaktifan dan daftar endpoint API |
| GET | `/laporan` | Menampilkan seluruh data laporan kebakaran |
| POST | `/laporan` | Menambahkan data laporan kebakaran baru |
| PUT | `/laporan/<id_laporan>` | Memperbarui deskripsi atau status laporan berdasarkan ID |
| DELETE | `/laporan/<id_laporan>` | Menghapus laporan kebakaran berdasarkan ID |

---
