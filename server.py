from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ="topsecret"

@app.route('/', methods=['GET'])
def counter():
    print( session )
    #session["views"] = 0		# borra todas las claves

    if 'views' in session:
        session["views"] += 1 
    else:
        session["views"] = 0

    return render_template( "show.html", views = session["views"] )

@app.route('/destroy_session', methods=['POST'])
def destroy():
    if 'views' in session:
        session.clear()		# borra todas las claves
    return redirect('/')

@app.route('/add2', methods=['POST'])
def addtwo():
    session["views"] += 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)