from models.user import User

class Mail:

    def __init__(self):
        self.sender = User()
        self.receiver = User()
        self.subject = ""
        self.message = ""

    def print(self):
        print(f'From: {self.sender.email}')
        print(f'To: {self.receiver.email}')
        print(f'Subject: {self.subject}')
        print(f'Message: {self.message}')


class MailBuilder:

    def __init__(self):
        self.mail = Mail()

    def get(self):
        return self.mail

    def sender(self, sender):
        self.mail.sender = sender
        return self

    def receiver(self, receiver):
        self.mail.receiver = receiver
        return self

    def subject(self, subject):
        self.mail.subject = subject
        return self

    def message(self, message):
        self.mail.message = message
        return self
