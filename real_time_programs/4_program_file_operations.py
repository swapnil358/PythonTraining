"""
Requirement:
Read data from server_log.txt and extract
IP
DATE
PICS
URL
from each IP address lines
and write extracted info to log_report.txt and log_report.csv
"""

"""
Requirement:
Read data from server_log.txt and extract
IP
DATE
PICS
URL
from each IP address lines
and write extracted info to log_report.txt and log_report.csv
"""

# Split into smaller tasks
# ------------------------
# Task - 1 : Read data from log file and store in a variable
# Task - 2 : create files log_report.txt and log_report.csv and add heading
# Task - 3 : Extract info and write to file
# ------------------------

print("# Task - 1 : Read data from log file and store in a variable")
print("-" * 20)
# ----------------------

# Step - 1 : Connect to file
# --------------------------
my_file_handle = open('../log/server_log.txt', 'r')

# Step - 2 : Read
# --------------------------
list_of_lines = my_file_handle.readlines()

# Step - 3 : Disconnect
# --------------------------
my_file_handle.close()

print(list_of_lines)

print("#" * 40, end="\n\n")
########################

print("# Task - 2 : create files log_report.txt and log_report.csv and add heading")
print("-" * 20)
# ----------------------

# Step - 1 : Connect to file
# --------------------------
my_txt_file_handle = open('log_report.txt', 'w')
my_csv_file_handle = open('log_report.csv', 'w')

# Step - 2 : Write heading # Write : 1) write 2) writelines 3) print
# --------------------------
# txt file
# my_txt_file_handle.write("IP\tDATE\tPICS\tURL\n")
# my_txt_file_handle.writelines(["IP\t", "DATE\t", "PICS\t", "URL\n"])
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle, flush=True)

# csv file
# my_csv_file_handle.write("IP,DATE,PICS,URL\n")
# my_csv_file_handle.writelines(["IP,", "DATE,", "PICS,", "URL\n"])
print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file_handle, flush=True)

print("Done")

print("#" * 40, end="\n\n")
########################

print("# Task - 3 : Extract info and write to file")
print("-" * 20)
# ----------------------

for each_line in list_of_lines:
    if each_line.startswith('123'):
        # Below code is copied from program_1
        sp = each_line.split()  # split by space

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

        print(ip, dt, image, url, sep="\t", file=my_txt_file_handle, flush=True)
        print(ip, dt, image, url, sep=",", file=my_csv_file_handle, flush=True)

my_txt_file_handle.close()
my_csv_file_handle.close()

print("Reports created. Please check log_report.txt & log_report.csv")

print("#" * 40, end="\n\n")
########################
