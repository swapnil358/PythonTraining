"""
In this section, we are discussing about,
    2nd way is : pass in the form of key/value

"""

print("Function with KEYWORD ARGUMENTS")
print("-" * 20)


# ----------------------------


# name, company are called KEYWORD ARGUMENTS
def employee(*, name, company):
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee(name='emp-1',
                          company='XYZ Company')  # pass in the same order mentioned in function definition
print("received_value : ", received_value)

received_value = employee(name='emp-2', company='XYZ Company')
print("received_value : ", received_value)

received_value = employee(name='emp-3', company='XYZ Company')
print("received_value : ", received_value)

received_value = employee(name='emp-4', company='MNC Company')
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################

print("Function with KEYWORD ARGUMENTS & Default value args")
print("-" * 20)


# ----------------------------


# name, company are called KEYWORD ARGUMENTS
def employee(*, name, company='XYZ Company'):  # default value args should come after non-default value
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee(name='emp-1')  # company will make use of default value
print("received_value : ", received_value)

received_value = employee(name='emp-2')  # company will make use of default value
print("received_value : ", received_value)

received_value = employee(name='emp-3', company='XYZ Company')  # company will receive this value
print("received_value : ", received_value)

received_value = employee(name='emp-4', company='MNC Company')  # company will receive this value
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################Z
