from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('copia.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')

if __name__ == '__main__':
    app.run(debug=True)
