from models.user import UserBuilder
from models.mail import MailBuilder

ub = UserBuilder()

ub.role("admin") \
  .name("Alarm System Team") \
  .email("alarmsystem.su.fmi@gmail.com")

admin = ub.get()


ub.role("user") \
  .username("dnaidenov") \
  .name("Dimitar","Naidenov") \
  .email("msfurnadzhiev@gmail.com")

user = ub.get()


mb = MailBuilder()

mb.sender(admin) \
  .receiver(user) \
  .subject("Possible problem with your property") \
  .message( f""" \
        <html>
        <body>
            <p>Dear {mb.get().receiver.name},<br><br>
            We want to inform you about a possible problem in your property! <br>
            Please check if everything is ok as soon as possible.<br><br>
            Best Regards,<br>
            {mb.get().sender.name}
            </p>
        </body>
        </html>
        """)

mail = mb.get()