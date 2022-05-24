from flask import Flask, redirect
gapp = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('success')

@app.route('/success')
def success():
    return 'this is so successful, blah blah test test'

if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)