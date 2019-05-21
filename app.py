from flask import Flask, render_template, redirect, request

app = Flask(__name__)

get_counter = 0
post_counter = 0


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/request_counter', methods=['GET, POST'])
def request_counter():
    if request.method == 'GET':
        get_counter += 1
        return redirect('/')
    else:
        post_counter += 1

    return redirect('/')


@app.route('/statistics')
def request_statistics():
    return render_template('statistics.html', get_counter=get_counter, post_counter=post_counter)


if __name__ == '__main__':
    app.run(
        debug=True
    )
