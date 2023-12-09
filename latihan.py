print("Halo Selamat Datang")
belanja=float(input("Masukkan jumlah belanja anda:"))
if belanja >=400000:
    print("anda mendapatkan diskon 20%")
    diskon=belanja*(20/100)
    hasil=str(belanja-diskon)
    print("Total belanja anda "+hasil)
elif belanja >=300000:
    print("anda mendapatkan diskon 10%")
    diskon=belanja*(10/100)
    hasil=str(belanja-diskon)
    print("Total belanja anda "+hasil)
elif belanja >=200000:
    print("anda mendapatkan diskon 5%")
    diskon=belanja*(5/100)
    hasil=str(belanja-diskon)
    print("Total belanja anda "+hasil)
else:
    hasil=str(belanja)
    print("total belanja anda "+hasil)