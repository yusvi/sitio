from rest_framework import serializers
from home.models import Tipo_Contacto, Organizacion, Cliente_Empleado, Asignacion_Peticion
from django.contrib.auth.models import User


class TipoContactoSerializer(serializers.ModelSerializer):
#class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tipo_Contacto
        #fields = ('country_name')
        fields = '__all__' # 
        
class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organizacion
        #fields = ('state_name')
        fields = '__all__' # 
        
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente_Empleado
        #fields = ('city_name')
        fields = '__all__' # 
        

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asignacion_Peticion
        #fields = ('city_name')
        fields = '__all__' # 
        
