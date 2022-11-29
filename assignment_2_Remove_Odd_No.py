list =[]

number = int(input('How many numbers: '))

for n in range(number):
    numbers = int(input('Enter number '))
    list.append(numbers)


for n in list[:]:
    if (n%2)!=0: 
        list.remove(n)
print(list)