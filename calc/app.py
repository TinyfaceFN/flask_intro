from flask import Flask, request
import operations
app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.add(a,b))

@app.route('/sub')
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.sub(a,b))

@app.route('/mult')
def mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.mult(a, b))

@app.route('/div')
def div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.div(a, b))

maths = {
    'add': operations.add,
    'sub':operations.sub,
    'mult':operations.mult,
    'div':operations.div
}
@app.route('/math/<math>')
def do_math(math):
      a = int(request.args.get('a'))
      b = int(request.args.get('b'))
      return str(maths[math](a,b))
      