# 🧠 Flask Web App
Proyek ini adalah **web app berbasis Flask (Python)** yang memiliki beberapa fitur interaktif seperti:
- Menentukan **umur** berdasarkan tahun lahir + **fakta unik dari AI (Groq API)**
- Menghitung dan menentukan **status BMI (Body Mass Index)**
- **Kalkulator sederhana**
- Menghitung **rumus bangun datar** (persegi, segitiga, lingkaran, dll)

---

## 🚀 Fitur Utama

### 🧓 1. Penentu Umur + Fakta Unik (AI)
Input: Tahun lahir  
Output:
- Umur pengguna saat ini  
- Kategori umur (anak-anak, remaja, dewasa, lansia)  
- Fakta menarik dari tahun tersebut (dihasilkan oleh **Groq AI**)

🧠 *Contoh:*
> Kamu lahir tahun **1998**, umur kamu sekarang **27 tahun (Dewasa)**.  
> Fakta unik: “Tahun 1998 adalah tahun di mana Google pertama kali didirikan oleh Larry Page dan Sergey Brin.”

---

### ⚖️ 2. Status BMI
Input: Tinggi badan (cm) & berat badan (kg)  
Output: Nilai BMI + status tubuh (Kurus, Normal, Gemuk, Obesitas)

---

### ➕ 3. Kalkulator Sederhana
Operasi dasar:
- Penjumlahan (+)
- Pengurangan (-)
- Perkalian (×)
- Pembagian (÷)

---

### 📐 4. Rumus Bangun Datar
Mendukung beberapa bentuk:
- Persegi → `L = s²`
- Persegi Panjang → `L = p × l`
- Segitiga → `L = ½ × a × t`
- Lingkaran → `L = π × r²`

---

## 🧩 Teknologi yang Digunakan

| Komponen | Deskripsi |
|-----------|------------|
| **Python 3.x** | Bahasa utama |
| **Flask** | Framework web |
| **Groq API** | AI Assistant untuk memberikan fakta unik |
| **HTML / CSS / Bootstrap** | Tampilan antarmuka |
| **Jinja2** | Template engine Flask |

---

## ⚙️ Instalasi & Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/FauziWBSCH/flask_project.git
cd flask_project
