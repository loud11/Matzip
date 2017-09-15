import hashlib
import os
import datetime

def file_hashing(file_name_list): # ex) file_name_list = ['C:/test/test1.txt', 'C:/test/test2.txt']
    file_hashed_list = []

    for file_name in file_name_list:
        with open(file_name,'r',encoding='utf-8') as file_to_check:
            data = file_to_check.read().encode('utf-8')
            file_hashed_list.append([hashlib.md5(data).hexdigest(),hashlib.sha1(data).hexdigest()])
            file_to_check.close()
    return file_hashed_list

def file_MAC_time(file_name_list):
    #file_MAC_time = []
    for file_name in file_name_list:
        file_stat = os.stat(file_name)
        print(file_name)
        print("MODIFY Time : " , datetime.datetime.fromtimestamp(file_stat.st_mtime))
        print("ACCESS Time : " , datetime.datetime.fromtimestamp(file_stat.st_atime))
        print("Create Time : " , datetime.datetime.fromtimestamp(file_stat.st_ctime))
        print("File size : " , file_stat.st_size , "B")
        #file_MAC_time.append(os.stat(file_name))

def is_file_bad_signature(file_name_list):
    for file_name in file_name_list:
        with open(file_name, "rb") as f:
            byte = f.read(1)
            while len(byte) is not 0 :
                print('%02X' % int(ord(byte)),end=' ')
                # Do stuff with byte.
                byte = f.read(1)
            f.close()

file_name_list = ['C:/testforproject/test.txt']
file_MAC_time(file_name_list)
is_file_bad_signature(file_name_list)
