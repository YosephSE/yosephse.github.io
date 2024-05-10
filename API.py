from flask import Flask, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'BGPHMS@gmail.com'
app.config['MAIL_PASSWORD'] = 'vjkcslwthvdgerod'

mail = Mail(app)


@app.route('/msg', methods=['POST'])
def msg():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    email_message = f"""
    <html>
        <head></head>
        <body>
            <h2>Client request</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Message:</strong><br/>{message}</p>
        </body>
    </html>
    """
    
    msg = Message(subject="Client request",
                  recipients=['yoseph.kedir10@gmail.com', email],
                  sender=app.config.get("MAIL_USERNAME"))
    msg.html = email_message
    mail.send(msg)
    return redirect("http://localhost:5500/build")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
