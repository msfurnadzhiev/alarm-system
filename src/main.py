from mocks import mail
from services.mail_service import MailService


if __name__ == "__main__":
  ms = MailService()
  mail.print()
  ms.send(mail)