"""
2nd program using while loop
"""
print("log_data : ")
print("-" * 20)
# ----------------------

log_data = '''
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
'''

print(log_data)

print("#" * 40, end="\n\n")
###################

print("type of log_data : ")
print("-" * 20)
# ----------------------

print(type(log_data))

print("#" * 40, end="\n\n")
###################

print("Methods inside 'str' class : ")
print("-" * 20)
# ----------------------

print(dir(log_data))

print("#" * 40, end="\n\n")
###################

print("raw string: log_data : ")
print("-" * 20)
# ----------------------

print(repr(log_data))

print("#" * 40, end="\n\n")
###################

print("list of lines: ")
print("-" * 20)
# ----------------------

# >>> log_data = 'line1\nline2\nline3'
# >>> log_data.split('\n')
# ['line1', 'line2', 'line3']
# >>>

list_of_lines = log_data.split("\n")
print(list_of_lines)

print("#" * 40, end="\n\n")
###################

print("Extract Info ")
print("-" * 20)
# ----------------------

line_no = 0
while line_no < len(list_of_lines):
    if list_of_lines[line_no].startswith('123'):
        sp = list_of_lines[line_no].split()  # split by space

        ip = sp[0]

        raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
        index_of_first_colon = raw_date.index(':')
        dt = raw_date[1:index_of_first_colon]

        image = sp[6]
        # if image.endswith('jpg') or image.endswith('png') or image.endswith('gif')
        if image.startswith('/pics/'):
            image = image.split('/')
            image = image[2]
        else:
            image = "No Image"
        raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url.strip('"')  # strip double quotes : ["]

        print(ip, dt, image, url)
    line_no = line_no + 1

# for each_line in list_of_lines:
#     if each_line.startswith('123'):
#         # Below code is copied from program_1
#         sp = each_line.split()  # split by space
#
#         ip = sp[0]
#
#         raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
#         index_of_first_colon = raw_date.index(':')
#         dt = raw_date[1:index_of_first_colon]
#
#         image = sp[6]
#         # if image.endswith('jpg') or image.endswith('png') or image.endswith('gif')
#         if image.startswith('/pics/'):
#             image = image.split('/')
#             image = image[2]
#         else:
#             image = "No Image"
#         raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
#         url = raw_url.strip('"')  # strip double quotes : ["]
#
#         print(ip, dt, image, url)

print("#" * 40, end="\n\n")
###################
