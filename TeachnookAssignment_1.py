

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

  
    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            sum = a+b
            print(a, "+", b, "=", sum)

        elif choice == '2':
            sub=a-b
            print(a, "-", b, "=", sub)

        elif choice == '3':
            product=a*b
            print(a, "*", b, "=", product)

        elif choice == '4':
            divide=a/b
            print(a, "/", b, "=", divide)
        
        next_calculation = input("Let's do next calculation? (Y/N): ")
        if next_calculation.upper == "N":
          break
    
    else:
        print("Invalid Input")
