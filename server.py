from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counterSession():
    if 'counter' in session:
      session['counter'] += 1
    else:
      session['counter'] = 1
    if 'visits' in session:
      session['visits'] += 1
    else:
      session['visits'] = 1
    return render_template('/index.html') 
    
    
@app.route("/addTwo")
def addTwo():
    session['counter'] += 1
    return redirect('/') 

@app.route("/addNum", methods=["POST"])
def addNum():
    if request.form["num"]!="":
      session['counter'] += int(request.form["num"])-1
    return redirect('/') 

@app.route("/destroySession")
def reset():
    #session.clear()
    session.pop('counter')
    return redirect('/')

if __name__=="__main__":
  app.run(debug=True)