def demonstrate_casting(raw_input: str):
    """Mendemonstrasikan type casting eksplisit dari string ke tipe lainnya."""
    print(f"\nAnalisis Input Mentah: '{raw_input}' (Tipe: {type(raw_input).__name__})")
    
    results = []

    # 1. Casting ke Integer
    try:
        val_int = int(raw_input)
        results.append(("int", f"{val_int}", "Sukses", "Konversi angka bulat berhasil."))
    except ValueError as e:
        results.append(("int", "-", "Gagal", f"ValueError: {e}"))
    except TypeError as e:
        results.append(("int", "-", "Gagal", f"TypeError: {e}"))

    # 2. Casting ke Float
    try:
        # Penanganan koma desimal khas Indonesia ke titik desimal standar pemrograman
        cleaned_float_str = raw_input.replace(',', '.')
        val_float = float(cleaned_float_str)
        # Menampilkan representasi presisi tinggi untuk mendemonstrasikan float accuracy
        precision_demo = f"{val_float} (Presisi internal: {val_float:.20f})"
        results.append(("float", precision_demo, "Sukses", "Konversi floating-point berhasil."))
    except ValueError as e:
        results.append(("float", "-", "Gagal", f"ValueError: {e}"))
    except TypeError as e:
        results.append(("float", "-", "Gagal", f"TypeError: {e}"))

    # 3. Casting ke Boolean (Truthy/Falsy Analysis)
    try:
        val_bool = bool(raw_input)
        truthy_falsy_status = "Truthy (String tidak kosong)" if val_bool else "Falsy (String kosong)"
        results.append(("bool", f"{val_bool}", "Sukses", f"{truthy_falsy_status}."))
    except (ValueError, TypeError) as e:
        results.append(("bool", "-", "Gagal", f"Error: {e}"))

    # 4. Casting ke String
    try:
        val_str = str(raw_input)
        results.append(("str", f"'{val_str}'", "Sukses", "Selalu berhasil untuk semua input."))
    except (ValueError, TypeError) as e:
        results.append(("str", "-", "Gagal", f"Error: {e}"))

    # Format Output CLI Table
    headers = ["Target Tipe", "Hasil Konversi / Presisi", "Status", "Keterangan Analisis"]
    
    # Hitung lebar kolom dinamis
    w1 = max(len(headers[0]), max(len(r[0]) for r in results)) + 2
    w2 = max(len(headers[1]), max(len(r[1]) for r in results)) + 2
    w3 = max(len(headers[2]), max(len(r[2]) for r in results)) + 2
    w4 = max(len(headers[3]), max(len(r[3]) for r in results)) + 2

    border = f"+{'-' * w1}+{'-' * w2}+{'-' * w3}+{'-' * w4}+"

    print("\nTabel Hasil Type Casting Eksplisit:")
    print(border)
    print(f"| {headers[0].ljust(w1 - 2)} | {headers[1].ljust(w2 - 2)} | {headers[2].ljust(w3 - 2)} | {headers[3].ljust(w4 - 2)} |")
    print(border)
    for t_type, val, status, desc in results:
        print(f"| {t_type.ljust(w1 - 2)} | {val.ljust(w2 - 2)} | {status.ljust(w3 - 2)} | {desc.ljust(w4 - 2)} |")
    print(border)

def main():
    print("=== PENGANALISIS TYPE CASTING DAN VALIDASI DATA ===")
    print("Program ini akan mendemonstrasikan bagaimana Python melakukan casting")
    print("input teks mentah ke tipe data integer, float, boolean, dan string.\n")

    raw_input = input("Masukkan data mentah dari terminal: ")
    demonstrate_casting(raw_input)

    # Tambahan: Edukasi singkat perbedaan interpretasi boolean manusia vs Python
    print("\n[Catatan Edukasi Boolean]")
    print("- Python mengevaluasi `bool('False')` sebagai `True` karena string tersebut tidak kosong.")
    print("- Hanya string kosong `\"\"` yang dievaluasi sebagai `False` dalam casting boolean standar.")
    
    # Tambahan: Edukasi float accuracy
    print("\n[Catatan Edukasi Float Accuracy]")
    print("- Representasi bilangan pecahan menggunakan standard IEEE 754.")
    print("- Coba masukkan '0.1' untuk melihat hilangnya presisi desimal tepat pada digit belakang.")

if __name__ == '__main__':
    main()
