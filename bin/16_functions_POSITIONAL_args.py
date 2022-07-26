"""
2 cases
Case - 1 : How access values outside the function
Case - 2 : How to pass values to variables inside the function

in this section, we will discuss about
Case - 1 : How access values outside the function
"""

print("Function with 1 return value")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return name  # what value you want send? Provide that to return.
    print("After return, if statements are present then IT WILL NEVER EXECUTE")


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function with more than 1 return value - Tuple")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return name, company  # what value you want send? Provide that to return.
    print("After return, if statements are present then IT WILL NEVER EXECUTE")


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function with more than 1 return value - Tuple")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return name, company  # what value you want send? Provide that to return.
    print("After return, if statements are present then IT WILL NEVER EXECUTE")


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function with more than 1 return value - LIST")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return [name, company]  # what value you want send? Provide that to return.
    print("After return, if statements are present then IT WILL NEVER EXECUTE")


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################

print("Function with more than 1 return value - DICT")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return {'name': name, 'company': company}  # what value you want send? Provide that to return.
    print("After return, if statements are present then IT WILL NEVER EXECUTE")


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function without return value - None")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return
    print("After return, if statements are present then IT WILL NEVER EXECUTE")


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################

print("Function without return statement - None")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function with one line expression in return statement")
print("-" * 20)


# ----------------------------


def employee():
    name = 'emp-1'
    company = 'XYZ company'
    print("name : ", name)
    print("company : ", company)
    return (10 + 20) / (10 - 20)  # Return the result


received_value = employee()
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################
