print(f"Enter your name:")
name = input()
print(f"Your name is {name}")
maths = int(input("Enter your maths marks"))
Physics = int(input("Enter your marks in Physics"))
Geo = int(input("Enter your marks in Geo"))
Chem = int(input("Enter your marks in Chem"))
#calculate the average
avg = (maths+Physics+Geo+Chem) / 4
print(avg)
if 0 <= avg <= 30:
    print("D")
elif 31 <= avg <= 50:
    print("C")
elif 51 <= avg <= 70:
    print("B")
elif 71 <= avg <= 30:
    print("A")
else:
    print("Unrecognized marks/avg")

