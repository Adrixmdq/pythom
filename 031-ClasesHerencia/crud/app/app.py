from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
   return render_template('login.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # renderizo las DOS RUTASA usando plantillas dentro de template
    # renderizo un template que se llama  hola.html, con los datos que le mante
    # que pueden ser datos de una base de datos se hace por medio de JINJA
    return render_template('hola.html', person=name)

@app.route('/create/<first_name>/<last_name>')
# http://127.0.0.1:5000/create/adrian/recio
def create(first_name=None, last_name=None):
  return 'Hello ' + first_name + ',' + last_name


@app.route('/dashboard/<name>')
def dashboard(name):
   return 'Te logeaste papa!! %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    # Un redirect por post
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)
