def tampilDataBukuKeseluruhan(arrayBuku):
    stringHasil = ""
    for i in range(len(arrayBuku)):
        if arrayBuku[i][0] == "NONE":
            stringHasil += (
                str(0)
                + " "
                + arrayBuku[i][0]
                + " "
                + arrayBuku[i][1]
                + " "
                + str(arrayBuku[i][2])
                + " "
                + arrayBuku[i][3]
                + "\n"
            )
        else:
            stringHasil += (
                str(i + 1)
                + " "
                + arrayBuku[i][0]
                + " "
                + arrayBuku[i][1]
                + " "
                + str(arrayBuku[i][2])
                + " "
                + arrayBuku[i][3]
                + "\n"
            )
    return stringHasil


def cariBukuJudul(arrayBuku, judul):
    stringHasil = ""
    for i in range(len(arrayBuku)):
        if arrayBuku[i][0] == judul:
            stringHasil += (
                str(i + 1)
                + " "
                + arrayBuku[i][0]
                + " "
                + arrayBuku[i][1]
                + " "
                + str(arrayBuku[i][2])
                + " "
                + arrayBuku[i][3]
                + "\n"
            )
    if stringHasil == "":
        stringHasil = "Buku Tidak Ditemukan \n"
    return stringHasil


def cariBukuPenulis(arrayBuku, Penulis):
    for i in range(len(arrayBuku)):
        if arrayBuku[i][1] == Penulis:
            print(arrayBuku[i][0])


def cariBukuStatus(arrayBuku, status):
    for i in range(len(arrayBuku)):
        if arrayBuku[i][3] == status:
            print(arrayBuku[i][0])


def selection_sort(arrayBuku):
    for i in range(len(arrayBuku) - 1):
        min_idx = i
        for j in range(i + 1, len(arrayBuku) - 1):
            if arrayBuku[j][2] < arrayBuku[min_idx][2]:
                min_idx = j
        temp = arrayBuku[i]
        arrayBuku[i] = arrayBuku[min_idx]
        arrayBuku[min_idx] = temp


def main():
    # Inisialisasi
    arrayBuku = [
        ["Naruto 1", "Masashi Kishimoto", 2004, "Dipinjam"],
        ["Naruto 2", "Masashi Kishimoto", 2004, "Dipinjam"],
        ["Detektif Conan", "Gyoso Aoyama", 2001, "Tidak Dipinjam"],
        ["Doraemon", "Fujiko F Fujio", 1990, "Dipinjam"],
        ["NONE", "NONE", 0, "NONE"],
    ]

    # Tampil Data Keseluruhan
    dataKeseluruhan = tampilDataBukuKeseluruhan(arrayBuku)
    print(dataKeseluruhan)

    # Search Judul
    namaBuku = str(input("Cari Judul Buku ? "))
    data = cariBukuJudul(arrayBuku, namaBuku)
    print(data)

    # Search Penulis
    namaPenulis = str(input("Cari Penulis Buku ? "))
    cariBukuPenulis(arrayBuku, namaPenulis)

    # Search Status
    status = str(input("\nCari Status Buku ? "))
    cariBukuStatus(arrayBuku, status)
    print("\n")

    # Sorting Data Ascending
    selection_sort(arrayBuku)
    print("Data Di urutkan menaik")
    print(tampilDataBukuKeseluruhan(arrayBuku))


if __name__ == "__main__":
    main()
