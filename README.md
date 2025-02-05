# Python---OOP💻
## Fellicia Devina
---

## 💡Tentang aplikasi Data Penjualan Handphone
Aplikasi ini dirancang untuk:
- Mencatat penjualan handphone dengan informasi detail dari berbagai merek.
- Menghitung total penjualan berdasarkan harga dan jumlah unit yang terjual secara otomatis.


Aplikasi ini menggunakan pendekatan **Pemrograman Berorientasi Objek (OOP)** dengan Python, yang memudahkan admin dalam mengelola data dan memberikan kemudahan dalam perhitungan penjualan yang lebih efisien.

## 1. Konsep dasar OOP Python
[Diagram Konsep](https://excalidraw.com/#json=w6A36x2xQb6Bk_yD8fVpT,ct1yy5XzDHssWsyY1YI3Ww)

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
Admin/Pegawai Toko (pengguna sistem)

### **🗒️Use Case:**
- Menambahkan data handphone → Admin memasukkan informasi handphone yang terjual.
- Melihat daftar handphone terjual → Menampilkan daftar semua penjualan handphone yang telah diinput.
- Melihat total penjualan per merek → Menampilkan total penjualan berdasarkan merek handphone.
- Melihat total seluruh penjualan → Menghitung jumlah semua penjualan pada tanggal tersebut.

---

## 4. Sequence Diagram

---

## 5. CLI Apps
![output](https://github.com/user-attachments/assets/bfed9370-0c3c-4313-8d9a-3fc88e4f24ee)
![output 2](https://github.com/user-attachments/assets/c48a15e7-99f7-47d8-8fb7-1e68a4430e0b)


---
