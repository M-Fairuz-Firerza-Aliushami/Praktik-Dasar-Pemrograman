def to_celsius(value: float, unit: str) -> float:
    """Mengonversi nilai suhu dari satuan asal ke Celsius."""
    unit = unit.upper()
    if unit == 'C':
        return value
    elif unit == 'F':
        return (value - 32) * 5 / 9
    elif unit == 'K':
        return value - 273.15
    elif unit == 'R':
        return value * 5 / 4
    else:
        raise ValueError(f"Satuan asal '{unit}' tidak valid.")

def from_celsius(celsius: float, target_unit: str) -> float:
    """Mengonversi nilai suhu dari Celsius ke satuan tujuan."""
    target_unit = target_unit.upper()
    if target_unit == 'C':
        return celsius
    elif target_unit == 'F':
        return (celsius * 9 / 5) + 32
    elif target_unit == 'K':
        return celsius + 273.15
    elif target_unit == 'R':
        return celsius * 4 / 5
    else:
        raise ValueError(f"Satuan tujuan '{target_unit}' tidak valid.")

def main():
    print("=== KALKULATOR KONVERSI SUHU MULTI-SATUAN ===")
    
    valid_units = {
        'C': 'Celsius (°C)',
        'F': 'Fahrenheit (°F)',
        'K': 'Kelvin (K)',
        'R': 'Reamur (°R)'
    }
    
    while True:
        # 1. Input nilai suhu dengan penanganan error input non-numerik
        while True:
            value_raw = input("Masukkan nilai suhu      : ").strip()
            try:
                # Mengganti koma dengan titik untuk fleksibilitas input desimal
                value_raw = value_raw.replace(',', '.')
                value = float(value_raw)
                break
            except ValueError:
                print("[Error] Masukkan nilai numerik yang valid (contoh: 25 atau 36.5)!")

        # 2. Input satuan asal dengan validasi input
        while True:
            unit_raw = input("Masukkan satuan (C/F/K/R): ").strip().upper()
            if unit_raw in valid_units:
                unit = unit_raw
                break
            elif unit_raw == 'CELSIUS':
                unit = 'C'
                break
            elif unit_raw == 'FAHRENHEIT':
                unit = 'F'
                break
            elif unit_raw == 'KELVIN':
                unit = 'K'
                break
            elif unit_raw == 'REAMUR' or unit_raw == 'REAUMUR':
                unit = 'R'
                break
            else:
                print("[Error] Satuan tidak dikenal! Masukkan C, F, K, atau R.")

        # 3. Validasi batas fisik (Nol Mutlak / Absolute Zero)
        celsius = to_celsius(value, unit)
        kelvin = celsius + 273.15
        
        # Menggunakan toleransi kecil untuk floating point precision
        if kelvin < -1e-9:
            print(f"[Error] Batas fisik terlampaui! Suhu tidak boleh kurang dari Nol Mutlak (0 K / -273.15°C / -459.67°F).\n"
                  f"        Nilai input setara dengan {kelvin:.2f} K. Silakan coba lagi.\n")
            continue
        
        break

    # 4. Hitung konversi ke seluruh satuan
    conversions = {}
    for u in valid_units:
        conversions[u] = from_celsius(celsius, u)

    # 5. Tampilkan hasil dalam bentuk tabel CLI terformat dengan pembulatan 2 desimal
    headers = ["Satuan", "Nilai Konversi"]
    data = [
        (valid_units['C'], f"{conversions['C']:.2f}"),
        (valid_units['F'], f"{conversions['F']:.2f}"),
        (valid_units['K'], f"{conversions['K']:.2f}"),
        (valid_units['R'], f"{conversions['R']:.2f}")
    ]

    w1 = max(len(headers[0]), max(len(row[0]) for row in data)) + 2
    w2 = max(len(headers[1]), max(len(row[1]) for row in data)) + 2

    border = f"+{'-' * w1}+{'-' * w2}+"

    print("\nHasil Konversi Perbandingan:")
    print(border)
    print(f"| {headers[0].ljust(w1 - 2)} | {headers[1].ljust(w2 - 2)} |")
    print(border)
    for k, v in data:
        print(f"| {k.ljust(w1 - 2)} | {v.rjust(w2 - 2)} |")
    print(border)

if __name__ == '__main__':
    main()
