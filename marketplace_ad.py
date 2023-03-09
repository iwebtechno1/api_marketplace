from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

@app.route('/api/stored-procedures', methods=['GET'])
def fetch_stored_procedures():
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=IUMSDemo;"
                          "Database=MARKETPLACE_AD_DATA;"
                          "UID=iweb;"
                          "PWD=passwd@1;")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM [MARKETPLACE_AD_DATA].[dbo].[adv_data$]")
    # stored_procedures = [row[0] for row in cursor.fetchall()]
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    result = []
    for row in rows:
        d = {
            'buttonText': row[0],
            'category': row[1],
            'description': row[2],
            'details': row[3],
            'imagePath': row[4],
            'offerid': row[5],
            'title': row[6],
            'url': row[7]
        }
        result.append(d)
    
    return jsonify({'stored_procedures': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="42536", debug=True) 