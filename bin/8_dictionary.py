"""
In this section, we are discussing about,
5. Dictionary : There is a option to store  collection of elements like list of names, list of email-ids etc
                    But we dont know how?
                    - MUTABLE: After creating the list, throught the program,
                    we CAN modify the list(we can add element / we can remove element / we can update element / )
                    - We can provide own index also called "KEY". it is key/value.
"""
print("Dictionary PART - 1")
print("-"*20)
# -----------------------
# for key, we can use any IMMUTABLE object like numbers/string/tuple etc
my_dictionary_1 = {0: "Python", 1: 4, 2: "India"}
my_dictionary_2 = {"course": "Python", "duration": 4, "location": "India"}
my_dictionary_3 = dict({"course": "Python", "duration": 4, "location": "India"})
print(my_dictionary_1, my_dictionary_2, my_dictionary_3, sep="\n")
print("#"*40, end="\n\n")
####################
print("Dictionary PART - 2")
print("Accessing values")
print("-"*20)
# -----------------------
my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)
print("Course Name : ", my_dictionary["course"]) # "Python"
print("2nd char in Course Name : ", my_dictionary["course"][1])# 'y'
print("#"*40, end="\n\n")
####################





print("Dictionary PART - 3")
print("Methods inside dictionary class")
print("-"*20)
# -----------------------
print(dir(my_dictionary))
print("#"*40, end="\n\n")
####################









print("Dictionary PART - 4")
print("Trying few methods")
print("-"*20)
# -----------------------

my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)

# Add
my_dictionary['mode'] = ['Online', 'Offline'] # If key not present then add new key
print("my_dictionary after addig 'mode' : ", my_dictionary)

# Update Python to java
my_dictionary['course'] = 'Java' # If key present update
print("after Updating Python to java : ", my_dictionary)


my_dictionary['new_duration'] = my_dictionary['duration']
removed_element = my_dictionary.pop('duration')
print('after removing  "duration" : ', my_dictionary)
print('removed_element value : ', removed_element)

print("#"*40, end="\n\n")
####################




print("Dictionary PART - 5")
print("Trying few methods")
print("-"*20)
# -----------------------
my_dictionary = {"course": "Python", "duration": 4, "location": "India"}
print("my_dictionary : ", my_dictionary)
only_keys = my_dictionary.keys()
print("only_keys : ", only_keys)
print("only_keys : ", type(only_keys))
only_values = my_dictionary.values()
print("only_values : ", only_values)
print("only_values : ", type(only_values))
both_key_val = my_dictionary.items()
print('both_key_val : ', both_key_val)
print('both_key_val : ', type(both_key_val))
print("#"*40, end="\n\n")
####################


