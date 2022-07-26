"""
In this section, we are discussing about,
3. list : There is a option to store  collection of elements like list of names, list of email-ids etc
                    But we dont know how?
                    - MUTABLE : After creating the list, throught the program,
                    we CAN modify the list(we can add element / we can remove element / we can update element / )
                    - automatically index will be assigned to each value

"""

print("list PART - 1")
print("-"*20)
# -----------------------

my_list_1 = [10, 12.5, "Java", "Python", [100, 200] ]
# Or create using class name
my_list_2 = list([10, 12.5, "Java", "Python", [100, 200] ])

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end="\n\n")
####################

print("list PART - 2")
print("-"*20)
# -----------------------

# Indexes/slicing are similar to strings
my_list_3 = [10, 12.5, "Java", "Python", [100, 200] ]
print("my_list_3 : ", my_list_3)

print("1st Course : ", my_list_3[2]) # "Java"
print("2nd char at 1st Course : ", my_list_3[2][1]) # "a"

print("#"*40, end="\n\n")
####################




print("list PART - 3")
print("Methods inside the list class")
print("-"*20)
# -----------------------
print(dir(my_list_3))
print("#"*40, end="\n\n")
####################
print("list PART - 4")
print("Trying few methods")
print("-"*20)
# -----------------------
my_courses = ["Java", "Python", "C++", "C"]
print("my_courses : ", my_courses)
# add elemnent
my_courses.append('Perl')
print("my_courses after appending PERL : ", my_courses)
# Update C++ to java script
my_courses[2] = 'java script'
print("my_courses after updating C++ to Java Script : ", my_courses)
# remove python
my_courses.remove('Python') # It will remove only one python
print('after remove python : ', my_courses)
print("#"*40, end="\n\n")
####################
