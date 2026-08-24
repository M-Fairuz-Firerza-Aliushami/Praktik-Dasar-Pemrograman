def main():
    print("=== FORMULIR BIODATA MAHASISWA ===")
    
    # 1. Menerima input dari pengguna dan bersihkan whitespace berlebih
    nama = input("Masukkan Nama           : ").strip()
    nim = input("Masukkan NIM            : ").strip()
    prodi = input("Masukkan Program Studi  : ").strip()
    
    # 2. Validasi input Semester (angka positif, try-except ValueError tanpa crash)
    semester = 0
    while True:
        semester_raw = input("Masukkan Semester       : ").strip()
        try:
            semester = int(semester_raw)
            if semester <= 0:
                print("[Error] Semester harus berupa angka bulat positif!")
                continue
            break
        except ValueError:
            print("[Error] Semester harus berupa angka!")

    # 3. Validasi input Angkatan (angka positif, try-except ValueError tanpa crash)
    angkatan = 0
    while True:
        angkatan_raw = input("Masukkan Angkatan (Tahun): ").strip()
        try:
            angkatan = int(angkatan_raw)
            if angkatan <= 0:
                print("[Error] Angkatan harus berupa angka bulat positif!")
                continue
            break
        except ValueError:
            print("[Error] Angkatan harus berupa angka!")

    # 4. Tampilkan biodata yang telah divalidasi dalam format tabel ASCII CLI box
    data = [
        ("Nama", nama),
        ("NIM", nim),
        ("Program Studi", prodi),
        ("Semester", str(semester)),
        ("Angkatan", str(angkatan))
    ]
    
    col1_header = "Kategori"
    col2_header = "Keterangan"
    
    # Menghitung lebar kolom dinamis
    w1 = max(len(col1_header), max(len(k) for k, _ in data)) + 2
    w2 = max(len(col2_header), max(len(v) for _, v in data)) + 2
    
    border = f"+{'-' * w1}+{'-' * w2}+"
    
    print("\n" + border)
    print(f"| {col1_header.ljust(w1 - 2)} | {col2_header.ljust(w2 - 2)} |")
    print(border)
    for k, v in data:
        print(f"| {k.ljust(w1 - 2)} | {v.ljust(w2 - 2)} |")
    print(border)

if __name__ == '__main__':
    main()
