"""
In this section, we are discussing about,
4. tuple : There is a option to store  collection of elements like list of names, list of email-ids etc
                    But we dont know how?
                    - IMMUTABLE : After creating the tuple, throught the program,
                    we CAN'T modify the tuple(we can't add element / we can't remove element / we can't update element / )
                    - automatically index will be assigned to each value
"""
print("tuple PART - 1")
print("-"*20)
# -----------------------
my_tuple_1 = (10, 12.5, "Java", "Python", [100, 200] )
# Or create using class name
my_tuple_2 = tuple([10, 12.5, "Java", "Python", [100, 200] ])
print(my_tuple_1, my_tuple_2, sep="\n")
print("#"*40, end="\n\n")
####################
print("Tuple PART - 2")
print("-"*20)
# -----------------------
# Indexes/slicing are similar to strings
my_tuple_3 = (10, 12.5, "Java", "Python", [100, 200] )
print("my_tuple_3 : ", my_tuple_3)
print("1st Course : ", my_tuple_3[2]) # "Java"
print("2nd char at 1st Course : ", my_tuple_3[2][1]) # "a"
print("#"*40, end="\n\n")
####################
print("tuple PART - 3")
print("Methods inside the tuple class")
print("-"*20)
# -----------------------
print(dir(my_tuple_3))
print("Length ", len(my_tuple_3))
print("#"*40, end="\n\n")
####################
print("tuple PART - 4")
print("Trying few method")
print("-"*20)
# -----------------------
my_courses = ("Java", "Python", "C++", "C")
print("my_courses : ", my_courses)
index_of_c = my_courses.index('C')
print("index_of_c : ", index_of_c) #3
count_of_c = my_courses.count('C')
print('count_of_c : ', count_of_c)
print("#"*40, end="\n\n")
####################
