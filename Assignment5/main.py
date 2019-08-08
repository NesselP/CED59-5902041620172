<<<<<<< HEAD
from flask import  Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Register.html')

@app.route('/',methods=["post"])
def register():
    return 'xyz' ;

if __name__ == '__main__':
    app.run()
=======
from flask import  Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run()



>>>>>>> 62eb13fb99fcf3f9b1c3431a9d556209f24e929b
