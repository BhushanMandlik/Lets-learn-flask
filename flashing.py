from flask import *  

app = Flask(__name__)  
app.secret_key = "bhush@n"  
 
@app.route('/')  
def home():  
    return render_template("index.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    error = None;  
    if request.method == "POST":  
        if request.form['email'] == 'bhushanmandlik2001@gmail.com' and request.form['pass'] == '12345':    
            flash("you are successfuly logged in")  
            return redirect(url_for('home'))  
        else:
            error = "invalid login credentials" 
    return render_template('login.html',error=error)  
  
if __name__ == '__main__':  
    app.run(debug = True)