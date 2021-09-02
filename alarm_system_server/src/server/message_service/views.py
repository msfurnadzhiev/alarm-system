from django import http

# Cross Site Request Forgery protection
from django.views.decorators.csrf import csrf_exempt 

allowed_methods = ['POST', 'GET']

from .admin import admin
from .models import UserBuilder, MailBuilder
from .utils import MailService

def get_user_data(request):
    receiver = UserBuilder()
    receiver.role("user") \
            .name(request.POST['name']) \
            .email(request.POST['email'])
    return receiver.get()


def create_email(sender, receiver):
    mb = MailBuilder()
    mb.sender(sender) \
    .receiver(receiver) \
    .subject("Possible problem with your property") \
    .message( f""" \
            <html>
            <body>
                <p>Dear {receiver.name},<br><br>
                We want to inform you about a possible problem in your property! <br>
                Please check if everything is ok as soon as possible.<br><br>
                Best Regards,<br>
                {sender.name}
                </p>
            </body>
            </html>
            """)
    return mb.get()


@csrf_exempt
def send_message(request):

    if request.method in allowed_methods:
        sender = admin.adminUser.get()
        receiver = get_user_data(request)
        mail = create_email(sender, receiver)

        ms = MailService()
        ms.send(mail)

        return http.HttpResponse(status=200)

    return http.HttpResponseBadRequest('Bad Request')



