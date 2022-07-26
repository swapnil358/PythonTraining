"""
conditional statement 'if' : Based on the condition, we can execute the block of statements
"""

'''
In other languages,
if condn{
s1
    s2
        s3
    s4
s5    
}
s6

In python, we wont use {} to make a block instead we use INDENTATION to make a block
if condn:
    s1
    s2
    s3
    s4
    s5    
    if condn:
        s1
        s2
        s3
        s4
        s5    
s6
'''
print("only if")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")
if x > 10:
    print("Value of x is greater than 10")
if x < 10:
    print("Value of x is less than 10")
    

print("#"*40, end="\n\n")
#################


print("if-elif")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")
elif x > 10:
    print("Value of x is greater than 10")
elif x < 10:
    print("Value of x is less than 10")
    
print("#"*40, end="\n\n")
#################

print("if-elif-else")
print("-"*20)
# --------------------

x = 10
if x == 10:
    print("Value of x is 10")
elif x > 10:
    print("Value of x is greater than 10")
else:
    print("Value of x is less than 10")
    
print("#"*40, end="\n\n")
#################




print("if with strings")
print("-"*20)
# --------------------
my_string = "Python"
print("my_string : ", my_string)
if ((my_string != "Java") and (my_string != "C++")) or (my_string == "Python"):
    print("my_string is equal to Python")
if "tho" in my_string:
    print("Substring 'tho' found ")
if not my_string.startswith("Java"):
    print("Not Java")
print("#"*40, end="\n\n")
#################






print("if with list/tuple/set/any other collection")
print("-"*20)
# --------------------
my_courses_1 = ["Java", "C", "C++", "Python"]
my_courses_2 = ["Java", "C++", "C", "Python"]
print("my_courses_1 : ", my_courses_1, "my_courses_2 : ", my_courses_2, sep="\n")
if my_courses_1 == my_courses_2:
    print("Both list are equal")
else:
    print("Both lists are NOT equal")
if "C++" in my_courses_1:
    print("C++ found")
print("#"*40, end="\n\n")
#################





print("if with Dictionary")
print("-"*20)
# --------------------
my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)
# >>> my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
# >>> my_dictionary
# {'course': 'Python', 'duration': 4, 'location': 'India'}
# >>> my_dictionary.keys()
# dict_keys(['course', 'duration', 'location'])
if 'course' in my_dictionary.keys():
    print('key "course" found')
# >>> my_dictionary.values()
# dict_values(['Python', 4, 'India'])
if "Python" in my_dictionary.values():
    print("Value 'Python' found ")
# >>> my_dictionary.items()
# dict_items([('course', 'Python'), ('duration', 4), ('location', 'India')])
# >>>
if ('course', 'Python') in my_dictionary.items():
    print("Item ('course', 'Python') found ")
print("#"*40, end="\n\n")
#################
