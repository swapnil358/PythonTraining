"""
from below string extract,
IP
DATE
PICS
URL
and print
"""
print("in_string : ")
print("-"*20)
# ----------------------
in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(in_string)
print("#"*40, end="\n\n")
###################
print("type of in_string : ")
print("-"*20)
# ----------------------
print(type(in_string))
print("#"*40, end="\n\n")
###################
print("Methods inside 'str' class : ")
print("-"*20)
# ----------------------
print(dir(in_string))     #die -> display content
print("#"*40, end="\n\n")
###################
print("rar string: in_string : ")
print("-"*20)
# ----------------------
print(repr(in_string))    #repr -> display raw format means as it is
print("#"*40, end="\n\n")
###################






print("Extract IP - 1 - way ")
print("-"*20)
# ----------------------

ip = in_string[0:15]
print("ip : ", ip)

print("#"*40, end="\n\n")
###################

print("Extract IP - 2 - way ")
print("-"*20)
# ----------------------

index_of_first_space = in_string.index(' ')

ip = in_string[0:index_of_first_space]
print("ip : ", ip)

print("#"*40, end="\n\n")
###################

print("Extract IP - 3 - way ")
print("-"*20)
# ----------------------

sp = in_string.split() # split by space
print(sp)
ip = sp[0]
print("ip : ", ip)

print("#"*40, end="\n\n")
###################







print("Extract DATE - 1 - way ")
print("-"*20)
# ----------------------
index_of_first_sq_bracket = in_string.index('[')
index_of_first_colon = in_string.index(':')
dt = in_string[ index_of_first_sq_bracket + 1 : index_of_first_colon]
print("dt : ", dt)
print("#"*40, end="\n\n")
###################
print("Extract DATE - 2 - way ")
print("-"*20)
# ----------------------
raw_date = sp[3] # '[26/Apr/2000:00:23:48'
index_of_first_colon = raw_date.index(':')
dt = raw_date[1:index_of_first_colon]
print('dt : ', dt)
print("#"*40, end="\n\n")
###################




print("Extract PIC NAME - 1 - way ")
print("-"*20)
# ----------------------
index_of_w = in_string.index('w',)
index_of_f = in_string.index('f',)

pics_name = in_string[index_of_w : index_of_f+1]


print("pics_name : ", pics_name)
print("#"*40, end="\n\n")




print("Extract URL  - 1 - way ")
print("-"*20)
# ----------------------
splt = in_string.split()

print("url : ", splt[10])

print("#"*40, end="\n\n")


