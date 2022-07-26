"""
In this section, we are discussing about,
2. Strings :  There is a option to store  collection of characters like name, email etc
                    But we dont know how?
                    - IMMUTABLE 
                    - automatically index will be assigned to each character                    

"""

print("Strings PART - 1")
print("-"*20)
# ---------------------

a = 'PERSON'
# internally, there is predefined class called 'str', it will create 'str' class object and store the values
# we can also create like
b = str('PERSON')

print(a, b, sep="\n")

print("#"*40, end="\n\n")
###################

print("Strings PART - 2")
print("-"*20)
# ---------------------

c = "PERSON'S"
d = 'PERSON\'S'
e = '''PERSON'S HEIGHT IS XYZ" (" represents inches)'''
f = """PERSON'S HEIGHT IS XYZ" (" represents inches)"""
# COMMENT
"""PERSON'S HEIGHT IS XYZ" (" represents inches)"""

print(c, d, e, f, sep='\n')

print("#"*40, end="\n\n")
###################





print("Strings PART - 3")
print("-"*20)
# ---------------------
g = 'C:\newfolder\test.py'
#\n & \t will get replaced with newline and tab space
print('g : ', g, sep="\n")
h = r'C:\newfolder\test.py'
# r - rawstring - \n & \t will NOT get replaced with newline and tab space
print('h : ', h, sep="\n")
print("dispaly existing string in raw fomat : ", repr(g))
print("#"*40, end="\n\n")
###################



print("Strings PART - 4")
print("-"*20)
# ---------------------
x = 10
y = 20
z = x + y
i = f'add of {x} and {y} is {z}'
# f -> format : it will replace {var_name} with values
print('i : ', i)
print("#"*40, end="\n\n")
###################
print("Strings PART - 5")
print("Access each character using INDEX")
print("-"*20)
# ---------------------
my_string = "WEL COME"
print("my_string : ", my_string)
# Refer 5_strings.xlsx SECTION-1
print("0th character using +ve index number : ", my_string[0])
print("0th character using -ve index number : ", my_string[-8])
print("1st character using +ve index number : ", my_string[1])
print("1st character using -ve index number : ", my_string[-7])
#print("10th character using +ve index number : ", my_string[10]) # ERROR
print("#"*40, end="\n\n")
###################



print("Strings PART - 5")
print("SLICING : Getting substring")
print("-"*20)
# ---------------------
my_string = "WEL COME"
print("my_string : ", my_string)
# Refer 5_strings.xlsx SECTION-2
print("Substring from index 1 to 6 using +ve index nos: ", my_string[1:6]) # EL CO
print("Substring from index 1 to 6 using -ve index nos: ", my_string[-7:-2]) # EL CO
print("Substring from index 1 to END using +ve index nos: ", my_string[1:]) # EL COME
print("Substring from index 1 to END using -ve index nos: ", my_string[-7:]) # EL COME
print("Substring from index BEGINNING to 6 using +ve index nos: ", my_string[:6]) # WEL CO
print("Substring from index BEGINNING to 6 using -ve index nos: ", my_string[:-2]) # WEL CO
print("Substring from index BEGINNING to END using +ve index nos: ", my_string[:]) # WEL COME
print("#"*40, end="\n\n")
###################



print("Strings PART - 6")
print("STEP : Skip characters")
print("-"*20)
# ---------------------

my_string = "WEL COME"
print("my_string : ", my_string)

# Refer 5_strings.xlsx SECTION-3

print("Substring from index 1 to 6 using +ve index nos, step by 1 : ", my_string[1:6]) # EL CO
print("Substring from index 1 to 6 using -ve index nos, step by 1 : ", my_string[-7:-2]) # EL CO
# default step value is 1 : Which means, from 1 to 6 give me every character

print("Substring from index 1 to 6 using +ve index nos, step by 1 : ", my_string[1:6:1]) # EL CO
print("Substring from index 1 to 6 using -ve index nos, step by 1 : ", my_string[-7:-2:1]) # EL CO
# step value is 1 : Which means, from 1 to 6 give me every character

print("Substring from index 1 to 6 using +ve index nos, step by 2 : ", my_string[1:6:2]) # 
print("Substring from index 1 to 6 using -ve index nos, step by 2 : ", my_string[-7:-2:2]) # 
# step value is 2 : Which means, from 1 to 6 give me every 2nd character

print("#"*40, end="\n\n")
###################




print("Strings PART - 6")
print("Reverse Order")
print("-"*20)
# ---------------------

my_string = "WEL COME"
print("my_string : ", my_string)

# Refer 5_strings.xlsx SECTION-4

print("Substring from index 6 to 1 using +ve index nos, step by '-1' : ", my_string[6:1:-1]) # MOC L
print("Substring from index 6 to 1 using -ve index nos, step by '-1' : ", my_string[-2:-7:-1]) # MOC L 
# step value is '-1' : Which means, from 6 to 1 give me every character in reverse direction
# +ve step value : Left to Right
# -ve step value : Right to Left

print("Substring from index 6 to 1 using +ve index nos, step by '-2' : ", my_string[6:1:-2]) # MCL
print("Substring from index 6 to 1 using -ve index nos, step by '-2' : ", my_string[-2:-7:-2]) # MCL


print("#"*40, end="\n\n")
###################






print("Strings PART - 6")
print("Methods inside the string class")
print("-"*20)
# ---------------------

my_string = "WEL COME"

print(dir(my_string))


print("#"*40, end="\n\n")
###################

print("Strings PART - 7")
print("Trying few methods")
print("-"*20)
# ---------------------

my_string = "XYXYXYXYWEL XY COMEXYXYXY"
my_string = my_string.strip('XY') # remove all 'XY' from both ends & not in between
print("my_string.strip('XY') : ", my_string)

my_string = "           WEL         COME        "
my_string = my_string.strip() # remove SPACES from both ends & not in between
print("my_string.strip() : ", my_string)

print("#"*40, end="\n\n")
###################





print("Strings PART - 8")
print("Trying few methods")
print("-"*20)
# ---------------------

my_string = "WEL COME"
print("my_string : ", my_string)

sp = my_string.split() # split by SPACE : ['WEL' , 'COME']
print("my_string.split() : ", sp)

sp = my_string.split('E') # split by 'E': ['W' , 'L COM', '']
print("my_string.split('E') : ", sp)

print("#"*40, end="\n\n")
###################





print("Strings PART - 9")
print("Trying few methods")
print("-"*20)
# ---------------------
my_string = "WEL COME"
print("my_string : ", my_string)
index_of_1st_E = my_string.index('E')
index_of_2nd_E = my_string.index('E', 3) # Start looking for E from 3rd index
index_of_last_E = my_string.rindex('E') # from right, first E
print("index_of_1st_E : ", index_of_1st_E)
print("index_of_2nd_E : ", index_of_2nd_E)
print("index_of_last_E : ", index_of_last_E)
print("#"*40, end="\n\n")
###################






print("Strings PART - 10")
print("Trying few methods")
print("-"*20)
# ---------------------
my_string = "123"
print("my_string : ", my_string)
result = my_string.isdigit() # True if All chars in string should be digits
print("my_string.isdigit() : ", result) # True
my_string = "abc123"
print("my_string : ", my_string)
result = my_string.isdigit()
print("my_string.isdigit() : ", result) # False
# Find whether last 3 chars are digit
last_3_chars = my_string[-3:] # '123'
print("last_3_chars : ", last_3_chars)
result = last_3_chars.isdigit()
print("last_3_chars.isdigit() : ", result)
my_string = "abc 123"
result = ' ' in my_string
print("result = ' ' in my_string : ", result)
print("#"*40, end="\n\n")
###################



print("Extract PICS  - one - way ")
print("-"*20)
# ----------------------
sp = in_string.split();
ímage  = sp[6];
image_1 = ímage.split('/');
print("PICS : ", image_1[2])
print("#"*40, end="\n\n")
###################
print("Extract URL - 1 - way ")
print("-"*20)
# ----------------------
raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
url = raw_url.strip('"') # strip double quotes : ["]
print('url : ', url)
print("#"*40, end="\n\n")
###################
