from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'k'

if __name__ == '__main__':
    app.run()