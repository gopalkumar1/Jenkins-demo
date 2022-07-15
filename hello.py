from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("hello")
    return "hello! everyone"

if __name__ == "__main__":
    app.run('0.0.0.0',9999)
