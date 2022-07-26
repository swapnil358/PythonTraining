"""
while loop : Based on the condition, we can execute the loop
"""

print("while example ")
print("-" * 20)
# ----------------------

a = 0
while a < 10:
    print("a : ", a)
    a = a + 1

print("#" * 40, end="\n\n")
########################


# ----------------------
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(2,10))
# [2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(2,10,2))
# [2, 4, 6, 8]
# >>>
# ----------------------

print("for loop example ")
print("-" * 20)
# ----------------------

for a in range(10):
    print("a : ", a)

print("#" * 40, end="\n\n")
########################


print("print each char using while loop")
print("-" * 20)
# ------------------------

my_string = "Python"
print("my_string : ", my_string)

index_no = 0
while index_no < len(my_string):
    print("Each char : ", my_string[index_no])
    index_no = index_no + 1

# for each_char in my_string:
#     print("each_char : ", each_char)

print("#" * 40, end="\n\n")
####################


print("print each char using while loop")
print("-" * 20)
# ------------------------

my_string = "PythonXYZPythonabPythonXPythonhasjdhaPythonMNC"
print("my_string : ", my_string)

# print chars coming after python

index_no = 0
while index_no < len(my_string):
    if my_string[index_no] == 'P':
        index_no = index_no + 6
    print("Each char : ", my_string[index_no])
    index_no = index_no + 1

# for each_char in my_string:
#     print("each_char : ", each_char)

print("#" * 40, end="\n\n")
####################


# ------------------------
# 2 Cases
# ------------------------
# Case - 1 : How to stop the loop in between
# Case - 2 : How to skip current iteration & go for next iteration
# ------------------------

print("# Case - 1 : How to stop the loop in between")
print("-" * 20)
# ------------------------

my_courses = ["C", "Java-1", "C++", "Java-2", "Python", "Java-3"]
print("my_courses: ", my_courses)

# Requirement: Findout are there any java course in my_courses
# if one course found then it is found only, no need to check other courses

index_no = 0
while index_no < len(my_courses):
    if my_courses[index_no].startswith("Java"):
        print("Java course found")
        break
    index_no = index_no + 1

# for each_course in my_courses:
#     if each_course.startswith('Java'):
#         print("Java course found")
#         break

print("#" * 40, end="\n\n")
####################


print("# Case - 2 : How to skip current iteration & go for next iteration")
print("-" * 20)
# ------------------------

my_courses = ["C", "Java-1", "C++", "Java-2", "Python", "Java-3"]
print("my_courses: ", my_courses)

index_no = 0
while index_no < len(my_courses):
    if not my_courses[index_no].startswith('Java'):
        index_no = index_no + 1
        continue
    # 100% below code is only for java courses
    print("This Java course name is : ", my_courses[index_no])
    print("This is one version of java course")
    print("This java course duration is 1 week")
    print("-" * 10)
    index_no = index_no + 1

# for each_course in my_courses:
#     # other elements are not required to proceed further
#     if not each_course.startswith('Java'):
#         continue # jump to next iteration
#
#     # 100% below code is only for java courses
#     print("This Java course name is : ", each_course)
#     print("This is one version of java course")
#     print("This java course duration is 1 week")
#     print("-"*10)

print("#" * 40, end="\n\n")
####################
