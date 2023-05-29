from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>/<password>')
def success(name, password):
   # a = 'welcome %s' % name, 'u re %s' % password
   return 'welcome {}, your password is {}'.format(name, password)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
        user = request.form['nm']
        user_password = request.form['pswd']
        return redirect(url_for('success',name = user, password  = user_password))
   else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
 app.run()
