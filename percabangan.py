nilai = int(input('masukkan nilai ujian akhir anda: '))

if nilai >= 85:
    print('predikat: A')
elif nilai >= 70-84:
    print('predikat: B')
elif nilai >= 55-69 :
    print('predikat: c')
elif nilai >= 55:
    print('predikat: D')
else:
    print('predikat: E')