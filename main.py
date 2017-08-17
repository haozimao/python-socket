#!/usr/bin/python3
import sql
mydata=['',"123","rt"]
# print("name")
# mydata.append(input())
# print("name2")
# mydata.append(input())
# print("name")
# mydata.append(input())
# print("name2")
# mydata.append(input())
# print("name")
# mydata.append(input())
print(mydata)

sql.writesql(mydata[0],mydata[1],mydata[2])

