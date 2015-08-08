from flask import Flask, render_template, request, redirect, url_for, abort, session, make_response

app = Flask(__name__)
app.config.from_pyfile('Config.cfg', silent=False)

@app.route('/Hello')
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/Index')
@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/Happening', methods=['GET','POST'])
@app.route('/happening', methods=['GET','POST'])
def the_happening():
    top=295
    try:
        if request.form['offset'] is not None:
            top-=int(request.form['offset'])*28
    except Exception:
        print Exception
    left=450
    return render_template('happening.html', arrowtop=top, arrowleft=left, title="WTF is Happening?")

if __name__ == '__main__':
    app.run()
#    app.run(debug=True, host='0.0.0.0.', port=5555)

