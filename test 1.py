# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:19:14 2021

@author: Azar
"""

import cx_Oracle
import pandas as pd

def sq_input(query):
    dsn_tns = cx_Oracle.makedsn('192.168.56.101', '1521', service_name='orcl') 
    conn = cx_Oracle.connect(user='system', password='oracle', dsn=dsn_tns) 
    sql_query=query
    db_dtls = pd.read_sql(sql_query, con=conn)
    row_val = db_dtls.to_json(orient="records",date_format="iso")
    col_nam=[]
    for a ,b in db_dtls.iteritems():
        col_nam.append(a)
    column_name=col_nam
    return column_name,row_val

a,b=sq_input('select * from  emp')
print(a)
print(1)
print(b)
"""db_dtls = db_dtls.to_json(orient="records")"""
    