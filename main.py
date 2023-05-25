from flask import Flask, url_for, request
# from markupsafe import escape
from faker import Faker
import csv
import statistics
import requests


app = Flask(__name__)


@app.route("/")
def index():
    return f"""
    <a href="{url_for('requirements')}">Requirements</a><br>
    <a href="{url_for('generate_users')}">Users</a><br>
    <a href="{url_for('mean')}">Mean</a><br>
    <a href="{url_for('space')}">Space</a><br>
    """


@app.route("/requirements/")
def requirements():
    with open('requirements.txt', 'r') as file:
        lines = file.readlines()
        data = "<br>".join(lines)
    file.close()
    return f"""
    <a href="{url_for('index')}">Index</a><br>
    {data}
    """


@app.route("/generate_users/")
def generate_users():
    qty = request.args.get('count', 100, type=int)
    fake = Faker()
    user_list = []
    for user in range(qty):
        username = fake.name()
        mail = username.split(' ')
        company = fake.company().split(' ')
        user_list.append(f'user: {username} - {str(mail[0])[0].lower()}.{str(mail[1]).lower()}'
                         f'@{str(company[0]).lower()}.com')

    return f"""
    <a href="{url_for('index')}">Index</a><br>
    {"<br>".join(user_list)}
    """


@app.route("/mean/")
def mean():
    weight = []
    height = []
    with open('hw.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar=',')
        next(reader)
        for row in reader:
            if row:
                height.append(float(row[1]))
                weight.append(float(row[2]))
        return f"""
            <a href="{url_for('index')}">Index</a><br>
            Average height is: {statistics.mean(height) * 2.54} cm<br>
            Average weight is: {statistics.mean(height) * 0.45359237} kgs
            """


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    answer = r.json().get('number')
    return f"""
            <a href="{url_for('index')}">Index</a><br>
            Currently there are {answer} astronauts
            """


@app.route('/urls/')
def urls():
    return url_for('index')


if __name__ == "__main__":
    app.run()
