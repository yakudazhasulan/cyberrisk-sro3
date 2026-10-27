import os

from flask import Flask, render_template_string
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="kk">
<head>
    <meta charset="UTF-8">
    <title>CyberRisk - PostgreSQL</title>
    <style>
        body {
            background: #101827;
            color: white;
            font-family: Arial, sans-serif;
            padding: 40px;
            text-align: center;
        }
        h1 { color: #38bdf8; }
        table {
            margin: 30px auto;
            border-collapse: collapse;
            width: 85%;
        }
        th, td {
            border: 1px solid #475569;
            padding: 14px;
        }
        th { background: #1e40af; }
        tr:nth-child(even) { background: #1e293b; }
    </style>
</head>
<body>
    <h1>CyberRisk - SRO 3</h1>
    <h2>2-команда | PostgreSQL</h2>
    <p>Docker Compose + Flask + PostgreSQL</p>

    <table>
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Role</th>
            <th>Email</th>
        </tr>
        {% for user in users %}
        <tr>
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.role }}</td>
            <td>{{ user.email }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def index():
    connection = psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

    try:
        with connection.cursor(
            cursor_factory=RealDictCursor
        ) as cursor:
            cursor.execute(
                "SELECT id, username, role, email "
                "FROM users ORDER BY id"
            )
            users = cursor.fetchall()
    finally:
        connection.close()

    return render_template_string(HTML, users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)