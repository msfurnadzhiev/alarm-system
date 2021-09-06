from django import http

# Cross Site Request Forgery protection
from django.views.decorators.csrf import csrf_exempt 

from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin

allowed_methods = ['GET']
required_params = ['name', 'email']

from .admin import admin
from .models import *
from .utils import MailService
from .tables import RecordsTable


def check_for_required_params(request):
    for param in required_params:
        if request.GET.get(param) is None:
            return False
    return True


def get_user_data(request):
    if check_for_required_params(request):
        receiver = UserBuilder()
        receiver.role("user") \
                .name(request.GET['name']) \
                .email(request.GET['email'])
        return receiver.get()
    return None


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

    sender = admin.adminUser.get()
    receiver = get_user_data(request)
   
    if request.method in allowed_methods and receiver is not None: 
        mail = create_email(sender, receiver)
        ms = MailService()
        ms.send(mail)

        Record.create(receiver)
        return http.HttpResponse(status=200)

    return http.HttpResponseBadRequest('Bad Request')



class RecordsTableView(ExportMixin, SingleTableView):
    model = Record
    table_class = RecordsTable
    template_name = 'logpage.html'