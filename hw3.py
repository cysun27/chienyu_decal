# [1] Oski Stole Your Power
def compute_power(x, y):
    pwr = 1
    while y > 0:
        pwr = pwr*x
        y -= 1
    return pwr

x = 2
y = 3
print(compute_power(x, y))



# [2] What Should I Wear?
def temperatureRange(x):
    return min(x), max(x)

readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))



# [3] Check if its the Weekend
def isWeekend(day):
    if day == 6 or day == 7:
        return True
    elif 1 <= day <= 5:
        return False
    elif day > 7:
        return "Not a day of the week"

day = 6
print(isWeekend(day))



# [4] Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel):
    return distance/fuel

distance = 70
fuel = 21.5
print(round(fuel_efficiency(distance, fuel), 2))



#[5] Secret Code
def decodeNumbers(n):
    x = n % 10
    y = n // 10
    z = 0
    while n > 10:
        n = n/10
        z += 1
    new_n = x*(10**(z)) + y
    return new_n

n = 12345
print(decodeNumbers(n))



# [6] Min and Max but with Loops!
# [6.1] For Loop
def find_max_with_for_loop(numbers):
    maxNumber = numbers[0]
    for number in numbers:
        if number > maxNumber:
            maxNumber = number
    return (maxNumber)

nums = [2024, 98, 131, 3, 72]
print(find_max_with_for_loop(nums))


def find_min_with_for_loop(numbers):
    minNumber = numbers[0]
    for number in numbers:
        if number < minNumber:
            minNumber = number
    return (minNumber)

nums = [98, 131, 3, 72]
print(find_min_with_for_loop(nums))
        


# [6.2] While Loop
def find_max_with_for_loop(numbers):
    maxNumber = numbers[0]
    i = 0
    while i < len(numbers):
        number = numbers[i]
        if number > maxNumber:
            maxNumber = number
        i += 1
    return (maxNumber)

nums = [2024, 98, 131, 3, 72]
print(find_max_with_for_loop(nums))


def find_min_with_for_loop(numbers):
    minNumber = numbers[0]
    i = 0
    while i < len(numbers):
        number = numbers[i]
        if number < minNumber:
            minNumber = number
        i += 1
    return (minNumber)

nums = [2024, 98, 131, 3, 72]
print(find_min_with_for_loop(nums))



#[7] Counting Vowels
def vowel_and_consonant_count(text):
    lowerText = text.lower()
    seenA = False
    seenE = False
    seenI = False
    seenO = False
    seenU = False
    vowelCount = 0
    consonantCount = 0
    for char in lowerText:
        if seenA != True and char == "a":
            vowelCount += 1
            seenA = True
        elif seenE != True and char == "e":
            vowelCount += 1
            seenE = True
        elif seenI != True and char == "i":
            vowelCount += 1
            seenI = True
        elif seenO != True and char == "o":
            vowelCount += 1
            seenO = True
        elif seenU != True and char == "u":
            vowelCount += 1
            seenU = True
        elif char.isalpha() and char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            consonantCount += 1
    return vowelCount, consonantCount

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))



# [8] Calculate Digital Root
def digital_root(num):
    og_num = num
    z = 0
    while og_num > 1:
        og_num = og_num / 10
        z += 1
    
    new_num = 0
    while z >= 0:
        x = num // 10**z
        y = num % 10**z
        new_num = new_num + x
        num = y
        z -= 1
    return new_num

num = 2468
print (digital_root(num))