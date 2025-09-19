tugas = float(input("Masukkan nilai Tugas : "))
uts = float(input("Masukkan nilai UTS : "))
uas = float(input("Masukkan nilai UAS : "))

nilai_tugas = 0.3
nilai_uts = 0.3
nilai_uas = 0.4

nilai_akhir = (tugas * nilai_tugas) + (uts * nilai_uts) + (uas * nilai_uas)

print("nilai akhir :", nilai_akhir)