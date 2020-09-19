from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', name='EnKo')


@app.route('/greet', methods=['GET'])
def greet():
    if 'user' in request.args:
        usr = request.args['user']
        return render_template('greet.html', user=usr)
    else:
        render_template(
            'greet.html', user='Send your user name with user in query string')
        # http://127.0.0.1:5000/greet?user=Ahmet seklinde ? arkasindan key value pair gonderebiliyoruz.
        # ikinci birtane gondereceksek araya & koyup yeni key value yu &key=value seklinde yaziyoruz


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        return render_template('secure.html', user=user_name)
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

    # Bu app e heryerden ulasilmasini istiyorsak host a everywhere karsiligi olan 0.0.0.0,
    #  porta http karsiligi olan 80 atanir
    # app.run(host='0.0.0.0', port=80)
