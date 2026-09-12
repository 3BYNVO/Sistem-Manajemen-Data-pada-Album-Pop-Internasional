Album_Pop = [
    ["Petal", "Ariana Grande", 4.7], 
    ["YSPSFAGSIL", "Olivia Rodrigo", 4.9], 
    ["brat", "Charli XCX", 3.9], 
    ["WOR$T GIRL IN AMERICA", "Slayyyter", 4.0], 
    ["LUX", "Rosalia", 4.3]
]
daftar_album = []

while True:
    print("Selamat datang di Nada Internasional Anda!")
    print("1. Lihat Daftar Album Pop")
    print("2. Tambahkan Album Favorit Anda!")
    print("3. Ubah Rating Album")
    print("4. Hapus Album")
    print("5. Keluar")
    menu=input("Pilih menu anda: (1-5):")

    if menu == "1":
        print("\n===== DAFTAR ALBUM POP =====")
        for i in range(len(Album_Pop)):
            print("-", i+1, ":", Album_Pop[i])

    elif menu == "2":
        print("Ketik 'selesai' jika anda merasa cukup dengan albumnya.")
        Album = input("Tambahkan Album : ")
        if Album == "selesai":
            continue
        Artis = input("Tambahkan Artis : ")
        Rating = float(input("Rating Album: "))
        if Rating <= 0.0:
            print("Rating tidak boleh 0.0 atau minus, ulangi input item ini.")
        else:
            Album_Pop.append((Album, Artis, Rating))
            print("\n===== DAFTAR ALBUM POP =====")
            for i in range(len(Album_Pop)):
                print("-", i+1, ":", Album_Pop[i])

    elif menu == "3":
            print("Daftar album yang sudah dirating:" )
            for i in range(len(Album_Pop)):
                print("-", i+1, ":", Album_Pop[i])
            ubah = input("Masukkan Album yang ingin diubah ratingnya: ")
            for i in range(len(Album_Pop)):
                if Album_Pop[i][0] == ubah:
                    rating_baru = float(input("Rating Album baru: "))
                    if rating_baru < 0 or rating_baru > 10:
                        print("ulangi input item ini.")
                    else:
                        print("Rating", ubah, "berhasil diubah menjadi", rating_baru,)
                        print("\n===== DAFTAR ALBUM POP =====")
                        Album_Pop[i][2] = rating_baru
                        for i in range(len(Album_Pop)):
                            print("-", i+1, ":", Album_Pop[i])

    elif menu == "4":
        hapus = input("Album yang akan dihapus dari daftar: ")
        Album_Pop = [i for i in Album_Pop if i [0] !=hapus]
        print("\n===== DAFTAR ALBUM POP =====")
        for i in range(len(Album_Pop)):
            print("-", i+1, ":", Album_Pop[i])

    elif menu == "5":
        print("Terima kasih telah mendengarkan karya internasional!")
        break
    else:
        print("input kembali pilihan anda.")