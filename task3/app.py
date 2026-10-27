import os

from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="kk">
<head>
    <meta charset="UTF-8">
    <title>CyberRisk - MySQL</title>
    <style>
        body {
            background: #101827;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        h1 { color: #38bdf8; }
        table {
            margin: 30px auto;
            border-collapse: collapse;
            width: 90%;
        }
        th, td {
            border: 1px solid #475569;
            padding: 14px;
        }
        th { background: #1e40af; }
        tr:nth-child(even) { background: #1e293b; }
        .High, .Critical { color: #f87171; }
        .Medium { color: #facc15; }
        .Low { color: #4ade80; }
    </style>
</head>
<body>
    <h1>CyberRisk - SRO 3</h1>
    <h2>2-команда | MySQL</h2>
    <p>Docker Compose + Flask + MySQL</p>

    <table>
        <tr>
            <th>ID</th>
            <th>Event Type</th>
            <th>Severity</th>
            <th>Description</th>
        </tr>
        {% for event in events %}
        <tr>
            <td>{{ event.id }}</td>
            <td>{{ event.event_type }}</td>
            <td class="{{ event.severity }}">
                {{ event.severity }}
            </td>
            <td>{{ event.description }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def index():
    connection = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

    try:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id, event_type, severity, description "
                "FROM security_events ORDER BY id"
            )
            events = cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()

    return render_template_string(HTML, events=events)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)