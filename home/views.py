from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1> Hello World </h1>')
    response.write('Wellcome to app home')
    return response