"""
Program to communicate with external text files with any extension
like .txt, .csv, .log, .mylog, .yourlog etc
finally file which can be opened in notepad
"""

'''
We need to follow 3 steps
Step - 1 : Connect to file
Step - 2 : Read/Write
Step - 3 : Disconnect
'''

'''
3 steps : Functions
Step - 1 : Connect to file
            - open function
Step - 2 : Read/Write
            - Write : 1) write 2) writelines 3) print 
            - Read : 1) read 2) readline 3) readline using for loop
            4) readlines 5) list/tuple/set/dict classes to read file
Step - 3 : Disconnect
            - flush() # Send data from buffer to file
            - close() # 1st call flush() then disconnect
'''

"""
Program to communicate with external text files with any extension
like .txt, .csv, .log, .mylog, .yourlog etc
finally file which can be opened in notepad
"""

'''
We need to follow 3 steps
Step - 1 : Connect to file
Step - 2 : Read/Write
Step - 3 : Disconnect
'''

'''
3 steps : Functions
Step - 1 : Connect to file
            - open function
Step - 2 : Read/Write
            - Write : 1) write 2) writelines 3) print 
            - Read : 1) read 2) readline 3) readline using for loop
            4) readlines 5) list/tuple/set/dict classes to read file
Step - 3 : Disconnect
            - flush() # Send data from buffer to file
            - close() # 1st call flush() then disconnect
'''

print("Write Operations")
print("-" * 20)
# --------------------------

# We need to follow 3 steps
# Step - 1 : Connect to file
# --------------------------
# my_file_handle = open('provide file path or file name(cur dir)' , 'mode')
my_file_handle = open('../real_time_programs/my_out_file.txt', 'w')
# mode 'w' : Write Only
# mode 'w' : Create new file
# mode 'w' : ERASE the content if file present (it will make EMPTY file)

# Step - 2 : Write : 1) write 2) writelines 3) print
# --------------------------

# our data
x = 10
s = "Python\n"
x = str(x) + "\n"  # write & writelines exprects data in string

# 1) write : All data should be in one single string
my_file_handle.write(x)  # send data to buffer
my_file_handle.write(s)  # send data to buffer
my_file_handle.flush()  # send data from buffer to file my_out_file.txt

# 2) writelines : Collection of strings like it can be in list/tuple etc
my_list = [x, s]
my_file_handle.writelines(my_list)

# 3) print
print(x, s, 20, "\n", "Java", sep='', file=my_file_handle, flush=True)
print(100, 200, 300, 400, sep="\n", end='', file=my_file_handle, flush=True)
# my_file_handle.flush() # Not required
# not required to convert 20 to string. print will take care

# Step - 3 : Disconnect
# --------------------------
my_file_handle.close()

print("All data written to file, please check 'my_out_file.txt' ")

print("#" * 40, end="\n\n")
############################


print("Read Operations - 1) read")
print("-" * 20)
# --------------------------

# Step - 1 : Connect to file
# --------------------------
my_file_handle = open('../real_time_programs/my_out_file.txt', 'r')
# mode 'r' : Read only
# mode 'r' : It will not create file if not present. FileNotFound error

# Step - 2 : Read
# --------------------------
file_content = my_file_handle.read()  # read complete file content and return complete content in one string
print("file_content : ", file_content)
print("file_content RAW: ", repr(file_content))

# Step - 3 : Disconnect
# --------------------------
my_file_handle.close()

print("#" * 40, end="\n\n")
############################


print("Read Operations - 2) readline")
print("-" * 20)
# --------------------------

# Step - 1 : Connect to file
# --------------------------
my_file_handle = open('../real_time_programs/my_out_file.txt', 'r')

# Step - 2 : Read
# --------------------------
file_content = my_file_handle.readline()
print("1st line : ", file_content)

file_content = my_file_handle.readline()
print("2nd line : ", file_content)

file_content = my_file_handle.readline()
print("3rd line : ", file_content)

# seek pointer will be used for read operations
# character based seek
# we can set to any character
my_file_handle.seek(0)  # point to 0th character. Which means beginning of the file
file_content = my_file_handle.readline()
print("1st line : ", file_content)

# Step - 3 : Disconnect
# --------------------------
my_file_handle.close()

print("#" * 40, end="\n\n")
############################


print("Read Operations - 4) readlines/list/tuple/set/dict")
print("-" * 20)
# --------------------------

# Step - 1 : Connect to file
# --------------------------
my_file_handle = open('../real_time_programs/my_out_file.txt', 'r')

# Step - 2 : Read
# --------------------------

# 1
file_content = my_file_handle.readlines()
# return complete file content in list
print("file_content using readlines : ", file_content)
# seek pointer reached EOF

# 2
my_file_handle.seek(0)
file_content = list(my_file_handle)
# return complete file content in list
print("file_content using list : ", file_content)
# seek pointer reached EOF

# 3
my_file_handle.seek(0)
file_content = tuple(my_file_handle)
# return complete file content in tuple
print("file_content using tuple : ", file_content)
# seek pointer reached EOF

# 4
my_file_handle.seek(0)
file_content = set(my_file_handle)
# return complete file content in set
print("file_content using set : ", file_content)
# seek pointer reached EOF

# 5
my_file_handle.seek(0)
file_content = dict(enumerate(my_file_handle))
# return complete file content in dict
print("file_content using dict : ", file_content)

# Step - 3 : Disconnect
# --------------------------
my_file_handle.close()

print("#" * 40, end="\n\n")
############################


# --------------------------
# Modes
# --------------------------
# mode 'w' : 1) Write Only 2) Create new file 3) Erase the content of the file
# mode 'r' : 1) Read Only 2) It will not create new file if not present
# mode 'a' : 1) Append Only 2) It will create new file if file not present
# mode 'w+' : 1) RW 2) Create new file 3) Erase the content of the file
# mode 'r+' : 1) RW 2) It will not create new file if not present
# mode 'a+' : 1) RW 2) It will create new file if file not present
# --------------------------

# COMMENT - 1
# --------------------------
# >>> # 1-way to convert to dictionary
# >>> L = [100, 200, 300]
# >>> dict(L)
# Traceback (most recent call last):
#   File "<pyshell#56>", line 1, in <module>
#     dict(L)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
# >>>
# >>> # Make index & value pair
# >>> M = [(0, 100), (1,200), (2,300)]
# >>> dict(M)
# {0: 100, 1: 200, 2: 300}
# >>>
# >>> # To make pair, we can use enumerate function
# >>> # To make pair, we can use enumerate function
# >>> e = enumerate(L)
# >>> list(e)
# [(0, 100), (1, 200), (2, 300)]
# >>> dict(enumerate(L))
# {0: 100, 1: 200, 2: 300}
# --------------------------
