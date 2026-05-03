def kata_unik(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi_teks = file.read().lower() 
            daftar_kata = isi_teks.split()
            unik = set(daftar_kata)
            print(f"Daftar kata unik di {nama_file}:")

            for i in sorted(unik):
                print("-", i)
            return unik
            
    except FileNotFoundError:
        print("Error: File tidak ditemukan!")

file_target = input("Masukkan nama file: ")
kata_unik(file_target)