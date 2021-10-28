from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *

def async_test(request):

    result=asyncio.run(main())

    print(result)

    return HttpResponse('working')




   



