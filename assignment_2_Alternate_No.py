list =[]
number = int(input('How many numbers: '))

for n in range(number):
    numbers = int(input('Enter number '))
    list.append(numbers)
number=number-1


for n in range(number):
    if (n%2)!=0:
        list.pop(n)

print(list)