"""
About print function
"""

print("print function PART-1 ")
print("-"*20)
# ------------------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # default sep="SPACE" : print each value with space separated
print(a, b, c, d, sep=',') # print each value with comma separated
print(a, b, c, d, sep="|") # print each value with pipe separated
print(a, b, c, d, sep="XYZ") # print each value with XYZ separated

print("#"*40, end='\n\n')
####################

print("print function PART-2 ")
print("-"*20)
# ------------------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # default end='\n'. After printing all values, put \n at the end
print(a, b, c, d, end='.') # After printing all values, put . at the end
print(a, b, c, d, end='|') # After printing all values, put | at the end
print(a, b, c, d, end='XYZ') # After printing all values, put XYZ at the end
print(a, b, c, d) # default end='\n'. After printing all values, put \n at the end

# TOtally we can pass 4 arguments to print function
# 1) sep 2) end 3) file 4) flush
# file & flush will be discussed during file operations

print("#"*40, end='\n\n')
####################
