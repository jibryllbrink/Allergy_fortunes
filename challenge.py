from flask import Flask
app = Flask(__name__)

@app.route('/double')
def double2():
    the_number = request.args.get('number')
    the_number =
    return str(any_number *2)