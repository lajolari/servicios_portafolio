from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from contacto.models import Mensaje
from contacto.serializers import MensajeSerializer


@csrf_exempt
def mensaje_list(request):
    """
    List all code mensajes, or create a new mensaje.
    """
    if request.method == 'GET':
        mensajes = Mensaje.objects.all()
        serializer = MensajeSerializer(mensajes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MensajeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def mensaje_detail(request, pk):
    """
    Retrieve, update or delete a code mensaje.
    """
    try:
        mensaje = Mensaje.objects.get(pk=pk)
    except mensaje.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MensajeSerializer(mensaje)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MensajeSerializer(mensaje, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mensaje.delete()
        return HttpResponse(status=204)