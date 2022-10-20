Alphabets = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a = str(input())
ind_a = Alphabets.rfind(a)
print(Alphabets[ind_a+1]+" "+ Alphabets[ind_a+2])