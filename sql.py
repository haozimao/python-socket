#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pymysql


def sqlread(): #sql读取
  msg=[]
  db = pymysql.connect("127.0.0.1","root","hu19950615","world" )
  cursor = db.cursor()
  i=0
  sql="SELECT * FROM city  WHERE Name>'%s' "%(100)
  try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
         i=1+i
         fname =str( row[0])
         lname = row[1]
         coder=row[2]
         msg.append(fname+'\t'+lname+'\t'+coder+'\n')
  except :
        print("no people")


  #text("money", msg)
  cursor.close()
  db.close()


def text(name,msg):#写入text
    my_path="D:\\test\\"
    filename=my_path+name+'.txt'
    file=open(filename,'w')
    for i in msg:
     file.write(i)
    file.close()

def readvar ():
    db = pymysql.connect("127.0.0.1", "root", "密码", "world")
    cursor = db.cursor()

def creatsql():
    db = pymysql.connect("127.0.0.1", "root", "密码", "world")
    cursor = db.cursor()

    sql = """CREATE TABLE name (
             FNAME  CHAR(20) NOT NULL,
             LNAME CHAR(20),
             MONEY INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    try:
      cursor.execute(sql)
    except:
      print("no")
    db.close()
    cursor.close()

def writesql(fname,lname,age):
    db=pymysql.connect("127.0.0.1", "root", "hu19950615", "world")
    cursor=db.cursor()
    sql = "INSERT INTO sqlstu_company(full_name, address,tel) \
           VALUES ( '%s','%s','%s' )" % \
          (fname, lname,age)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("no")
    db.close()
    cursor.close()

