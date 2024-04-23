import re

search_container="" #searching container in document
search_TMName ="" #search Task Manager in document
mycontainer_list =[]
myTMname_list = []

print("please enter the Task managers output file path")

file_path= input[]
line_number=0

with open(file_path,'r') as TMnames_object:
    for line in TMnames_object:
        line_number +=1
        if search_container in line:
            mycontainer_list1 = line.split("container_")[1]
            mycontainer_list1 = mycontainer_list1.replace('",\n','')
            mycontainer_list.append(mycontainer_list1)
        if search_TMName in line:
            myTMname_list1 = line.split("flink@")[1]
            myTMname_list1 = myTMname_list1[0:30]
            myTMname_list.append(myTMname_list)

TMnames_object.close()

print("please enter the output file path")

file_metricpath = input()

with open(file_metricpath,'w') as TMwrite_object:
    for first_parameters,second_parameters in zip(myTMname_list, mycontainer_list):
        TMwrite_object.write("APM | appname | Individual Nodes |appname"
        +first_parameters+"-TaskManager_"+second_parameters+"|Hardware Resource|CPU|%Busy")

TMwrite_object.close()