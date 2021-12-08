from django.http import HttpResponse
from django.shortcuts import render


from chat.models import Message



def page(request):
    take_sms = Message.objects.order_by('-id')
    return render(request, './index.html', {'take_sms':take_sms})

    # return HttpResponse(f'{take_sms}')
