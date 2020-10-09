def stringPrincipality(matriks, baris, kolom):
    stringDiagonal = ""
    for i in range(baris):
        for j in range(kolom):
            if i == j:
                stringDiagonal += str(matriks[i][j]) + " "
    return stringDiagonal


def hitungDiagonal(matriks, baris, kolom):
    sum = 0
    for i in range(baris):
        for j in range(kolom):
            if i == j:
                sum += matriks[i][j]
    return sum


def main():
    baris = int(input("Silahkan Masukan Baris : "))
    kolom = int(input("Silahkan Masukan Kolom : "))
    matriks = []
    if baris == kolom:
        for i in range(baris):
            isiMatriks = []
            for j in range(kolom):
                isi = int(input(""))
                isiMatriks.append(isi)
            matriks.append(isiMatriks)
        diagonalUtama = hitungDiagonal(matriks, baris, kolom)
        diagonalUtamaString = stringPrincipality(matriks, baris, kolom)
        print("Diagonal Utama : ", diagonalUtamaString)
        print("Nilai Total Diagonal Utama : ", diagonalUtama)
    else:
        print(
            "Matriks yang dibuat bukan Persegi sehingga tidak memiliki diagonal utama \n"
        )


if __name__ == "__main__":
    main()
