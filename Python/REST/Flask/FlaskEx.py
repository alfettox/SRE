from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<body><h1> Title</h1><h3>Subtitle</h3><p>This is a paragraph. I'm writing live. Is it true</p><ul></body>"


app.run()

if __name__ == '__main__':
    app.run(debug=True)
