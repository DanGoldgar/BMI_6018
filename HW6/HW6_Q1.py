def wrong_add_function(arg1, arg2):
    '''
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.
    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [6,9,12]
    whereas the expected correct answer is, [2,3,4]

    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of
       arg2 added to it.

    '''
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        # This summation loop logic is useful in the string section but causes problems for the numerical section
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])
        arg_2_corr = arg1[arg1_index] + arg2[arg1_index]
        # Print error statement with expected correct value of arg_2_sum
        print(f"The program makes an error at this loop. Value of arg_2_sum is {arg_2_sum} The correct value should be: {arg_2_corr}")
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1

# Returns a list containing the elements from arg2 added to elements of arg1
def correct_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1

arg_int_1=[1, 2, 3]
arg_int_2=[1, 1, 1]

one_a = wrong_add_function(arg_int_1, arg_int_2)
print("1.a wrong_add_function output:")
print(one_a)

arg_int_1=[1, 2, 3]
arg_int_2=[1, 1, 1]

one_b = correct_add_function(arg_int_1, arg_int_2)
print("1.b correct_add_function output:")
print(one_b)