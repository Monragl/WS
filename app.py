from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Приветмир!"
 app.run(port="9999")
