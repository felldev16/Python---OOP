# Laporan Python : OOP💻
## Fellicia Devina
---

## 💡Tentang aplikasi Data Penjualan Handphone
Aplikasi ini dirancang untuk:
- Mencatat penjualan handphone dengan informasi detail dari berbagai merek.
- Menghitung total penjualan berdasarkan harga dan jumlah unit yang terjual secara otomatis.


Aplikasi ini menggunakan pendekatan **Pemrograman Berorientasi Objek (OOP)** dengan Python, yang memudahkan admin dalam mengelola data dan memberikan kemudahan dalam perhitungan penjualan yang lebih efisien.

## 1. Konsep dasar OOP Python
[Diagram Konsep OOP](https://excalidraw.com/#json=2lAm_yQtq_oKkQQSxF9fF,_ONspMyjV34J8Z4T9-ILTw)

![image excalidraw](https://github.com/user-attachments/assets/c7cd30b3-1da8-44fe-aef2-c534a993314d)

### **Dalam konsep OOP, berikut prinsip-prinsip OOP yang digunakan pada aplikasi ini:**
#### 🔺Enkapsulasi (*Encapsulation*)
- Atribut dan metode dalam kelas `Handphone` hanya dapat diakses melalui metode khusus (`tampilkan_info()`, `total_penjualan()`).

#### 🔺Pewarisan (*Inheritance*)
- Handphone sebagai superclass diwarisi oleh `iPhone`, `Samsung`, dan `Xiaomi`.
- Subclass hanya perlu menambahkan atribut/metode spesifiknya tanpa mengulang kode dari superclass.

#### 🔺Polimorfisme (*Polymorphism*)
- Metode `tampilkan_info()` di setiap subclass memiliki implementasi berbeda sesuai dengan atribut tambahan masing-masing.

#### 🔺Abstraksi (*Abstraction*)
- Konsep handphone digeneralisasi dalam superclass `Handphone`, sementara subclass hanya menangani fitur unik masing-masing merek.

---

## 2. Class Diagram
![class diagram](https://github.com/user-attachments/assets/356752a5-2ac2-43bb-b49a-56cbdf641cc6)


### **📱 Struktur Kelas `Handphone`**

#### Atribut:

- `merk (str)`: Merek handphone (*iPhone, Samsung, Xiaomi*).
- `model (str)`: Model handphone.
- `tanggal_jual (datetime)`: Tanggal transaksi penjualan.
- `harga (float)`: Harga satuan per unit.
- `jumlah (int)`: Jumlah unit handphone yang terjual.
- `spesifikasi (dict)`: Berisi warna dan kapasitas memori internal.

#### Metode:
- `tampilkan_info()`: Menampilkan informasi handphone.
- `total_penjualan()`: Menghitung jumlah pendapatan berdasarkan jumlah unit dan harga satuan.

### **⚪Subclass `iPhone`**

- **Atribut tambahan:** `ios_version (float)`: Versi sistem operasi iOS, `face_id (bool)`: Apakah mendukung Face ID.
- **Modifikasi metode:** `tampilkan_info()`: Menampilkan tambahan informasi versi iOS dan Face ID.

### **🔵Subclass `Samsung`**

- **Atribut tambahan:** `oneUI_version (float)`: Versi OS One UI, `s_pen (bool)`: Apakah mendukung S-Pen.
- **Modifikasi metode:** `tampilkan_info()`: Menampilkan informasi versi One UI dan dukungan S-Pen.

### **🟠Subclass `Xiaomi`**

- **Atribut tambahan:** `miUI_version (float)`: Versi OS MIUI, `watt_fastCharge (int)`: Daya pengisian cepat dalam watt.
- **Modifikasi metode:** `tampilkan_info()`: Menampilkan informasi versi MIUI dan watt fast charging.

---

## 3. Use Case Diagram
![use case](https://github.com/user-attachments/assets/4b4efc06-60a4-4a4a-8573-23f2dfae0e86)

### **🧍‍♂️Aktor utama:**
Admin (pengguna sistem)

### **🗒️Use Case:**
- Menambahkan data handphone → Admin memasukkan informasi handphone yang terjual.
- Melihat daftar handphone terjual → Menampilkan daftar semua penjualan handphone yang telah diinput.
- Melihat total penjualan per merek → Menampilkan total penjualan berdasarkan merek handphone.
- Melihat total seluruh penjualan → Menghitung jumlah semua penjualan pada tanggal tersebut.

---

## 4. Sequence Diagram
![sequence](https://github.com/user-attachments/assets/157700e1-1120-410a-a087-09acbe3d93ca)

### **📲Alur Interaksi dalam Sistem**
**▫️Membuat Objek Handphone**
   - Admin akan menginput informasi berdasarkan atribut yang ada pada  **`Handphone`** dengan memanggil fungsi **`input_user()`** dan atribut tambahan pada sub class **`iPhone, Samsung, dan Xiaomi`**.

**▫️Menyimpan Objek Handphone**
   - Semua data akan disimpan pada list **`daftar_hp`**.
  
**▫️Menghitung Total Penjualan Handphone**
   - Sistem memanggil **`total_penjualan()`** untuk menghitung total penjualan handphone, baik berdasarkan merk maupun total keseluruhan.

**▫️Menampilkan Informasi Penjualan Handphone**
   - Sistem memanggil **`tampilkan_info()`** untuk menampilkan semua daftar penjualan handphone dan total penjualan.

---

## 5. CLI Apps
![output](https://github.com/user-attachments/assets/bfed9370-0c3c-4313-8d9a-3fc88e4f24ee)
![output 2](https://github.com/user-attachments/assets/c48a15e7-99f7-47d8-8fb7-1e68a4430e0b)


---
