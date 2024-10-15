from logging import raiseExceptions
from operator import indexOf

# 2.a wrong_add_function has numeric section corrected and is renamed correct_add_function
def correct_add_function(arg1, arg2):
    # numeric section
    if sum([type(i) == int for i in arg1]) == len(arg1) and \
            sum([type(i) == int for i in arg2]) == len(arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
            arg1[arg1_index] = arg_2_sum
            arg1_index += 1
        return arg1
    # string section
    elif sum([type(i) == str for i in arg1]) == len(arg1) and \
            sum([type(i) == str for i in arg2]) == len(arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
            arg1_index += 1
        return arg1
    # Handles edge cases where input lists are entirely of inappropriate type
    else:
        raise TypeError

# 2.b exception_add_function raises an exception for arguments of inappropriate type
def exception_add_function(arg1, arg2):
    error_index = 0
    expected_type = type(arg1[0])
    error_arg = 0
    i = 0
    try:
        for i in arg1:
            if type(i) != expected_type:
                error_index = indexOf(arg1,i)
                error_arg = arg1
                raise TypeError
        for i in arg2:
            if type(i) != expected_type:
                error_index = indexOf(arg2,i)
                error_arg = arg2
                raise TypeError
    except TypeError:
        print(f"Your input element {i} at argument index {error_index} in {error_arg} is "
              f"not of the expected type ({expected_type}). Please change this and rerun.")
    else:
        try:
            return correct_add_function(arg1, arg2)
        # Handles edge cases where input lists are entirely of inappropriate type
        except TypeError:
            print("Error: Please ensure inputs are lists of str or int")

# 2.c correction_add_function converts bad inputs to string inputs
def correction_add_function(arg1,arg2):
    # Assumes first element in arg1 is the intended type for list elements
    expected_type = type(arg1[0])
    try:
        for i in arg1:
            if type(i) != expected_type:
                raise TypeError
        for i in arg2:
            if type(i) != expected_type:
                raise TypeError
    # If a type mismatch is detected in arguments, elements of both lists are cast to strings
    # function then proceeds normally through string logic
    except TypeError:
        arg1_s = list(map(str, arg1))
        arg2_s = list(map(str, arg2))
        return correct_add_function(arg1_s, arg2_s)
    # If no type mismatch (all int or all string elements) function proceeds normally
    else:
        try:
            return correct_add_function(arg1, arg2)
        # Handles edge cases where input lists are entirely of inappropriate type
        except TypeError:
            print("Error: Please ensure inputs are lists of str or int")


arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '2', 3]

two_b = exception_add_function(arg_str_1, arg_str_2)
print("2.b exception output:")
print(two_b)

arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '2', 3]

two_c = correction_add_function(arg_str_1, arg_str_2)
print("2.c correction output:")
print(two_c)

