from flask import Flask, render_template, request
#Flask extension of the Transpiler
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index(result=None):
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
