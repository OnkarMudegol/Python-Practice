#Write a program to print the following number patterns using a loop.
#	1
#	1 	2
#	1	2	3
#	1	2	3	4
#	1	2	3	4	5
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")
#	5	4	3	2	1
#	4	3	2	1
#	3	2	1
#	2	1	
#	1
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print("\n")