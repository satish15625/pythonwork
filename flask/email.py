from flask_mail import Mail, Message
from flask import Flask
 
app = Flask(__name__)
mail = Mail(app)
 
@app.route(“/mail”)
def email():
    msg = Message( “Hello Message”, sender=”satish15625@gmail.com”, recipients=[“cavisson7@gmail.com”])
   mail.send(msg)
