#122140196_Lucas Hamonangan Simaremare_Pset{1}

tinggi = int(input("Tinggi = "))
for i in range(tinggi):
    for a in range(i, tinggi, 1): 
        print(" ", end="")

    for b in range(-1,i,1): 
        print("*", end="")

    for c in range(0,i,1): 
        print("*", end="")
    else:
        print(" ")
