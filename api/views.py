from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import Tipo_Contacto, Organizacion, Cliente_Empleado
from .serializers import TipoContactoSerializer, OrganizacionSerializer, ContactoSerializer
import json
from django.core import serializers
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt



'''class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
'''

# Create your views here.

@api_view(['GET'])
@csrf_exempt
def get_tipo_contacto(request):
    tipobj = Tipo_Contacto.objects.all()
    print "tipobj",tipobj
    
    tipocontacto_serializer = TipoContactoSerializer(tipobj, many=True)
    response = Response(tipocontacto_serializer.data)
    
    return Response(response.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def get_organizacion(request, sid):
    
    #stateobj = State.objects.all()
    organizacionobj = Organizacion.objects.filter(contacto=sid)
    #cid =  request.GET.get('cid')
    
    organizacion_serializer = OrganizacionSerializer(organizacionobj, many=True)
    response = Response(organizacion_serializer.data)
    
    return Response(response.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def get_contacto(request, cid):
    #cityobj = City.objects.all()
    contactobj = Cliente_Empleado.objects.filter(organizacion=cid)
    
    contacto_serializer = ContactoSerializer(contactobj, many=True)
    response = Response(contacto_serializer.data)
    
    return Response(response.data,status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def get_asignacion_peticion(request, cid):
    obj = Asignacion_Peticion.objects.filter(peticion=cid)
    
    asignacion_serializer = AsignacionSerializer(obj, many=True)
    response = Response(asignacion_serializer.data)
    
    return Response(response.data,status=status.HTTP_200_OK)
