from flask import Flask
from flask_mail import Mail, Message
import os


app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465

user_name = "AxelFlaskblog@gmail.com"

print(user_name)
app.config['MAIL_USERNAME'] =  user_name

pwd = "Passw0rd7700"
print(pwd)
app.config['MAIL_PASSWORD'] = pwd


app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    msg = Message('This is a test message', sender = user_name, recipients = ['Axel@gmail.com'])
    msg.body = "This is a test"
    mail.send(msg)
    return("Sent")


if __name__ == '__main__':
   app.run(debug = True)
