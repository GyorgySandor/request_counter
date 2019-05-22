from flask import Flask, render_template, redirect, request

app = Flask(__name__)




@app.route('/')
@app.route('/index')
def home_page():
    return render_template('index.html')


@app.route('/request_counter', methods=['GET', 'POST'])
def request_counter():
    if request.method == 'POST':
        print("POST")
        return redirect('/index')
    print("GET")
    return redirect('/index')


@app.route('/statistics')
def request_statistics():
    return render_template('statistics.html')


if __name__ == '__main__':
    app.run(
        debug=True
    )
