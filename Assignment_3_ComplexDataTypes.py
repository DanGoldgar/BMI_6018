print("Assignment 3: Complex Data Types")
print("Dan Goldgar u0414652")
# Note: In some cases a variable may be copied for answer formatting purposes
#       while the original variable is further modified

# Problem 1

# 1.a Create list of integers 0-9
one_a = [0,1,2,3,4,5,6,7,8,9]
print("1a:")
print(one_a)

# 1.b Add 3 to element at index 4
one_a[4]+=3
one_b = one_a.copy()
print("1b:")
print(one_b)

# 1.c Coerce list items to float numbers
one_c = [float(i) for i in one_b]
print("1c:")
print(one_c)

# 1.d Coerce list to set. Note: sets do not permit repeated values.
one_d = set(one_c)
print("1d:")
print(one_d)

# 1.e Append the value 10 to set
one_d.add(10)
one_e = one_d.copy()
print("1e:")
print(one_e)

# 1.f Pop one element from set
one_d.pop()
one_f = one_d.copy()
print("1f:")
print(one_f)

# 1.g Print length of set
one_g = len(one_d)
print("1g:")
print(one_g)

# 1.h Check if list and set have same number of items
one_h = (len(one_b)==len(one_d))
print("1h:")
print(one_h)

# 1.i Coerce set to a list and combine with list in 1.a
one_i = list(one_d) + one_a
print("1i:")
print(one_i)

# 1.j Coerce list from 1.i to a set
one_j = set(one_i)
print("1j:")
print(one_j)

# 1.k Print length of set from 1.j
one_k = len(one_j)
print("1k:")
print(one_k)

# Problem 2
# Initiate dictionaries
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

# 2.a Create nested dictionary
two_a = {"two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko,
         "two_patient_dictionary_dango" : two_patient_dictionary_dango,
         "two_patient_dictionary_mochi" : two_patient_dictionary_mochi
         }
print("2a:")
print(two_a)

# 2.b Retrieve name Dango
two_b = two_a.get("two_patient_dictionary_dango").get("name")
print("2b:")
print(two_b)

# 2.c Update year for Mochi
two_a.get("two_patient_dictionary_mochi").update({"year":2018})
two_c = two_a.copy()
print("2c:")
print(two_a)

# 2.d Create new dictionary with names as keys and years as values
two_d = {
    "Kinoko" : 2021,
    "Dango" : 2019,
    "Mochi" : 2018
}
print("2d:")
print(two_d)

# 2.e Coerce dictionary keys to a list
two_e = list(two_d.keys())
print("2e:")
print(two_e)

# 2.f Coerce dictionary keys to a list
two_f = list(two_d.values())
print("2f:")
print(two_f)

# 2.g Use zip method to recombine into dictionary
two_g = dict(zip(two_e, two_f))
print("2g:")
print(two_g)

# Problem 3
# Initiate sets
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

# 3.a Return true if E is subset of A
three_a = (three_setE.issubset(three_setA))
print("3a:")
print(three_a)

# 3.b Return true if E is strict subset of A
three_b = ((three_setA != three_setE)and(three_setE.issubset(three_setA)))
print("3b:")
print(three_b)

# 3.c Return intersection of A and B
three_c = (three_setA & three_setB)
print("3c:")
print(three_c)

# 3.d Return union of C,D,E
three_d = (three_setC | three_setD | three_setE)
print("3d:")
print(three_d)

# 3.e Add 9 to the set (set already contains 9)
three_d.add(9)
three_e = three_d.copy()
print("3e:")
print(three_e)

# 3.f Compare to original set.
three_f = (three_d == one_a)
print("3f:")
print(three_f)

# 3.g Why are they not equal?
three_g = ("The list in 1a contains 0, which this set does not. However even if they contain the same elements,"
           "they must be the same type for 3f to be True.")
print("3g:")
print(three_g)

# Problem 4
# List variable created in 4.b is modified throughout problems 4 and 5 without creating new list variables per directions.
# However since the instructions also state that each answer should be a variable with name four_b etc,
# a copy of the list is made at each step with the expected variable name

# 4.a Initiate int variable
four_a = 8
print("4a:")
print(four_a)

# 4.b Initiate empty list
four_b = []
print("4b:")
print(four_b)

# 4.c Append type of four_a (int)
four_b.append(type(four_a))
four_c = four_b.copy()
print("4c:")
print(four_c)

# 4.d Add 0.39 to variable
four_d = four_a + 0.39
print("4d:")
print(four_d)
print("0.39 added to variable")

# 4.e Append type of 0.39 to list
four_b.append(type(0.39))
four_e = four_b.copy()
print("4e:")
print(four_e)

# 4.f Exponentiate variable to the -10
four_f = round(four_d**(-10))
print("4f:")
print(four_f)

# 4.g Append type of four_f (int)
four_b.append(type(four_f))
four_g = four_b.copy()
print("4g:")
print(four_g)

# Problem 5

# 5.a create dictionary from list in problem 4
five_a = dict(zip([0,1,2],four_b))
print("5a:")
print(five_a)

# 5.b Add 300 to value stored in four_f (currently 0) and coerce to String
five_b = str(four_f + 300)
print("5b:")
print(five_b)

# 5.c Append type to list
four_b.append(type(five_b))
five_c = four_b.copy()
print("5c:")
print(five_c)

# 5.d Slice the string to 2nd character
five_d = five_b[0:2]
print("5d:")
print(five_d)

# 5.e Append type to list
four_b.append(type(five_d))
five_e = four_b.copy()
print("5e:")
print(five_e)

# 5.f Use list comprehension to convert this into a new list of integers
five_f = [i for i in five_d]
print("5f:")
print(five_f)

# 5.g Append type to list
four_b.append(type(five_f))
five_g = four_b.copy()
print("5g:")
print(five_g)

# 5.h Append type of three_setA to list
four_b.append(type(three_setA))
five_h = four_b.copy()
print("5h:")
print(five_h)
