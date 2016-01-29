from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Please send to /track/<pagename>\n"

@app.route("/track/<pagename>", methods=['GET', 'POST'])
def track(pagename):
    print request.method
    print request.get_data()
    resp = Response("Foo bar baz")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
