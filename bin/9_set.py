"""
In this section, discuss about,
6. set : There is a option to store  collection of elements like list of names, list of email-ids etc
                    But we dont know how?
                    - MUTABLE : After creating the list, throught the program,
                    we CAN modify the list(we can add element / we can remove element / we can update element / )
                    - No index
                    - No key
                    - Un ordered
                    - Only we can store IMMUTABLE values (Objects)
                    - It keeps UNIQUE. It removes duplicates.
                    - to get values, we can use loops else we can convert to list
"""
print("Set PART - 1")
print("-"*20)
# ----------------------
my_set_1 = {10, 10, 10, 20, 20, "C", "C", "Java"}
# if we provide only values then it will become set
my_set_2 = set({10, 10, 10, 20, 20, "C", "C", "Java"})
print(my_set_1, my_set_2, sep="\n")
print('#'*40, end="\n\n")
###################
print("Set PART - 2")
print("Methods inside set class")
print("-"*20)
# ----------------------
my_list = list(my_set_1)
print(dir(my_set_1))
print('#'*40, end="\n\n")
###################
print("Set PART - 3")
print("Trying few methods")
print("-"*20)
# ----------------------
sb_acc_customers = { 'cust-1', 'cust-2', 'cust-3', 'cust-4'}
ca_acc_customers = { 'cust-3', 'cust-4', 'cust-5', 'cust-6'}
print('sb_acc_customers : ', sb_acc_customers)
print('ca_acc_customers : ', ca_acc_customers)
# union : OR
all_customers = sb_acc_customers.union(ca_acc_customers)
print("all_customers : ", all_customers)
# Intersection : AND : {'cust-3', 'cust-4'}
both_acc_holders = sb_acc_customers.intersection(ca_acc_customers)
print("both_acc_holders : ", both_acc_holders)
# Difference : { 'cust-1', 'cust-2', }
having_sb_not_ca = sb_acc_customers.difference(ca_acc_customers)
print("having_sb_not_ca : ", having_sb_not_ca)
print('#'*40, end="\n\n")
###################
