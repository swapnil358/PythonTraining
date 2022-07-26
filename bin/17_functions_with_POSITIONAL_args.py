"""
Case - 2 : How to pass values to variables inside the function

2 ways to pass values
    1st way is : pass only values
    2nd way is : pass in the form of key/value

in this section, we are discussing about
    1st way is : pass only values
"""

print("Function with POSITIONAL ARGUMENTS")
print("-" * 20)


# ----------------------------


# name, company are called POSITIONAL ARGUMENTS
def employee(name, company):
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee('emp-1', 'XYZ Company')  # pass in the same order mentioned in function definition
print("received_value : ", received_value)

received_value = employee('emp-2', 'XYZ Company')
print("received_value : ", received_value)

received_value = employee('emp-3', 'XYZ Company')
print("received_value : ", received_value)

received_value = employee('emp-4', 'MNC Company')
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function with POSITIONAL ARGUMENTS & Default value args")
print("-" * 20)


# ----------------------------


# name, company are called POSITIONAL ARGUMENTS
def employee(name, company='XYZ Company'):  # default value args should come after non-default value
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee('emp-1')  # company will make use of default value
print("received_value : ", received_value)

received_value = employee('emp-2')  # company will make use of default value
print("received_value : ", received_value)

received_value = employee('emp-3', 'XYZ Company')  # company will receive this value
print("received_value : ", received_value)

received_value = employee('emp-4', 'MNC Company')  # company will receive this value
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################


print("Function with VARIABLE POSITIONAL ARGUMENTS")
print("-" * 20)


# ----------------------------


# *prev_companies called  VARIABLE POSITIONAL ARGUMENTS
def employee(name, company='XYZ Company', *prev_companies):
    print("name : ", name)
    print("company : ", company)
    print("prev_companies : ", prev_companies)
    return [name, company, prev_companies]


received_value = employee('emp-1')
# name='emp-1', company='XYZ Company', prev_companies=()
print("received_value : ", received_value)

received_value = employee('emp-2', 'XYZ Company')
# name='emp-1', company='XYZ Company', prev_companies=()
print("received_value : ", received_value)

received_value = employee('emp-3', 'MNC Company')
# name='emp-1', company='XYZ Company', prev_companies=()
print("received_value : ", received_value)

received_value = employee('emp-3', 'MNC Company', 'comp-1')
# name='emp-1', company='XYZ Company', prev_companies=('comp-1')
print("received_value : ", received_value)

received_value = employee('emp-3', 'MNC Company', 'comp-1', 'comp-2')
# name='emp-1', company='XYZ Company', prev_companies=('comp-1', 'comp-2')
print("received_value : ", received_value)

print("#" * 40, end="\n\n")
##############################
