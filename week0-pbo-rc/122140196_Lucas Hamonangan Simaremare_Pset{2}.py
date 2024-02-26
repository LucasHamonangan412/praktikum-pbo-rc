#122140196_Lucas Hamonangan Simaremare_Pset{2}

num_people = int(input("Masukkan jumlah orang: "))
grade_dict = {}

for _ in range(num_people):
    name = input("Nama: ")
    grade = int(input("Nilai: "))
    grade_dict[name] = grade

print("Data nilai:", grade_dict)
