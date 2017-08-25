from flask import Flask, request,redirect, url_for,render_template
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def calc():
  if request.method == 'POST':
    num=request.form['enternumber']

    calcu=eval(num)
    return render_template('calc.html', calcu=calcu)
  return render_template('calc.html')
  
if __name__ == '__main__':
   app.run(debug = True)  