from flask import Flask, request, make_response, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "API_MYSQL"

mysql = MySQL(app)

@app.route("/karyawan", methods=["GET", "POST"])
def karyawan():
    try:
        myCursor = mysql.connection.cursor()
        if request.method == "GET":
            myCursor.execute("SELECT * FROM karyawan")
            row_header = [x[0] for x in myCursor.description]
            results = myCursor.fetchall()
            data = []
            for result in results:
                data.append(dict(zip(row_header, result)))

        if request.method == "POST":
            nama = request.json["nama"]
            pekerjaan = request.json["pekerjaan"]
            umur = request.json["umur"]

            myCursor.execute("INSERT INTO karyawan (nama, pekerjaan, umur) VALUES (%s,%s,%s)", (nama, pekerjaan, umur))
            mysql.connection.commit()

            data = {
                "code" : 200,
                "status" : "OK",
                "data" : {
                    "nama" : nama,
                    "pekerjaan" : pekerjaan,
                    "umur" : umur
                }
            }
    
    except Exception as e:
        return make_response(jsonify({'error' : str(e)}), 400)
    return make_response(jsonify(data), 200)

@app.route("/karyawan/<id>", methods=["GET", "PUT", "DELETE"])
def karyawan_id(id):
    try:
        myCursor = mysql.connection.cursor()
        if request.method == "GET":
            myCursor.execute("SELECT * FROM karyawan WHERE id = %s", (id,))
            row_header = [x[0] for x in myCursor.description]
            results = myCursor.fetchall()
            data = []
            for result in results:
                data.append(dict(zip(row_header, result)))

        if request.method == "PUT":
            nama = request.json["nama"]
            pekerjaan = request.json["pekerjaan"]
            usia = request.json["usia"]

            myCursor.execute("UPDATE karyawan SET nama = %s, pekerjaan = %s, usia = %s WHERE id = %s", (nama, pekerjaan, usia, id))
            mysql.connection.commit()

            data = {
                "code" : 200,
                "status" : "OK",
                "data" : {
                    "id" : id,
                    "nama" : nama,
                    "pekerjaan" : pekerjaan,
                    "usia" : usia
                }
            }

        if request.method == "DELETE":
            myCursor.execute("DELETE FROM karyawan WHERE id = %s", (id,))
            mysql.connection.commit()

            data = {
                "code" : 200,
                "status" : "OK"
            }

    except Exception as e:
        return make_response(jsonify({"error" : str(e)}), 400)
    return make_response(jsonify(data), 200)

app.run(debug=True)