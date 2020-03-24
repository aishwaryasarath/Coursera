#! python3
import os
#import requests

filenames = []
path = os.chdir(r"C:\Users\aishw\PycharmProjects\PythonED2\course6\project2\data\feedback")
#print(os.listdir())
filenames = os.listdir()
#print(filenames)
return_json = {}
ret_list = []
for file in filenames:
    #print("here")
    with open(file) as fp:
        for i, line in enumerate(fp):
            #print(i,line)
            if i == 0:
                return_json['title']=line.strip()
            elif i == 1:
                return_json['name'] = line.strip()
            elif i == 2:
                return_json['date'] = line.strip()
            elif i == 3:
                return_json['feedback'] = line.strip()
        #print(return_json)
        
        #ret_list.append(return_json)

#print(ret_list)

