"""
for loop : to iterate any collection
"""
print("print each char using for loop")
print("-" * 20)
# ------------------------
my_string = "Python"
print("my_string : ", my_string)
for each_char in my_string:
    print("each_char : ", each_char)
print("#" * 40, end="\n\n")
####################
print("for with list/tuple/set/any other collections")
print("-" * 20)
# ------------------------
my_courses = ["Java", "C", "C++", "Python"]
print("my_courses: ", my_courses)
for each_value in my_courses:
    print("each_value : ", each_value)
print("#" * 40, end="\n\n")
####################


print("for with Dictionary - my_dictionary.keys()")
print("-" * 20)
# ------------------------
my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)
# >>> my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
# >>> my_dictionary
# {'course': 'Python', 'duration': 4, 'location': 'India'}
# >>> my_dictionary.keys()
# dict_keys(['course', 'duration', 'location'])
for each_key in my_dictionary.keys():
    print("each_key : ", each_key)
    print("each_key value : ", my_dictionary[each_key])
    print("-" * 10)
print("#" * 40, end="\n\n")
####################


print("for with Dictionary - my_dictionary.values()")
print("-" * 20)
# ------------------------
my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)
# >>> my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
# >>> my_dictionary
# {'course': 'Python', 'duration': 4, 'location': 'India'}
# >>> my_dictionary.values()
# dict_values(['Python', 4, 'India'])
for each_value in my_dictionary.values():
    print("each_value : ", each_value)
print("#" * 40, end="\n\n")
####################


print("for with Dictionary - my_dictionary.items()")
print("-" * 20)
# ------------------------

my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)

# >>> my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
# >>> my_dictionary
# {'course': 'Python', 'duration': 4, 'location': 'India'}

# >>> my_dictionary.items()
# dict_items([('course', 'Python'), ('duration', 4), ('location', 'India')])
# >>>

for each_item in my_dictionary.items():
    print("each_item : ", each_item)  # ('course', 'Python')
    print("key in each_item : ", each_item[0])
    print("value in each_item : ", each_item[1])
    print("-" * 10)

print("#" * 40, end="\n\n")
####################




# ------------------------
# 2 Cases
# ------------------------
# Case - 1 : How to stop the loop in between
# Case - 2 : How to skip current iteration & go for next iteration
# ------------------------

print("# Case - 1 : How to stop the loop in between")
print("-"*20)
# ------------------------

my_courses = ["C", "Java-1",  "C++", "Java-2", "Python", "Java-3"]
print("my_courses: ", my_courses )

# Requirement: Findout are there any java course in my_courses
# if one course found then it is found only, no need to check other courses

for each_course in my_courses:
    if each_course.startswith('Java'):
        print("Java course found")
        break

print("#"*40, end="\n\n")
####################





print("# Case - 2 : How to skip current iteration & go for next iteration")
print("-"*20)
# ------------------------

my_courses = ["C", "Java-1",  "C++", "Java-2", "Python", "Java-3"]
print("my_courses: ", my_courses )

for each_course in my_courses:
    # other elements are not required to proceed further
    if not each_course.startswith('Java'):
        continue # jump to next iteration

    # 100% below code is only for java courses
    print("This Java course name is : ", each_course)
    print("This is one version of java course")
    print("Thius java course duration is 1 week")
    print("-"*10)

print("#"*40, end="\n\n")
####################
