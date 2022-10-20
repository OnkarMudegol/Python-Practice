#compund interest monthly 
P = int(input())
R = float(input())
T = float(input())
power = 12*T
division = R/1200
CI = (P*((1+division))**power)-P
print("%.2f"%(CI))