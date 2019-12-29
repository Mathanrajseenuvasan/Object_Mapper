from flask import Flask
from service import Request

app = Flask(__name__)


@app.route('/')
def index():
    response = Request.request_url()
    return {"response": response}


@app.route('/condensed')
def condensed():
    data = Request.request_url()
    response = Request.request_data(data)
    return {"response":response}

if __name__ == '__main__':
    app.run(debug=True)
