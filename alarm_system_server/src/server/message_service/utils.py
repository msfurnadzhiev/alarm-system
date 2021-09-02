import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailService:

  def __init__(self):
    self.password = 'Ftt00Y2YjU'
    self.message = MIMEMultipart("alternative")

  def send(self, mail):
    
    if mail.sender.role == "admin":

      # Turn these into MIMEText objects
      self.message["Subject"] = mail.subject
      self.message["From"] = mail.sender.email
      self.message["To"] = mail.receiver.email
      self.message.attach(MIMEText(mail.message, "html"))

      # Create secure connection with server and send email
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: #465
          server.login(self.message["From"], self.password)
          server.sendmail(
              self.message["From"], self.message["To"], self.message.as_string()
          )