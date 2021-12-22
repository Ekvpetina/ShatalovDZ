from flask import Flask
from flask import redirect

app = Flask(__name__)

users = [{'username': 'jpetrov', 'name': 'John', 'surname': 'Petrov', 'age': '19'},
         {'username': 'apetrova', 'name': 'Anna', 'surname': 'Petrova', 'age': '22'},
         {'username': 'joganov', 'name': 'Jora', 'surname': 'Oganov', 'age': '18'}]


@app.route('/')
def index2():
    return redirect('/users/')


@app.route('/users/')
def your_users():
    data = ''
    for user in users:
        data += f'<a href = "http://127.0.0.1:5000/users/{user["name"]}" >' + user['name'] + ' ' + user['surname'] + ' ' + user['age'] + '</a>' + '<br>'
    return data


@app.route('/users/<username>')
def return_username(username):
    check = []
    for user in users:
        check.append(user['name'])
    if username in check:
        return f"<h3>user {username} is in list</h3>"
    else:
        return "<h1>404: User Not Found</n>"


if __name__ == '__main__':
    app.run(debug=True)


