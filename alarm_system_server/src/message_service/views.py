from django import http


def home(request):
    pass

def send_message(request):
    return http.HttpResponse("Succesful Sending of Message", status=200)

def log_page(request):
    return http.HttpResponse("Log Page", status=200)

