"""
Write a function for processing server log and return extracted info
"""


def log_process_func_pos_args(log_file_path):
    """
    Function to process server log data and returns extracted data
    :param log_file_path:
    :return list of tuples:
    [(ip, dt, pics, url), (ip, dt, pics, url),(ip, dt, pics, url),]
    """

    # --------------------------
    my_file_handle = open(log_file_path, 'r')
    list_of_lines = my_file_handle.readlines()
    my_file_handle.close()
    # --------------------------
    final_result = []
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

            each_line_tuple = (ip, dt, image, url)
            final_result.append(each_line_tuple)
    return final_result


def log_process_func_kw_args(*, log_file_path):
    """
    Function to process server log data and returns extracted data
    :param log_file_path:
    :return list of tuples:
    [(ip, dt, pics, url), (ip, dt, pics, url),(ip, dt, pics, url),]
    """

    # --------------------------
    my_file_handle = open(log_file_path, 'r')
    list_of_lines = my_file_handle.readlines()
    my_file_handle.close()
    # --------------------------
    final_result = []
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

            each_line_tuple = (ip, dt, image, url)
            final_result.append(each_line_tuple)
    return final_result


# Calling functions
func_1_result = log_process_func_pos_args("../log/server_log.txt")
print("func_1_result : ", func_1_result)

func_2_result = log_process_func_kw_args(log_file_path="../log/server_log.txt")
print("func_2_result : ", func_2_result)
