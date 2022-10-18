# This program looks for a number that is equal to the number of times this number appears

def CountElements(arr):

    tam = len(arr)
    soma = 0
    total = -1
    i = 0
    while i < tam:
        j = 0
        while j < tam:
            if arr[i] == arr[j]:
                soma += 1
            j += 1
        if soma == int(arr[i]):
            total = soma
            break
        i += 1
        soma = 0
    arr[1] = str(total)


numbers = input('Enter numbers separeted by space, where a number n appear n times: ').split(' ')
tam = len(numbers)

if tam == 1:    # Restriction of CountElements function
    numbers.insert(0,'0')
    tam = 2;

for index in range(tam):
    int(numbers[index])

#for index, item in enumerate(numbers):
#    int(item)

CountElements(numbers)
print(f'The equal number is : {numbers[1]}')

