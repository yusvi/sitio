from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Sum
#from smart_selects import *
from smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Clasificacion_EC(models.Model):
    nombre_clasificacion = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.nombre_clasificacion

    def get_absolute_url(self):
        return reverse('editar', kwargs={'id': self.id})

class EC(models.Model):
    nombre_ec = models.CharField(max_length=200, null=False, blank=False, unique=True)
    clasificacion = models.ForeignKey(Clasificacion_EC, null=False, blank=False)

    def __unicode__(self):
        return self.nombre_ec

class Grupo_EC(models.Model):
    nombre_grupo = models.CharField(max_length=200, null=False, blank=False, unique=True)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nombre_grupo

class Tipo_Contacto(models.Model):
    CHOICES_CONTACTO = ( ('Cliente', 'Cliente'), ('Prestador de Servicios', 'Prestador de Servicios') )
    contacto = models.CharField(max_length=200, choices=CHOICES_CONTACTO, null=False, blank=False)

    def __unicode__(self):
        return self.contacto

class Organizacion(models.Model):
    nombre_organizacion = models.CharField(max_length=200, null=False, blank=False, unique=True)
    activo = models.BooleanField(default=False)
    contacto = models.ForeignKey(Tipo_Contacto, null=False, blank=False)

    def __unicode__(self):
        return self.nombre_organizacion

class Localidad(models.Model):
    organizacion = models.ForeignKey(Organizacion, null=False, blank=False)
    nombre_localidad = models.CharField(max_length=200, null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False, unique=True)
    cp = models.PositiveIntegerField(null=True, blank=True)
    ciudad = models.CharField(max_length=200, null=True, blank=True)
    pais = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre_localidad

class General_Configuracion(models.Model):
    
    CHOICES_CRITICIDAD = ( ('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo') )

    nombre_ec = models.ForeignKey(EC, null=False, blank=False)
    nombre_grupo = models.ForeignKey(Grupo_EC, null=False)
    fecha_registro = models.DateField()
    activo = models.BooleanField(default=False)
    criticidad = models.CharField(max_length=200, choices=CHOICES_CRITICIDAD, null=False, blank=False)
    localidad = models.ForeignKey(Localidad, null=False, blank=False)

    def __str__(self):
        return '%s' % (self.id)

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.nombre_marca

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, null=False)
    nombre_modelo = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.nombre_modelo

class Red(models.Model):
    tipo_red = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.tipo_red

class SO_Programa(models.Model):
    nombre_ec = models.ForeignKey(EC, editable=True, default=10)
    nombre_software = models.CharField(max_length=200, null=False, blank=False, unique=True)
    proveedor = models.CharField(max_length=200, null=True, blank=True)
    sistema_operativo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nombre_software

class Version(models.Model):
    nombre_version = models.CharField(max_length=200, null=False, blank=False)
    software = models.ForeignKey(SO_Programa, null=False)

    def __unicode__(self):
        return self.nombre_version   

class Impresora(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=9)
    nombre_impresora = models.CharField(max_length=200, null=False, blank=False, unique=True)

    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
       
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)

    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        )

    numero_serie =  models.CharField(max_length=200, null=True, blank=True)
    fecha_compra = models.DateField()
    fecha_produccion = models.DateField()
    fecha_vencimiento = models.DateField()

    def __unicode__(self):
        return self.nombre_impresora

class Granja(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=4)
    nombre_granja = models.CharField(max_length=200, null=False, blank=False, unique=True)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    fecha_produccion = models.DateField()

    def __unicode__(self):
        return self.nombre_granja
    
class Licencia(models.Model):
    
    nombre_licencia = models.CharField(max_length=200, null=False, blank=False, unique=True)

    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    tipo = models.ForeignKey(EC, null=True, blank=True)
    llave =  models.CharField(max_length=200, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    software = models.ForeignKey(SO_Programa, null=True, blank=True)
    #version = models.ForeignKey(Version, null=False)

    version = ChainedForeignKey(
        Version,
        chained_field="software",
        chained_model_field="software",
        show_all=False,
        auto_choose=False,
        null=True, blank=True
        )
    
    def __unicode__(self):
        return self.nombre_licencia

class Maquina_Virtual(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=6)
    nombre_maquina = models.CharField(max_length=200, null=False, blank=False, unique=True)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    ) 
    granja = models.ForeignKey(Granja, null=False)
    software = models.ForeignKey(SO_Programa, null=False)
    #version = models.ForeignKey(Version, null=False)
    version = ChainedForeignKey(
        Version,
        chained_field="software",
        chained_model_field="software",
        show_all=False,
        auto_choose=True,
        )
    
    #licencia = models.ForeignKey(Licencia, null=False, blank=True)
    licencia = ChainedForeignKey(
        Licencia,
        chained_field="version",
        chained_model_field="version",
        show_all=False,
        auto_choose=True,
        )
    ip = models.CharField(max_length=200, null=True, blank=True)
    cpu = models.CharField(max_length=200, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    fecha_produccion = models.DateField()

    def __unicode__(self):
        return self.nombre_maquina

class Vlan(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=13)
    nombre_vlan = models.CharField(max_length=200, null=False, blank=False, unique=True) 
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    ) 
    descripcion = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre_vlan

class Cliente_Empleado(models.Model):
    nombre_contacto = models.CharField(max_length=200, null=False, blank=False)
    apellido_contacto = models.CharField(max_length=200, null=False, blank=False)

    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    ) 
    
    activo = models.BooleanField(default=False)
    tipo_contacto = models.ForeignKey(Tipo_Contacto, null=False)
    #organizacion = models.ForeignKey(Organizacion, null=False)
    organizacion = ChainedForeignKey(
        Organizacion,
        chained_field="tipo_contacto",
        chained_model_field="contacto",
        show_all=False,
        auto_choose=True,
        )
    
    grupo = models.ForeignKey(Grupo_EC, null=False)
    funcion = models.CharField(max_length=200, null=True, blank=True)
    jefe = models.CharField(max_length=200, null=True, blank=True)
    correo = models.EmailField(max_length=70, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.nombre_contacto, self.apellido_contacto)

class PC_Laptop(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=7)
    nombre_equipo = models.CharField(max_length=200, null=False, blank=False)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    organizacion = models.ForeignKey(Organizacion, editable=True, default=1)
    #organizacion = Organizacion.objects.filter(nombre_organizacion = 'Excel Distribuidora' ).order_by( 'id' )
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="organizacion",
        chained_model_field="organizacion",
        show_all=False,
        auto_choose=True,
        )
    laptop = models.BooleanField(default=False)
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)
    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        )
    
    cpu = models.CharField(max_length=200, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    numero_serie =  models.CharField(max_length=200, null=True, blank=True)
    fecha_compra = models.DateField()
    fecha_produccion = models.DateField()
    fecha_vencimiento = models.DateField()

    def __unicode__(self):
        return '%s %s' % (self.nombre_equipo, self.contacto)

class Instalacion_Software(models.Model):
    
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    software = models.ForeignKey(SO_Programa, null=False)
    #version = models.ForeignKey(Version, null=False)
    version = ChainedForeignKey(
        Version,
        chained_field="software",
        chained_model_field="software",
        show_all=False,
        auto_choose=True,
        )
    
    licencia = models.ForeignKey(Licencia, null=False)
    pc_laptop = models.ForeignKey(
        PC_Laptop,
        on_delete=models.CASCADE,
        null=False
    )
    fecha_instalacion = models.DateField()

    def __str__(self):
        return '%s %s' % (self.software, self.pc_laptop)

class Rack(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=1)
    nombre_rack = models.CharField(max_length=200, null=False, blank=False, unique=True)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)
    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        )

    unidades_rack = models.PositiveIntegerField(null=True, blank=True)
    numero_serie =  models.CharField(max_length=200, null=True, blank=True)
    fecha_compra = models.DateField()
    fecha_produccion = models.DateField()
    fecha_vencimiento = models.DateField()

    def __unicode__(self):
        return self.nombre_rack


class Servidor(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=2)
    nombre_servidor = models.CharField(max_length=200, null=False, blank=False, unique=True)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    rack = models.ForeignKey(Rack, null=True, blank=True)
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)
    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        )
    
    software = models.ForeignKey(SO_Programa, null=True, blank=True)
    #version = models.ForeignKey(Version, null=True, blank=True)
    version = ChainedForeignKey(
        Version,
        chained_field="software",
        chained_model_field="software",
        show_all=False,
        auto_choose=True,
        null=True, blank=True
        )

    ip = models.CharField(max_length=200, null=True, blank=True)    
    licencia = models.ForeignKey(Licencia, null=True, blank=True)
    cpu = models.CharField(max_length=200, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    unidades_rack = models.PositiveIntegerField(null=True, blank=True)
    numero_serie =  models.CharField(max_length=200, null=True, blank=True)
    fecha_compra = models.DateField()
    fecha_produccion = models.DateField()
    fecha_vencimiento = models.DateField()

    def __unicode__(self):
        return self.nombre_servidor

class Hypervisor(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=5)
    nombre_hypervisor = models.CharField(max_length=200, null=False, blank=False, unique=True)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    fecha_produccion = models.DateField()
    servidor = models.ForeignKey(Servidor, null=True, blank=True)
    granja = models.ForeignKey(Granja, null=True, blank=True)
                                         
    def __unicode__(self):
        return self.nombre_hypervisor

class Telefono_Celular(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=8)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    organizacion = models.ForeignKey(Organizacion, editable=True, default=1)
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="organizacion",
        chained_model_field="organizacion",
        show_all=False,
        auto_choose=True,
        )
    celular = models.BooleanField(default=False)
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)
    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        )
    
    numero_telefono = models.CharField(max_length=200, null=False, blank=False)
    numero_serie =  models.CharField(max_length=200, null=True, blank=True)
    fecha_produccion = models.DateField()

    def __unicode__(self):
        return '%s %s' % (self.nombre_ec, self.contacto)

class Dispositivo_Red(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=3)
    nombre_dispositivo = models.CharField(max_length=200, null=False, blank=False, unique=True)
    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )
    rack = models.ForeignKey(Rack, null=True, blank=True)
    tipo_red = models.ForeignKey(Red, null=True, blank=True)
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)
    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        )
    software = models.ForeignKey(SO_Programa, null=True, blank=True)
    #version = models.ForeignKey(Version, null=True, blank=True)
    version = ChainedForeignKey(
        Version,
        chained_field="software",
        chained_model_field="software",
        show_all=False,
        auto_choose=True,
        null=True, blank=True
        )
    
    ip = models.CharField(max_length=200, null=True, blank=True)
    ram = models.CharField(max_length=200, null=True, blank=True)
    unidades_rack = models.PositiveIntegerField(null=True, blank=True)
    numero_serie =  models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre_dispositivo

class Interfaz_Red(models.Model):
    #nombre_ec = models.ForeignKey(EC, editable=True, default=12)
    nombre_interfaz = models.CharField(max_length=200, null=False, blank=False, unique=True)

    general = models.OneToOneField(
        General_Configuracion,
        on_delete=models.CASCADE,
        null=False
    )

    dispositivo = models.ForeignKey(Dispositivo_Red, null=True, blank=True)
    ip = models.CharField(max_length=200, null=True, blank=True)
    mac = models.CharField(max_length=200, null=True, blank=True)
    gateway = models.CharField(max_length=200, null=True, blank=True)
    mascara = models.CharField(max_length=200, null=True, blank=True)
    velocidad = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre_interfaz

class Auditoria_EC(models.Model):
    fecha_auditoria = models.DateField()
    nombre_ec = models.ForeignKey(EC, null=False)
    total_elementos = models.PositiveIntegerField(null=True, blank=True)
    total_productivo = models.PositiveIntegerField(null=True, blank=True)
    total_alta = models.PositiveIntegerField(null=True, blank=True)
    total_media = models.PositiveIntegerField(null=True, blank=True)
    total_baja = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return 'Auditoria %s' % (self.fecha_auditoria)

class Tipo_Solicitud(models.Model):
    CHOICES_SOLICITUD = ( ('Cambio', 'Cambio'), ('Mejora', 'Mejora') )
    nombre_solicitud = models.CharField(max_length=200, choices=CHOICES_SOLICITUD, null=False, blank=False)

    def __unicode__(self):
            return self.nombre_solicitud

class Origen(models.Model):

    nombre_origen = models.CharField(max_length=200, null=False, blank=False, unique=True)
    solicitud = models.ForeignKey(Tipo_Solicitud, null=False)

    def __unicode__(self):
        return self.nombre_origen

class Solicitud_Cambio(models.Model):
    
    CHOICES_EFICACIA = ( ('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo') )

    grupo = models.ForeignKey(Grupo_EC, null=False)
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    fecha = models.DateField()
    asunto = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    #estimacion_recursos = models.CharField(max_length=200, null=True, blank=True)
    estimacion_recursos = models.CharField(max_length=200, choices=CHOICES_EFICACIA, null=False, blank=False)
    tiempo_cambio = models.CharField(max_length=200, null=True, blank=True)
 

    def __unicode__(self):
        return 'Cambio %s' % (self.id)

class Exclusivo_Cambio(models.Model):
    CHOICES_ESTADOS = ( ('Aprobada', 'Aprobada'), ('En Espera', 'En Espera'), ('Rechazado', 'Rechazado') )
    CHOICES_ORIGEN = ( ('Actualizacion de Infraestructura', 'Actualizacion de Infraestructura'),
                       ('Infraestructura', 'Infraestructura'),
                       ('Proposito de Mejora', 'Proposito de Mejora'),
                       ('Nuevo Servicio', 'Nuevo Servicio'),
                       ('Modificacion de Servicio', 'Modificacion de Servicio'),
                       ('Gestion de Problema', 'Gestion de Problema'))

    #folio = models.ForeignKey(Solicitud_Cambio, null=False)
    folio= models.OneToOneField(
        Solicitud_Cambio,
        on_delete=models.CASCADE,
        null=False
    )

    origen = models.CharField(max_length=200, choices=CHOICES_ORIGEN, null=False, blank=False)
    #origen = models.ForeignKey(Origen, null=False)
    #origen = ChainedForeignKey(
     #   Origen,
      #  chained_field="solicitud",
       # chained_model_field="solicitud",
        #show_all=False,
        #auto_choose=True,
        #)
    estado = models.CharField(max_length=200, choices=CHOICES_ESTADOS, null=False, blank=False)

    def __unicode__(self):
        return 'Exclusivo %s' % (self.id)



class Encargados(models.Model):
    grupo = models.ForeignKey(Grupo_EC, null=False)
    encargado = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    
    def __unicode__(self):
        return '%s' % (self.encargado)

class Reunion(models.Model):
    solicitud = models.ForeignKey(Tipo_Solicitud, null=False)
    fecha_reunion = models.DateField()
    
    def __unicode__(self):
        return '%s %s' % (self.solicitud, self.fecha_reunion)

class Asistencia_Reunion(models.Model):
    solicitud = models.ForeignKey(Tipo_Solicitud, null=False)
    #reunion = models.ForeignKey(Reunion, null=False)
    reunion = ChainedForeignKey(
        Reunion,
        chained_field="solicitud",
        chained_model_field="solicitud",
        show_all=False,
        auto_choose=True,
        )
    encargado = models.ForeignKey(Encargados, null=False)
    asistencia = models.BooleanField(default=False)
    
    def __unicode__(self):
        return 'Asistencia %s' % (self.id)

class Marcha_Atras(models.Model):
    recursos = models.CharField(max_length=200, null=True, blank=True)
    tiempo = models.CharField(max_length=200, null=True, blank=True)
    procedimiento = models.CharField(max_length=200, null=True, blank=True)
    descripcion_plan = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return 'Marcha Atras %s' % (self.id)
    

class Planificacion_Cambio(models.Model):
    CHOICES_PRIORIDAD = ( ('Baja', 'Baja'), ('Normal', 'Normal'), ('Alta', 'Alta'), ('Urgente', 'Urgente') )
    CHOICES_CATEGORIA = ( ('Rutina', 'Rutina'), ('Normal', 'Normal'), ('Urgente', 'Urgente') )
    
    folio= models.OneToOneField(
        Solicitud_Cambio,
        on_delete=models.CASCADE,
        null=False
    )
    reunion = models.ForeignKey(Reunion, null=False)
    area_implicada = models.ForeignKey(Grupo_EC, null=False) 
    coordinador = models.ForeignKey(Cliente_Empleado, null=False)

    hora_impacto = models.CharField(max_length=200, null=True, blank=True)
    duracion_impacto = models.CharField(max_length=200, null=True, blank=True)
    costo_impacto = models.CharField(max_length=200, null=True, blank=True)
    prioridad = models.CharField(max_length=200, choices=CHOICES_PRIORIDAD, null=False, blank=False)
    categoria = models.CharField(max_length=200, choices=CHOICES_CATEGORIA, null=False, blank=False)
    descripcion_aprobado = models.TextField(null=True, blank=True)
    observaciones = models.CharField(max_length=200, null=True, blank=True)
    plan_marcha_atras = models.OneToOneField(
        Marcha_Atras,
        on_delete=models.CASCADE,
        null=True, blank=True)

    def __unicode__(self):
        return 'Planificacion %s' % (self.folio)
    
    
class Responsables_Cambio(models.Model):
    #planificacion = models.ForeignKey(Planificacion_Cambio, null=False)
    folio=models.ForeignKey(Solicitud_Cambio, null=False)

    acciones = models.TextField(null=True, blank=True)
    grupo = models.ForeignKey(Grupo_EC, null=False)
    #responsable = models.ForeignKey(Cliente_Empleado, null=False)

    responsable = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )

    #responsable = Cliente_Empleado.objects.filter(grupo=grupo)
    fecha_revision_accion = models.DateField()

    def __unicode__(self):
        return 'Responsabilidad %s' % (self.id)

class Seguimiento_Cambio(models.Model):
    folio=models.ForeignKey(Solicitud_Cambio, null=False)
    #responsabilidad_encargado = models.ForeignKey(Responsables_Cambio, null=False)

    responsabilidad_encargado = ChainedForeignKey(
        Responsables_Cambio,
        chained_field="folio",
        chained_model_field="folio",
        show_all=False,
        auto_choose=True
        )
    
    
    fecha_seguimiento = models.DateField()
    descripcion_seguimiento = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return 'Seguimiento %s' % (self.id)

class Verificacion_Cambio(models.Model):
    CHOICES_EFICACIA = ( ('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja') )

    folio=models.OneToOneField(
        Solicitud_Cambio,
        null=False
    )
    ##planificacion = models.ForeignKey(Planificacion_Cambio, null=False)
    #planificacion= models.OneToOneField(
     #   Planificacion_Cambio,
      #  on_delete=models.CASCADE,
       # null=False
    #)
    fecha_verificacion = models.DateField()
    eficacia = models.CharField(max_length=200, choices=CHOICES_EFICACIA, null=False, blank=False)
    descripcion_eficacia = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return 'Verificacion %s' % (self.id)








class Tipo_Peticion(models.Model):
    CHOICES_PETICION = ( ('Requerimiento', 'Requerimiento'), ('Incidente', 'Incidente') )
    nombre_peticion = models.CharField(max_length=200, choices=CHOICES_PETICION, null=True, blank=True, unique=True)

    def __unicode__(self):
            return self.nombre_peticion

class Alcance(models.Model):
    nombre_alcance = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __unicode__(self):
            return self.nombre_alcance

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=200, null=True, blank=True, unique=True)
    alcance  = models.ForeignKey(Alcance, null=False, default=1)

    def __unicode__(self):
            return self.nombre_servicio 

class Subcategoria(models.Model):
    servicio = models.ForeignKey(Servicio, null=False)
    nombre_subcategoria = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __unicode__(self):
            return self.nombre_subcategoria   
 
class Producto(models.Model):
    servicio = models.ForeignKey(Servicio, null=False)
    #subcategoria = models.ForeignKey(Sucategoria, null=False)
    subcategoria = ChainedForeignKey(
        Subcategoria,
        chained_field="servicio",
        chained_model_field="servicio",
        show_all=False,
        auto_choose=True,
        )    
    marca = models.ForeignKey(Marca, null=False)
    #modelo = models.ForeignKey(Modelo, null=False)
    modelo = ChainedForeignKey(
        Modelo,
        chained_field="marca",
        chained_model_field="marca",
        show_all=False,
        auto_choose=True,
        unique=True,
        )
    descripcion_producto = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return '%s' % (self.descripcion_producto)

class Peticion(models.Model):
    CHOICES_ORIGEN = ( ('Correo', 'Correo'), ('Monitoreo', 'Monitoreo'), ('Telefono', 'Telefono'), ('Portal', 'Portal') )
    CHOICES_IMPACTO = ( ('Departamento', 'Departamento'), ('Servicio', 'Servicio'), ('Persona', 'Persona') )
    CHOICES_URGENCIA = ( ('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Critica', 'Critica') )

    peticion = models.ForeignKey(Tipo_Peticion, null=True)
    tipo_contacto = models.ForeignKey(Tipo_Contacto, null=False)
    #organizacion = models.ForeignKey(Organizacion, null=False)
    organizacion = ChainedForeignKey(
        Organizacion,
        chained_field="tipo_contacto",
        chained_model_field="contacto",
        show_all=False,
        auto_choose=True,
        )
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="organizacion",
        chained_model_field="organizacion",
        show_all=False,
        auto_choose=True,
        )
    origen = models.CharField(max_length=200, choices=CHOICES_ORIGEN, null=False, blank=False)
    asunto = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    impacto = models.CharField(max_length=200, choices=CHOICES_IMPACTO, null=False, blank=False)
    urgencia = models.CharField(max_length=200, choices=CHOICES_URGENCIA, null=False, blank=False)

    def __unicode__(self):
        return '%s %s' % (self.peticion, self.id)
    

class Productos_Peticion(models.Model):
    #tipo = models.ForeignKey(Tipo_Peticion, null=True)
    ##peticion = models.OneToOneField(Peticion, null=False)
    peticion = ChainedForeignKey(
        Peticion,
        chained_field="tipo",
        chained_model_field="peticion",
        show_all=False,
        auto_choose=True,
        on_delete=models.CASCADE
        )
    producto = models.ForeignKey(Producto, null=False)
    cantidad = models.PositiveIntegerField(null=False, blank=False)

    def __unicode__(self):
        return '%s %s' % (self.peticion, self.producto)
    
class Asignacion_Peticion(models.Model):
    #tipo = models.ForeignKey(Tipo_Peticion, null=True)
    #peticion = models.OneToOneField(Peticion, null=False)
    peticion = ChainedForeignKey(
        Peticion,
        chained_field="tipo",
        chained_model_field="peticion",
        show_all=False,
        auto_choose=True,
        unique=True,
        on_delete=models.CASCADE
        )
    
    grupo = models.ForeignKey(Grupo_EC, null=False)
    #contacto = models.ForeignKey(Cliente_Empleado, null=True)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    fecha_asignacion = models.DateField()

    def __unicode__(self):
        return 'Asignacion %s' % (self.peticion)

class Seguimiento_Peticion(models.Model):
    #tipo = models.ForeignKey(Tipo_Peticion, null=True)
    ##peticion = models.ForeignKey(Peticion, null=False)
    peticion = ChainedForeignKey(
        Peticion,
        chained_field="tipo",
        chained_model_field="peticion",
        show_all=False,
        auto_choose=True,
        )

    ##asignacion = models.ForeignKey(Asignacion_Peticion, null=False)
    #asignacion = ChainedForeignKey(
     #   Asignacion_Peticion,
      #  chained_field="peticion",
       # chained_model_field="peticion",
        #show_all=False,
        #auto_choose=True,
        #)
    fecha_seguimiento = models.DateField()
    observaciones = models.TextField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return 'Seguimiento %s de %s' % (self.id, self.peticion)

class Lista_Proveedores(models.Model):
    #tipo_contacto=models.ForeignKey(Tipo_Contacto, editable=True, default=2)
    tipo_contacto = models.ForeignKey(Tipo_Contacto, editable=True, default=2)
    #organizacion = models.ForeignKey(Organizacion, null=False)
    organizacion = ChainedForeignKey(
        Organizacion,
        chained_field="tipo_contacto",
        chained_model_field="contacto",
        show_all=False,
        auto_choose=True,
        )
    #localidad=models.ForeignKey(Localidad, null=False)
    localidad = ChainedForeignKey(
        Localidad,
        chained_field="organizacion",
        chained_model_field="organizacion",
        show_all=False,
        auto_choose=True,
        )

    def __unicode__(self):
        return '%s' % (self.organizacion)

class Acuerdo_SLA(models.Model):
    CHOICES_MONEDA = ( ('Pesos', 'Pesos'), ('Dolares', 'Dolares'))

    tipo = models.ForeignKey(Tipo_Peticion, null=True)
    ##peticion = models.ForeignKey(Peticion, null=False)
    peticion = ChainedForeignKey(
        Peticion,
        chained_field="tipo",
        chained_model_field="peticion",
        show_all=False,
        auto_choose=True,
        unique=True
        )

    ##asignacion = models.ForeignKey(Asignacion_Peticion, null=False)
    #asignacion = ChainedForeignKey(
     #   Asignacion_Peticion,
      #  chained_field="peticion",
       # chained_model_field="peticion",
        #show_all=False,
        #auto_choose=True,
        #)
    
    #fecha_asignacion = models.DateField() # ajax 
    fecha_solucion = models.DateField()
    costo = models.PositiveIntegerField(null=True, blank=True)
    moneda = models.CharField(max_length=200, choices=CHOICES_MONEDA, null=False, blank=False)
    proveedor = models.ForeignKey(Lista_Proveedores, null=False)

    def __unicode__(self):
        return 'Acuerdo %s' % (self.peticion)

class Cierre_Peticion(models.Model):
    peticion = models.OneToOneField(Peticion, null=False)
    ##asignacion = models.ForeignKey(Asignacion_Peticion, null=False)
    #asignacion = ChainedForeignKey(
     #   Asignacion_Peticion,
      #  chained_field="peticion",
       # chained_model_field="peticion",
        #show_all=False,
        #auto_choose=True,
        #)
    solucion = models.TextField(max_length=200, null=True, blank=True)
    fecha_cierre = models.DateField()

    def __unicode__(self):
        return 'Cierre %s' % (self.peticion)

class Entrega_Peticion(models.Model):
    peticion = models.ForeignKey(Peticion, null=False)
    ##cierre = models.ForeignKey(Cierre_Peticion, null=False)
    #cierre = ChainedForeignKey(
     #   Cierre_Peticion,
      #  chained_field="peticion",
       # chained_model_field="peticion",
        #show_all=False,
        #auto_choose=True,
        #)
    #producto = models.ForeignKey(Productos_Peticion, null=False)
    producto = ChainedForeignKey(
        Productos_Peticion,
        chained_field="peticion",
        chained_model_field="peticion",
        show_all=False,
        auto_choose=False,
        unique=True,
        )
    factura = models.CharField(max_length=200, null=True, blank=True)
    fecha_factura = models.DateField()
    chofer = models.CharField(max_length=200, null=True, blank=True)
    firma = models.CharField(max_length=200, null=True, blank=True)
    fecha_entrega = models.DateField()

    def __unicode__(self):
        return 'Entrega %s %s' % (self.id, self.peticion)

    
class Problema(models.Model):
    CHOICES_IMPACTO = ( ('Departamento', 'Departamento'), ('Servicio', 'Servicio'), ('Persona', 'Persona') )
    CHOICES_URGENCIA = ( ('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Critica', 'Critica') )

    peticion = models.OneToOneField(Peticion, null=False)
    #producto = models.ForeignKey(Productos_Peticion, null=False)
    producto = ChainedForeignKey(
        Productos_Peticion,
        chained_field="peticion",
        chained_model_field="peticion",
        show_all=False,
        auto_choose=True,
        unique=True,
        )
    proveedor = models.ForeignKey(Lista_Proveedores, null=False)
    asunto_problema = models.CharField(max_length=200, null=True, blank=True)
    descripcion_problema = models.TextField(null=True, blank=True)
    impacto = models.CharField(max_length=200, choices=CHOICES_IMPACTO, null=False, blank=False)
    urgencia = models.CharField(max_length=200, choices=CHOICES_URGENCIA, null=False, blank=False)
    solicitud_cambio = models.ForeignKey(Solicitud_Cambio, null=True, blank=True)

    def __unicode__(self):
        return 'Problema %s' % (self.id)

class Asignacion_Problema(models.Model):
    problema = models.OneToOneField(Problema, null=False)
    grupo = models.ForeignKey(Grupo_EC, null=False)
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    fecha_inicio = models.DateField()
    fecha_resolucion = models.DateField()

    def __unicode__(self):
        return 'Asignacion %s' % (self.id)

class Seguimiento_Problema(models.Model):
    problema = models.ForeignKey(Problema, null=False)
    ##asignacion = models.ForeignKey(Asignacion_Problema, null=False)
    #asignacion = ChainedForeignKey(
        #Asignacion_Problema,
        #chained_field="problema",
        #chained_model_field="problema",
        #show_all=False,
        #auto_choose=True,
        #)
    fecha_seguimiento = models.DateField()
    observaciones = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return 'Seguimiento %s %s' % (self.id, self.problema)

class Errores(models.Model):
    sintoma = models.CharField(max_length=200, null=True, blank=True)
    que_sucedio = models.CharField(max_length=200, null=True, blank=True)
    por_que_sucedio = models.CharField(max_length=200, null=True, blank=True)
    que_puede_hacerse = models.CharField(max_length=200, null=True, blank=True)
    solucion_temporal = models.CharField(max_length=200, null=True, blank=True)
    solucion_final = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return 'Error %s' % (self.id)

class Cierre_Problema(models.Model):
    problema = models.OneToOneField(Problema, null=False)
    ##asignacion= models.ForeignKey(Asignacion_Problema, null=False)
    #asignacion = ChainedForeignKey(
     #   Asignacion_Problema,
      #  chained_field="problema",
       # chained_model_field="problema",
        #show_all=False,
        #auto_choose=True,
        #)
    fecha_cierre = models.DateField()
    error_conocido = models.ForeignKey(Errores, null=False)

    def __unicode__(self):
        return 'Cierre %s %s' % (self.id, self.problema)


class Desempeno(models.Model):
    concepto = models.CharField(max_length=200, null=False, blank=False, unique=True)
    porcentaje = models.PositiveIntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __unicode__(self):
        return '%s' % (self.concepto)

class Puntaje(models.Model):
    CHOICES_OPCION = ( ('Nunca', 'Nunca'), ('Pocas veces', 'Pocas veces'), ('Frecuentemente', 'Frecuentemente'), ('Siempre', 'Siempre') )

    opcion = models.CharField(max_length=200, choices=CHOICES_OPCION, null=False, blank=False, unique=True)
    puntos = models.PositiveIntegerField(null=False, blank=False)

    def __unicode__(self):
        return '%s' % (self.opcion)

class Ponderacion(models.Model):
    CHOICES_ESTADO = ( ('Insuficiente', 'Insuficiente'), ('Suficiente', 'Suficiente'), ('Bueno', 'Bueno'), ('Muy bueno', 'Muy bueno') )

    numero_minimo_incidentes = models.PositiveIntegerField(null=True, blank=True)
    estado = models.CharField(max_length=200, choices=CHOICES_ESTADO, null=False, blank=False, unique=True)

    def __str__(self):
        return '%s' % (self.estado)


class Tipo_Proceso(models.Model):
    CHOICES_TIPO = ( ('Recurso', 'Recurso'), ('Cliente', 'Cliente'), ('Seguridad', 'Seguridad'), ('Auditoria de Seguridad','Auditoria de Seguridad'), ('Proveedor', 'Proveedor') )
    
    tipo_proceso = models.CharField(max_length=200, choices=CHOICES_TIPO, null=False, blank=False, unique=True)

    def __unicode__(self):
        return '%s' % (self.tipo_proceso)




class Evaluacion(models.Model):
    proceso = models.ForeignKey(Tipo_Proceso, null=False)
    proveedor = models.ForeignKey(Lista_Proveedores, null=False)
    fecha_inicio = models.DateField()
    fecha_proxima_evaluacion = models.DateField()

    def __unicode__(self):
        return '%s' % (self.fecha_inicio)
    
class Reevaluacion_Proveedores(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, null=False)
    proveedor = models.ForeignKey(Lista_Proveedores, null=False)
    concepto = models.ForeignKey(Desempeno, null=False)
    puntaje = models.ForeignKey(Puntaje, null=False)

    def __unicode__(self):
        return 'Reevaluacion %s %s' % (self.evaluacion, self.proveedor)

class Evaluacion_Proveedores(models.Model):
    #evaluacion = models.ForeignKey(Evaluacion, null=False)
    proceso = models.ForeignKey(Tipo_Proceso, null=False)
    fecha_registro=models.DateField()
    proveedor = models.ForeignKey(Lista_Proveedores, null=False)
    total_incidentes = models.PositiveIntegerField(editable=False)
    estado = models.ForeignKey(Ponderacion, editable=False)

    calificacion = models.PositiveIntegerField(default=0, blank=True)
    estado2 = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        
        total= Acuerdo_SLA.objects.filter(proveedor_id=self.proveedor_id, tipo_id=2).count()
        self.total_incidentes = total

        maximo = Ponderacion.objects.filter(numero_minimo_incidentes__gte=self.total_incidentes).values('id')[0]['id']
        self.estado_id=maximo
        
        
        super(Evaluacion_Proveedores, self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Evaluacion %s %s' % (self.fecha_registro, self.proveedor)
    



class Preguntas(models.Model):
    tipo_pregunta = models.ForeignKey(Tipo_Proceso, null=False)
    pregunta = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __unicode__(self):
        return '%s' % (self.pregunta)

class Respuestas(models.Model):
    CHOICES_RESPUESTA = ( ('Muy poco', 'Muy poco'), ('Poco', 'Poco'), ('Medio', 'Medio'), ('Mucho', 'Mucho'), ('Totalmente', 'Totalmente') )
    
    tipo_respuesta = models.ForeignKey(Tipo_Proceso, null=False)
    respuesta = models.CharField(max_length=200, choices=CHOICES_RESPUESTA, null=False, blank=False, unique=True)
 
    def __unicode__(self):
        return '%s' % (self.respuesta)


RATING_CHOICES2 = ((0, u"Nunca"), (1, u"Pocas veces"), (2, u"Frecuentemente"), (3, u"Siempre"),)

class ProveedorAnswer(models.Model):
    evaluacion_proveedores = models.ForeignKey(Evaluacion_Proveedores, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Preguntas)
    #respuesta = models.CharField(max_length=200, choices=RATING_CHOICES, null=True, blank=True)
    respuesta = models.SmallIntegerField(choices=RATING_CHOICES2, null=True, blank=True)



    def __unicode__(self):
        return 'Pregunta %s- %s' % (self.pregunta_id, self.evaluacion_proveedores)




    

class Encuestado(models.Model):
    proceso = models.ForeignKey(Tipo_Proceso, null=False)
    tipo_contacto = models.ForeignKey(Tipo_Contacto, null=False)
    #organizacion = models.ForeignKey(Organizacion, null=False)
    organizacion = ChainedForeignKey(
        Organizacion,
        chained_field="tipo_contacto",
        chained_model_field="contacto",
        show_all=False,
        auto_choose=True,
        )
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="organizacion",
        chained_model_field="organizacion",
        show_all=False,
        auto_choose=True,
        null=True, blank=True
        )
    fecha_encuesta = models.DateField()
    calificacion = models.PositiveIntegerField(default=0, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return '%s, %s (%s)' % (self.proceso, self.organizacion, self.fecha_encuesta)


class ClienteQuestion(models.Model):
    pregunta = models.CharField(max_length=200)
    proceso = models.ForeignKey(Tipo_Proceso, null=False)

    def __unicode__(self):
        return self.pregunta

RATING_CHOICES = ((0, u"Muy poco"), (1, u"Poco"), (2, u"Medio"), (3, u"Mucho"), (4, u"Totalmente"),)

class ClienteAnswer(models.Model):
    encuestado = models.ForeignKey(Encuestado, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Preguntas)
    #respuesta = models.CharField(max_length=200, choices=RATING_CHOICES, null=True, blank=True)
    respuesta = models.SmallIntegerField(choices=RATING_CHOICES, null=True, blank=True)



    def __unicode__(self):
        return 'Pregunta %s- %s' % (self.pregunta_id, self.encuestado)







class Encuesta(models.Model):
    tipo_proceso = models.ForeignKey(Tipo_Proceso, null=False, editable=True, default=2)
    #encuestado = models.ForeignKey(Encuestado, null=False)
    encuestado = ChainedForeignKey(
        Encuestado,
        chained_field="tipo_proceso",
        chained_model_field="proceso",
        show_all=False,
        auto_choose=True,
        )
    pregunta = ChainedForeignKey(
        Preguntas,
        chained_field="tipo_proceso",
        chained_model_field="tipo_pregunta",
        show_all=False,
        auto_choose=True,
        )
    respuesta = ChainedForeignKey(
        Respuestas,
        chained_field="tipo_proceso",
        chained_model_field="tipo_respuesta",
        show_all=False,
        auto_choose=True,
        )

    def __unicode__(self):
        return 'Encuesta %s' % (self.encuestado)

class Reclamacion(models.Model):
    CHOICES_IMPORTANCIA = ( ('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Critica', 'Critica') )

    tipo_contacto = models.ForeignKey(Tipo_Contacto, null=False, default=1)
    #organizacion = models.ForeignKey(Organizacion, null=False)
    organizacion = ChainedForeignKey(
        Organizacion,
        chained_field="tipo_contacto",
        chained_model_field="contacto",
        show_all=False,
        auto_choose=True,
        )
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="organizacion",
        chained_model_field="organizacion",
        show_all=False,
        auto_choose=True,
        )
    #cliente = models.ForeignKey(Encuestado, null=False)

    fecha_registro = models.DateField()
    
    servicio = models.ForeignKey(Servicio, null=False)
    #subcategoria = models.ForeignKey(Sucategoria, null=False)
    subcategoria = ChainedForeignKey(
        Subcategoria,
        chained_field="servicio",
        chained_model_field="servicio",
        show_all=False,
        auto_choose=True,
        )
    motivo_reclamacion = models.CharField(max_length=200, null=False, blank=False)
    #importancia_cliente = models.CharField(max_length=200, null=False, blank=False)
    valor_importancia = models.CharField(max_length=200, choices=CHOICES_IMPORTANCIA, null=False, blank=False)

    def __unicode__(self):
        return 'Reclamacion %s' % (self.id)

class Asignacion_Reclamacion(models.Model):
    reclamacion = models.OneToOneField(Reclamacion, null=False)
    grupo = models.ForeignKey(Grupo_EC, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    fecha_asignacion = models.DateField()

    def __unicode__(self):
        return 'Asignacion %s' % (self.reclamacion)

class Asignacion_Encuesta(models.Model):
    encuesta = models.OneToOneField(Encuestado, null=False)
    grupo = models.ForeignKey(Grupo_EC, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    fecha_asignacion = models.DateField()

    def __unicode__(self):
        return 'Asignacion %s' % (self.encuesta)


class Activos(models.Model):
    activo = models.CharField(max_length=200, null=False, blank=False, unique=True)
    clase = models.CharField(max_length=200, null=False, blank=False, unique=True)
    confidencialidad = models.PositiveIntegerField(null=True, blank=True)
    integridad = models.PositiveIntegerField(null=True, blank=True)
    disponibilidad = models.PositiveIntegerField(null=True, blank=True)
    valor = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.valor = self.confidencialidad * self.integridad * self.disponibilidad
        super(Activos, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % (self.activo)

class Amenazas(models.Model):
    amenaza = models.CharField(max_length=200, null=False, blank=False, unique=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    vulnerabilidad = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % (self.amenaza)

class Prioridad_Riesgo(models.Model):
    CHOICES_PRIORIDAD = ( ('Baja', 'Baja'), ('Media', 'Media'), ('Mayor', 'Mayor') )

    numero_maximo_riesgo = models.PositiveIntegerField(null=True, blank=True)
    prioridad = models.CharField(max_length=200, choices=CHOICES_PRIORIDAD, null=False, blank=False, unique=True)

    def __str__(self):
        return '%s' % (self.prioridad)

class Riesgos(models.Model):
    amenaza = models.ForeignKey(Amenazas, null=False)
    activo = models.ForeignKey(Activos, null=False)
    probabilidad = models.PositiveIntegerField(null=True, blank=True)
    impacto = models.PositiveIntegerField(null=True, blank=True)
    valor = models.PositiveIntegerField(editable=False)
    calculo_riesgo = models.PositiveIntegerField(editable=False)
    prioridad = models.ForeignKey(Prioridad_Riesgo, editable=False)

    def save(self, *args, **kwargs):

        valor= Activos.objects.filter(activo=self.activo).values('valor')[0]['valor']
        self.valor = valor

        self.calculo_riesgo = self.probabilidad * self.impacto * self.valor
        
        prioridad = Prioridad_Riesgo.objects.filter(numero_maximo_riesgo__lte=self.calculo_riesgo).values('id')[0]['id']
        self.prioridad_id=prioridad

        super(Riesgos, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s' % (self.activo, self.amenaza)


class Analisis_Riesgos(models.Model):
    CHOICES_ESTADO = ( ('Abierto', 'Abierto'), ('En proceso', 'En proceso'), ('Implementado', 'Implementado') )
    CHOICES_OPCIONES = ( ('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto') )


    riesgo = models.OneToOneField(Riesgos, null=False)
    accion =  models.TextField(null=True, blank=True)
    costo = models.CharField(max_length=200, choices=CHOICES_OPCIONES, null=False, blank=False)
    proceso = models.ForeignKey(Tipo_Proceso, null=False)
    recursos = models.CharField(max_length=200, choices=CHOICES_OPCIONES, null=False, blank=False)
    grupo = models.ForeignKey(Grupo_EC, null=False)
    #contacto = models.ForeignKey(Cliente_Empleado, null=False)
    contacto = ChainedForeignKey(
        Cliente_Empleado,
        chained_field="grupo",
        chained_model_field="grupo",
        show_all=False,
        auto_choose=True,
        )
    estado_accion = models.CharField(max_length=200, choices=CHOICES_ESTADO, null=False, blank=False)

    def __unicode__(self):
        return 'Analisis Riesgo %s' % (self.id)

class Calificacion(models.Model):
    CHOICES_OPCIONES = ( ('Muy bien', 'Muy bien'), ('Bien', 'Bien'), ('Suficiente', 'Suficiente'), ('Bajo', 'Bajo')  )

    valor = models.CharField(max_length=200, choices=CHOICES_OPCIONES, null=False, blank=False, unique=True)
    puntos_respuesta = models.PositiveIntegerField(editable=True)
    puntos_cuestionario = models.PositiveIntegerField(editable=True)

    def __unicode__(self):
        return '%s' % (self.valor)

class Cuestionario_Seguridad(models.Model):
    proceso = models.ForeignKey(Tipo_Proceso, null=False, editable=True, default=3)
    #encuestado = models.ForeignKey(Encuestado, null=False)
    encuestado = ChainedForeignKey(
        Encuestado,
        chained_field="proceso",
        chained_model_field="proceso",
        show_all=False,
        auto_choose=True,
        )
    pregunta = ChainedForeignKey(
        Preguntas,
        chained_field="proceso",
        chained_model_field="tipo_pregunta",
        show_all=False,
        auto_choose=True,
        )
    descripcion_respuesta = models.TextField(null=True, blank=True)
    puntaje = models.ForeignKey(Calificacion, null=False)
    puntos = models.PositiveIntegerField(editable=False) 


    def save(self, *args, **kwargs):
        puntos = Calificacion.objects.filter(valor=self.puntaje).values('puntos_respuesta')[0]['puntos_respuesta']
        self.puntos = puntos
        
        super(Cuestionario_Seguridad, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Cuestionario %s' % (self.encuestado)

class Resultado_Cuestionario(models.Model):

    proceso = models.ForeignKey(Tipo_Proceso, null=False, editable=True, default=3)
    encuestado = ChainedForeignKey(
        Encuestado,
        chained_field="proceso",
        chained_model_field="proceso",
        show_all=False,
        auto_choose=True,
        unique=True,
        )
    calificacion = models.PositiveIntegerField(editable=False)
    estado = models.CharField(max_length=200, null=False, blank=False, editable=False)
    

    def save(self, *args, **kwargs):
        
        total= Cuestionario_Seguridad.objects.values('puntos').filter(encuestado=self.encuestado).aggregate(Sum('puntos')).values()[0]
        self.calificacion = (total * 100)/16

        estado = Calificacion.objects.filter(puntos_cuestionario__lte=self.calificacion).values('valor')[0]['valor']
        self.estado=estado

        
        super(Resultado_Cuestionario, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Calificacion %s' % (self.encuestado)

class Auditoria_Seguridad(models.Model):
    fecha_inicio = models.DateField()
    fecha_proxima = models.DateField()

    def __unicode__(self):
        return 'Auditoria Seguridad %s' % (self.fecha_inicio)

class Calificacion_Seguridad(models.Model):
    CHOICES_ESTADO = ( ('Parcial', 'Parcial'), ('No implementado', 'No implementado'), ('Implementado', 'Implementado') )

    respuesta = models.CharField(max_length=200, choices=CHOICES_ESTADO, null=False, blank=False)
    puntos = models.PositiveIntegerField(editable=True)
    
    def __unicode__(self):
        return '%s' % (self.respuesta)
    
class Checklist_Auditoria_Seguridad(models.Model):
    auditoria = models.ForeignKey(Auditoria_Seguridad, null=False)
    proceso = models.ForeignKey(Tipo_Proceso, null=False, editable=True, default=4)
    #encuestado = models.ForeignKey(Encuestado, null=False)
    encuestado = ChainedForeignKey(
        Encuestado,
        chained_field="proceso",
        chained_model_field="proceso",
        show_all=False,
        auto_choose=True,
        )
    pregunta = ChainedForeignKey(
        Preguntas,
        chained_field="proceso",
        chained_model_field="tipo_pregunta",
        show_all=False,
        auto_choose=True,
        )
    respuesta = models.ForeignKey(Calificacion_Seguridad, null=False)
    documento = models.CharField(max_length=200, null=True, blank=True)
    comentario = models.CharField(max_length=200, null=True, blank=True)
    puntos = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        
        total= Calificacion_Seguridad.objects.filter(respuesta=self.respuesta).values('puntos')[0]['puntos']
        self.puntos = total
        
        super(Checklist_Auditoria_Seguridad, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % (self.auditoria)
    
class Resultados_Auditoria_Seguridad(models.Model):
    auditoria = models.ForeignKey(Auditoria_Seguridad, null=False, unique=True)
    calificacion = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        
        total= Checklist_Auditoria_Seguridad.objects.values('puntos').filter(auditoria=self.auditoria).aggregate(Sum('puntos')).values()[0]
        self.calificacion = (100 * total) / 39
        
        super(Resultados_Auditoria_Seguridad, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return 'Resultados %s' % (self.auditoria)


