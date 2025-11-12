from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="exampleuser",
            password="change_this_strong_password",
            database="exampledb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        html = """<!DOCTYPE html>
<html>
<head>
    <title>LEMP-palvelin</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding-top: 50px;
        }}
        h1 {{
            color: #2c3e50;
        }}
        p {{
            color: #555;
        }}
    </style>
</head>
<body>
    <h1>Tervetuloa LEMP-palvelimelle!</h1>
    <p>Palvelimen kellonaika (SQL): <strong>{time}</strong></p>
    <p>Rakennettu Flaskilla, Gunicornilla ja Nginxillä 🚀</p>
</body>
</html>"""

        return html.format(time=result[0])
    except Exception as e:
        return f"<h1>Virhe: {e}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
