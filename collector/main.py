from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Please send to /track/<pagename>\n"

@app.route("/track/<pagename>", methods=['GET', 'POST'])
def track(pagename):
    print request.method
    print request.get_data()
    #print repr(request)
    return "received at /track.\n"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
