# 1 HW1/HW2 Review: The Terminal + Command Line + Git

## 1. Command: "pwd"
## 2. Command: "ls"
## 3. Commands: "cd .." , "cd brianna_repo" , "git pull origin main"
## 4. Command: "mv homework.py ~/python_decal/judy_decal/homework"
## 5. Command: "cat homework.py"
## 6. Command: "nano homework.py"
## 7. Commands: "git add homework.py" , "git commit -m 'Adding homework.py'" , "git push origin main"
## 8. Commands: "git pull --rebase origin main" , "git push origin main"
## 9. Command: cd ~/Recents/



# 2 HW3 Review: Data Types + Functions + Conditionals + Loops
# 2.1 Data Types
def checkDataType(x):
    print(type(x).__name__)

x = 3.14
checkDataType(x)



# 2.2 Conditionals
def evenOrOdd(y):
    if y%2 == 0:
        print("Even")
    else:
        print("Odd")
    return

y = 10
evenOrOdd(y)



# 3 Loops
def sumWithLoop(numbers):
    sum = 0
    for i  in range(len(numbers)):
        sum = sum + numbers[i]
    print(sum)

numbers = [1, 2, 3, 4, 5]
sumWithLoop(numbers)



# 4 HW 4 Review: Lists
# 4.1 Lists
def duplicateList(list):
    for i in range(len(list)):
        list.insert(2*i, list[2*i])
    print(list)

list = ["a", "b", "c"]
duplicateList(list)



# 4.2 Debugging

def square(num):
    return num * num
"""Added ":" at the end of the line"""

num = 3
print(square(num))