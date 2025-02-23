# 2 Practice Slicing and Striding
# 2.1 Making a Variable List
nums_to_twenty = list(range(21))
print(nums_to_twenty)



# 2.2 Working with List Elements
def squareList(my_list):
    for i in my_list:
        my_list[i] = i**2

        """I encountered the following error: "SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?"
       I flipped the two sides of the equal sign and the error went away."""
        
    return my_list

nums_squared = squareList(nums_to_twenty)
print(nums_squared)



# 2.3 Slicing
def first_fifteen_elements(list):
    return list[0:15]

print(first_fifteen_elements(nums_squared))



# 2.4 Striding
def every_fifth_element(list):
    return list[4:21:5]

print(every_fifth_element(nums_squared))



# 2.5 Slicing & Striding
def fancy_function(list):
    new_list = list[0:18]
    return new_list[::-3]

print(fancy_function(nums_squared))


# 3 2D Lists
# 3.1 Creating 5x5 2D List
def create_2d_list(list):
    list = (list(range(1, 6)), list(range(6, 11)), list(range(11, 16)), list(range(16, 21)), list(range(21, 26)))
    return list

matrix = create_2d_list(list)
print(matrix)



# 3.2 Replacing 2D List with Multiples of 3
def modified_2d_list(twod_list):
    for num_list in twod_list:
        for number in range(len(num_list)):
         
         """I encountered the following error: "IndexError: list assignment index out of range"
         I added my code to range(len(num_list)) and the error went away."""
         
         if num_list[number] % 3 == 0:
            num_list[number] = "?"
    return twod_list
#print(modified_2d_list(matrix))



# 3.3 Summing None- "?" Elements
new_matrix = modified_2d_list(matrix)
print(new_matrix)

def sum_non_question_elements(twod_list):
    sum = 0
    for num_list in twod_list:
        for number in range(len(num_list)):
         if type(num_list[number]) == int:
            sum += num_list[number]
    return sum

print(sum_non_question_elements(new_matrix))