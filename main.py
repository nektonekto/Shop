from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'kak'

if __name__ == '__main__':
    app.run()