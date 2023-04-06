
# Q1: 
numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]

def sum_numbers(numbers:list):
    total = 0
    for number in numbers:
        total += number

    return total

print(sum_numbers(numbers_list))

# Q2: 
def largest_num(numbers:list):
    largest_number = 0

    for number in numbers:
        if number > largest_number:
            largest_number = number
    
    return largest_number

print("largest number: ", largest_num(numbers_list))


# Q3:         
odd_numbers = [number for number in range(1200, 2000, 125) if number%2 != 0]

print(odd_numbers)


# Q4: 
new_list = numbers_list[:5]
print(new_list)