"""from flask import Flask ,render_template"""
import cx_Oracle
import pandas as pd
import json

"""app=Flask(__name__)"""

dsn_tns = cx_Oracle.makedsn('192.168.56.101', '1521', service_name='orcl') 
conn = cx_Oracle.connect(user='system', password='oracle', dsn=dsn_tns) 
cur = conn.cursor()
cur.execute('select json_object(id,name,emp_no) from emp order by id')
data=cur.fetchall()
#connecting to Oracle
"""dsn_tns = cx_Oracle.makedsn(ora_host, ora_port, ora_db)
ora_cnxn = cx_Oracle.connect(ora_user, ora_pwd, dsn_tns)"""
    #ends here
    #getting result as df
"""query='select id,name,emp_no,date_to from emp order by id'
db_dtls = pd.read_sql(query, con=conn)
db_dtls = db_dtls.to_json(orient="records")
my_Df=pd.DataFrame(data,columns=cur.col_names)"""


"""cur = conn.cursor()
    cur.execute('select Json_object(id,name,emp_no,date_to) from emp order by id ')
    data=cur.fetchall()"""
 """dsn_tns = cx_Oracle.makedsn('192.168.56.101', '1521', service_name='orcl') 
    conn = cx_Oracle.connect(user='system', password='oracle', dsn=dsn_tns) 
    query='select * from emp order by id'
    db_dtls = pd.read_sql(query, con=conn)
    row_val = db_dtls.to_json(orient="records",date_format="iso")
    col_nam=[]
    for a ,b in db_dtls.iteritems():
        col_nam.append(a)
    df_json_col=col_nam"""
    
list1=[]
for a in data:
	for b in a:
		list1.append(json.loads(b))
df=pd.DataFrame(list1)
df_json=df.to_json(orient='records')
print(df_json)
print(type(df_json))

list_key=[]
list_value=[]
for key,value in df.items():
	list_key.append(key)
	list_value.append(df[key].to_string(index=False))

"""list1=[]
    list_key=[]
    for a in data:  
    	for b in a:
    		list1.append(json.loads(b))
    df=pd.DataFrame(list1)
    df_json=df.to_json(orient='records') 
    for key,value in df.items():
        list_key.append(key)
    df_json_col=list_key"""
"""

@app.route('/')
def home():
	return render_template('home.html')  
@app.route('/table.html')
def table():
list_key=[]
list_value=[]
for key,value in df.items():
	list_key.append(key)
	list_value.append(df[key].to_string(index=False))
print('{} {}'.format(list_key,list_value))
return render_template('table.html',x=list_key,y=list_value)
app.run()"""