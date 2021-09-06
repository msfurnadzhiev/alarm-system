from django.db import models
from django.utils import timezone
import datetime
import copy

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


class User:

    def __init__(self):
        self.name = ""
        self.username = ""
        self.email = ""
        self.role = ""


class UserBuilder:

    def __init__(self):
        self.user = User()

    def get(self):
        return copy.deepcopy(self.user)

    def name(self, *args):
        self.user.name = ' '.join(args)
        return self

    def username(self, username):
        self.user.username = username 
        return self

    def email(self, email):
        self.user.email = email
        return self

    def role(self, role):
        self.user.role = role 
        return self


class Record(models.Model):

    userName = models.CharField(max_length=50)
    userEmail = models.CharField(max_length=50)
    datetime = models.DateTimeField()

    @staticmethod
    def create(receiver):
        return Record.objects.create(
            userName = receiver.name,
            userEmail = receiver.email,
            datetime = datetime.datetime.now(tz=timezone.utc)
        )

    @staticmethod
    def remove_all():
        Record.objects.all().delete()