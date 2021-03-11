from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Is it Sunny or not!"