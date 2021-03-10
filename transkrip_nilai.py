# Safira Nur Fauziah
# A11.2019.11718
# A11.4321

# Transkrip Nilai Mahasiswa
"""Membuat Transkrip Nilai Mahasiswa, jika diinputkan - 
maka program akan berhenti dan menampilkan hasil inputan"""

matkul = []
nilai = []

while (True):
    matkul_baru = str(input("Input Nama Mata Kuliah: "))
    if matkul_baru == "-":
        break
    nilai_baru = str(input("Input Nilai: "))
    print("-"*20)
    matkul.append(matkul_baru)
    nilai.append(nilai_baru)

print("Transkrip Nilai Mahasiswa")
print("-"*30)
for mt in range(len(matkul)):
    i = 0
    for nl in range(len(nilai[mt])):
        print(matkul[mt], "[Nilai:", nilai[nl], "]")
    