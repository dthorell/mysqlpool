import mysql.connector
from flask import Flask, abort, jsonify
from flask_mysqlpool import MySQLPool


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = "test"
app.config["MYSQL_PASS"] = "test"
app.config["MYSQL_DB"] = "world_x"
app.config["MYSQL_POOL_NAME"] = "mysql_pool"
app.config["MYSQL_POOL_SIZE"] = 5
app.config["MYSQL_AUTOCOMMIT"] = True

db = MySQLPool(app)


@app.route("/")
def index():
    try:
        conn = db.connection.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from world_x.city limit 10")
        result = cursor.fetchall()
        conn.close()
    except mysql.connector.ProgrammingError as err:
        print(err)
        abort(500)
    except mysql.connector.errors.PoolError as err:
        print(err)
        abort(500)
    return jsonify(result)
