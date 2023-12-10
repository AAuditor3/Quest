a = int(input("Wprowadź pierwszą liczbę całkowitą "))
b = int(input("Wprowadź drugą liczbę całkowitą "))
if b > a:
   highNum = b
   lowNum = a
elif a > b:
   highNum = a
   lowNum = b
while lowNum < highNum:
   lowNum = lowNum + 1
   print(f"{lowNum} {highNum}")
else:
   print("Zrobione!")
print(f"Liczby są równe {lowNum} {highNum}")
#