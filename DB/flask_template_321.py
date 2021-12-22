from flask import Flask
from flask import request, make_response, redirect, abort, render_template
import psycopg2
app = Flask(__name__)

def view():
    con = psycopg2.connect(dbname='web_basa', user='postgres', password='1111', host='localhost')
    bs = con.cursor()
    bs.execute("SELECT * FROM users;")
    data = bs.fetchall()
    con.commit()
    con.close()
    return data

def insert(name, surname):
    con = psycopg2.connect(dbname='web_basa', user='postgres', password='1111', host='localhost')
    bs = con.cursor()
    bs.execute(f"INSERT INTO users(nam, sur) VALUES ('{name}', '{surname}');")
    con.commit()
    con.close()

def edit(mode, ind, ed_name, ed_surname):
    con = psycopg2.connect(dbname='web_basa', user='postgres', password='1111', host='localhost')
    bs = con.cursor()
    if mode == 'cg_name':
        bs.execute(f"UPDATE users SET nam = '{ed_name}' WHERE id = {ind}")
    elif mode == 'cg_surname':
        bs.execute(f"UPDATE users SET sur = '{ed_surname}' WHERE id = {ind}")
    elif mode == 'cg_both':
        bs.execute(f"UPDATE users SET nam = '{ed_name}', sur = '{ed_surname}' WHERE id = {ind}")
    con.commit()
    con.close()

@app.route('/', methods=['post', 'get'])
def index():
    mes = ''
    name = ''
    surname = ''
    mode = 'entry'
    change = 'cg_name'
    ed_name = ''
    ed_surname = ''
    req = request
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        mode = request.form.get('mode')
        change = request.form.get('ch_data')
        ed_name = request.form.get('change_nm')
        ed_surname = request.form.get('change_snm')
    if mode == 'entry':
        if name != '' and surname != '':
            insert(name, surname)
        else:
            mes = 'You must fill both inputs'
    elif mode == 'edit':
        if name != '' and surname != '':
            ind = ''
            for row in view():
                if row[1] == name and row[2] == surname:
                    ind = row[0]
            if change == 'cg_name':
                if ed_name != '':
                    edit(change, ind, ed_name, ed_surname)
                else:
                    mes = 'Entry editing name'
            elif change == 'cg_surname':
                if ed_surname != '':
                    edit(change, ind, ed_name, ed_surname)
                else:
                    mes = 'Entry editing surname'
            elif change == 'cg_both':
                if ed_name != '' and ed_surname != '':
                    edit(change, ind, ed_name, ed_surname)
                else:
                    mes = 'Entry editing name and editing surname'
        else:
            mes = 'You must fill both inputs'
    users = view()
    return render_template('index.html', users_list=users, message=mes)

if __name__ == '__main__':
    app.run(debug=True)