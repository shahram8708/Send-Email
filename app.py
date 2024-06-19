from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emails')
def emails():
    return render_template('emails.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    
    smtp_server = data['smtp_server']
    smtp_port = data['smtp_port']
    smtp_username = data['smtp_username']
    smtp_password = data['smtp_password']
    from_email = data['from']
    to_email = data['to']
    subject = data['subject']
    body = data['body']

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        return jsonify({'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'message': 'Failed to send email', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
