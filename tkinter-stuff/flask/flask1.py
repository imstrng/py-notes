from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page       <hr /> (Try:  /hello, /projects, /about)'

# ----------- MORE ROUTING --------------

@app.route('/hello')
def hello():
    return 'Hello World      <hr /> (Try:  /, /projects, /about)'

@app.route('/projects')
def projects():
    return 'The project page <hr /> (Try: /, /hello,  /about)'

@app.route('/about')
def about():
    return 'The about page   <hr /> (Try: /, /hello, /projects)'


# ----------- RUN APP --------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)