from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Connect to the SQL Server database
server = 'IUMSDemo'
database = 'IPE_LIVE_TEST'
username = 'iweb'
password = 'passwd@1'
user_id_p = "768"
period_id_p = "10680"
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = conn.cursor()

# Route to fetch data from the database
@app.route("/data")
def data():
    # response = cursor.execute("select * from m_user")
    #cursor.execute("EXEC GetTeacherTimetable @PeriodID=" + period_id_p + ",@UserID=" + user_id_p + "")
    sql = "EXEC GetTeacherTimetable @PeriodID=" + period_id_p + ",@UserID=" + user_id_p + ""
    values = (user_id_p, period_id_p)
    cursor.execute(sql,values)
    
    print(sql)
    
    # cursor.execute("exec GetTeacherTimetable @PeriodID=10680,@UserID=768,@P_interval=0,@P_ALL=NULL,@P_DEGREE_TYPE=9")
    rows = cursor.fetchall()

    # Convert the data to a list of dictionaries
    data = []
    for row in rows:
        data.append({'column1': row[0], 'column2': row[1], 'column3': row[2]})
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="42536", debug=True) 