
def verif():
    kode = "988765"
    masukan = str(input("Masukkan enam digit kode verifikasi: "))
    
    if len(masukan) == 6:
        if kode == masukan:
            print("Verifikasi sukses, silakan lanjutkan proses berikutnya.")
        else:
            print("Maaf, kode verifikasi Anda salah, silakan coba lagi.")
            verif()
    else:
        print("Kode verifikasi terdiri dari enam digit angka, silakan ulangi. ")
        verif()

verif()

# ATAU

while True:
    kode = "988765"
    masukan = str(input("Masukkan enam digit kode verifikasi: "))
    
    if len(masukan) == 6:
        if kode == masukan:
            print("Verifikasi sukses, silakan lanjutkan proses berikutnya.")
            break
        else:
            print("Maaf, kode verifikasi Anda salah, silakan coba lagi.")
    else:
        print("Kode verifikasi terdiri dari enam digit angka, silakan ulangi. ")