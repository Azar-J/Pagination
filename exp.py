from flask import Flask ,render_template
import cx_Oracle
import pandas as pd

app=Flask(__name__)


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



#@app.route('/')
#def home():
#	return render_template('home.html')

@app.route('/table.html')
def table():
    query="""select * from emp
    order by id"""
    a,b=sq_input(query)
    #print(a)
    #print(b)
    return render_template('table.html',b=b)
        

app.run()

""""if __name__ == '__exp__':
    app.run(host='127.0.0.1', port='5000', debug= True)"""