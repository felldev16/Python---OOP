from datetime import datetime

# super class
class Handphone:
    def __init__(self, merk: str, model: str, tanggal_jual: str, harga: float, jumlah: int, warna: str, memori_internal: int):
        self.merk = merk
        self.model = model
        self.tanggal_jual = datetime.strptime(tanggal_jual, "%d-%m-%Y")
        self.harga = harga
        self.jumlah = jumlah
        self.spesifikasi = {
            "Warna": warna,
            "Memori Internal (GB)": memori_internal
        }
    
    def tampilkan_info(self):
        print(f"\nMerk: {self.merk}")
        print(f"Model: {self.model}")
        print(f"Tanggal Jual: {self.tanggal_jual.strftime('%d-%m-%Y')}")
        print(f"Harga (satuan): Rp{self.harga:,.2f}")
        print(f"Jumlah: {self.jumlah} unit")
        print("Spesifikasi:")
        for key, value in self.spesifikasi.items():
            print(f"  - {key}: {value}")

#sub class : mewarisi atribut dan fungsi dari super class
class iPhone(Handphone): #sub class 1
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version: float, face_id: bool):
        super().__init__("iPhone", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        # tambahan atribut, yaitu ios_version dan face_id
        self.ios_version = ios_version
        self.face_id = face_id  # True jika mendukung Face ID

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Versi iOS: {self.ios_version}")
        print(f"Face ID: {'Ya' if self.face_id else 'Tidak'}")

class Samsung(Handphone): #sub class 2
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version: float, s_pen: bool):
        super().__init__("Samsung", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        # tambahan atribut, yaitu oneUI_version dan s_pen
        self.oneUI_version = oneUI_version
        self.s_pen = s_pen  # True jika mendukung S-Pen

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"One UI Version: {self.oneUI_version}")
        print(f"S-Pen Support: {'Ya' if self.s_pen else 'Tidak'}")

class Xiaomi(Handphone): #sub class 3
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version: float, watt_fastCharge: int):
        super().__init__("Xiaomi",model, tanggal_jual, harga, jumlah, warna, memori_internal)
        # tambahan atribut, yaitu miUI_version dan watt_fastCharge
        self.miUI_version = miUI_version
        self.watt_fastCharge = watt_fastCharge  # Watt pengisian daya cepat

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"MIUI Version: {self.miUI_version}")
        print(f"Fast Charging (Watt): {self.watt_fastCharge}W")

def input_user():
    model = input("Masukkan model handphone: ")
    tanggal_jual = input("Masukkan tanggal jual handphone (dd-mm-yyyy): ")
    harga = float(input("Masukkan harga handphone (Satuan): "))
    jumlah = int(input("Masukkan jumlah handphone: "))
    warna = input("Masukkan warna handphone: ").title()
    memori_internal = int(input("Masukkan memori internal handphone (GB): "))
    return model, tanggal_jual, harga, jumlah, warna, memori_internal

if __name__ == "__main__":
    merk = input("Masukkan jenis handphone: ").lower()
    if merk == "iphone":
        model, tanggal_jual, harga, jumlah, warna, memori_internal = input_user()
        ios_version = float(input("Versi iOS: "))
        face_id = input("Mendukung Face ID? (y/n): ").lower() == 'y'
        hp1 = iPhone(model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version, face_id)
        hp1.tampilkan_info()       
    elif merk == "samsung":
        model, tanggal_jual, harga, jumlah, warna, memori_internal = input_user()
        oneUI_version = float(input("Versi One UI: "))
        s_pen = input("Mendukung S-Pen? (y/n): ").lower() == 'y'
        hp1 = Samsung(model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version, s_pen)
        hp1.tampilkan_info()
    elif merk == "xiaomi":
        model, tanggal_jual, harga, jumlah, warna, memori_internal = input_user()
        miUI_version = float(input("Versi MIUI: "))
        watt_fastCharge = int(input("Fast Charging (Watt): "))
        hp1 = Samsung(model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version, watt_fastCharge)
        hp1.tampilkan_info()
    else:
        print("Merk tidak tersedia")
        print("====Program Selesai====")
        exit()