from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from university.models import Departament


def vistaSimple(request, pk):
    try:
        miDepa = Departament.objects.get(pk=pk)
    except Departament.DoesNotExist as e:
        print(e)
        return HttpResponse("No existe")

    # mirquest = request.GET.get('p', 'p no está')
    # ejemplo: http://127.0.0.1:8000/vistaSimple/?p=ejbilweubfiwe%C3%B1bjf%C3%B1i
    # varios parametros ?p=valor%v=1234&z=6789
    return HttpResponse(miDepa.name)


def misDepartamentos(request):
    data = Departament.objects.all().values('name', 'budget')
    return JsonResponse(list(data), safe=False)

    data = serializers.serialize("json",
                                 Departament.objects.all())
    response = HttpResponse(data)
    response['content-type'] = 'text/json'
    return response
