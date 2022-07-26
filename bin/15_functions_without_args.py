"""
Functions: If we want to rewrite same code more than one time then
instead of rewriting, we can keep that code in a block and reuse
"""

print("Without using function")
print("-" * 20)
# ----------------------------

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

print("#" * 40, end="\n\n")
##############################


print("Using function")
print("-" * 20)


# ----------------------------


# Function Definition
def my_func():
    a = 10
    b = 20
    c = a + b
    print("c : ", c)


# Function Call
my_func()
my_func()
my_func()
my_func()
my_func()
my_func()

print("#" * 40, end="\n\n")
##############################


print("Just Another Function")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)


employee()
employee()
employee()
employee()

print("#" * 40, end="\n\n")
##############################
