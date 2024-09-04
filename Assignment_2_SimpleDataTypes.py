# Question 1: Booleans 1
# boolean True + boolean True - boolean False = ?
boolA = True
boolB = True
boolC = False
print(boolA+boolB-boolC)

# Question 2: Booleans 2
# Bitwise operators
tracker = True
tracker = tracker & tracker
tracker = tracker | (tracker-tracker)
print(tracker)

# Question 5: Strings 1
# String indexing starts at 0. Position [2] is a space.
bacteria = "E. coli"
print(bacteria[2])

# Question 6: Strings 2
# Are strings mutable? No!
testString = "I Bove python"
# Uncomment the line below to generate error
# testString[2] = 'L'

# Question 7
# Integer is the appropriate type for the number of medications prescribed to a patient
Medication = 5
print(type(Medication))

# Question 8
# Body Mass Index calculation
patientWeight = 60
patientHeight = 1.58
BMI = patientWeight/patientHeight
print(BMI)
print(type(BMI))


# Questions 9-10: Operators 2-3
# Demonstrate how the + operator behaves for integers vs. strings
print(7+3)
print("seventy"+"three")
print("7"+"3")
