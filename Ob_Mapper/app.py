from flask import Flask
from service import Request
from mapper import instance_b

app = Flask(__name__)


@app.route('/')
def index():
    response = Request.request_url()
    return {"response": response}


@app.route('/condense')
def condense():
    response = {"condense": instance_b.total}
    return response


if __name__ == '__main__':
    app.run(debug=True)
