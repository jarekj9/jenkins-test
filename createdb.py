#!/usr/bin/env python3

import sqlite3
 
class SQLITE():
  def __init__(self,db_file):
    self.conn = None
    try:
      self.conn = sqlite3.connect(db_file)
      self.c = self.conn.cursor()
    except sqlite3.Error as e:
      print(e)

  def sqlite_cmd(self,sqlite_cmd):
    try: 
      self.c.execute(sqlite_cmd)
    except sqlite3.Error as e:
      print(e)

  def sqlite_select(self,sqlite_cmd):
    try:
      self.c.execute(sqlite_cmd)
      output = [row for row in self.c]
      return(output)
    except sqlite3.Error as e:
      print(e)
    
  def sqlite_close(self):
    try:
      self.conn.commit()
      self.conn.close()
    except sqlite3.Error as e:
      print(e)

 
if __name__ == '__main__':
  sql_create_table1 = """ CREATE TABLE IF NOT EXISTS table1 (
                                      id integer PRIMARY KEY,
                                      date text,
                                      name text
                                  ); """
  sql_insert1 = """ INSERT INTO table1 (id,date,name) VALUES 
                                      (2,'2017-09-02','TEXTTEST')
                                  ; """
  sql_select1 = """ SELECT * from table1; """
  
  base=SQLITE("db1.db")
  base.sqlite_cmd(sql_create_table1)
  base.sqlite_cmd(sql_insert1)
  print(base.sqlite_select(sql_select1))
  base.sqlite_close()
  print("Testing1")
