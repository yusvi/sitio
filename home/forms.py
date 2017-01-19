from django import forms
from .models import *
from django.forms import widgets

from django.forms.models import inlineformset_factory

class ClasificacionForm(forms.ModelForm):
#PONER DATOS (IGUALES A CAMPOS EN HTML) PARA PODER INSERTAR Y VER
    
    class Meta:
        model = Clasificacion_EC
        fields = '__all__'

class ECForm(forms.ModelForm):
    class Meta:
        model = EC
        fields = '__all__'

class TipoContactoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Contacto
        fields = '__all__'

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = '__all__'
        
class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo_EC
        fields = '__all__'

class GeneralForm(forms.ModelForm):
    class Meta:
        model = General_Configuracion
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

class RedForm(forms.ModelForm):
    class Meta:
        model = Red
        fields = '__all__'

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = SO_Programa
        fields = '__all__'

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

class ImpresoraForm(forms.ModelForm):
    class Meta:
        model = Impresora
        fields = '__all__'

class GranjaForm(forms.ModelForm):
    class Meta:
        model = Granja
        fields = '__all__'

class LicenciaForm(forms.ModelForm):
    class Meta:
        model = Licencia
        fields = '__all__'

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina_Virtual
        fields = '__all__'

class VlanForm(forms.ModelForm):
    class Meta:
        model = Vlan
        fields = '__all__'

class ContactoForm(forms.ModelForm):    
    class Meta:
        model = Cliente_Empleado
        fields = '__all__'

class PCForm(forms.ModelForm):
    class Meta:
        model = PC_Laptop
        fields = '__all__'

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion_Software
        fields = '__all__'

class RackForm(forms.ModelForm):
    class Meta:
        model = Rack
        fields = '__all__'

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = '__all__'

class HypervisorForm(forms.ModelForm):
    class Meta:
        model = Hypervisor
        fields = '__all__'

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono_Celular
        fields = '__all__'

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo_Red
        fields = '__all__'

class InterfazForm(forms.ModelForm):
    class Meta:
        model = Interfaz_Red
        fields = '__all__'

class AuditoriaECForm(forms.ModelForm):
    class Meta:
        model = Auditoria_EC
        fields = '__all__'

class CambioForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Cambio
        fields = '__all__'

class ExclusivoForm(forms.ModelForm):
    class Meta:
        model = Exclusivo_Cambio
        fields = '__all__'

class EncargadosForm(forms.ModelForm):
    class Meta:
        model = Encargados
        fields = '__all__'

class ReunionForm(forms.ModelForm):
    class Meta:
        model = Reunion
        fields = '__all__'

class AsistenciaReunionForm(forms.ModelForm):
    class Meta:
        model = Asistencia_Reunion
        fields = '__all__'

class MarchaForm(forms.ModelForm):
    class Meta:
        model = Marcha_Atras
        fields = '__all__'

class PlanificacionCambioForm(forms.ModelForm):
    class Meta:
        model = Planificacion_Cambio
        fields = '__all__'

class ResponsableCambioForm(forms.ModelForm):
    class Meta:
        model = Responsables_Cambio
        fields = '__all__'

    #def __init__(self, *args, **kwargs):
     #   responsable=kwargs.pop('grupo')
      #  super (ResponsableCambioForm, self).__init__(*args, **kwargs)
       # self.fields['responsable'].queryset = Cliente_Empleado.objects.filter(grupo=grupo_ec.nombre_grupo)

class SeguimientoCambioForm(forms.ModelForm):
    class Meta:
        model = Seguimiento_Cambio
        fields = '__all__'

class VerificacionCambioForm(forms.ModelForm):
    class Meta:
        model = Verificacion_Cambio
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields = '__all__'
        #widgets = Textarea{attrs={'id':peticion_id}
         #   'peticion':
          #  }

class ProductosPeticionForm(forms.ModelForm):
    class Meta:
        model = Productos_Peticion
        fields = '__all__'

class AsignacionPeticionForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Peticion
        fields = '__all__'

class AcuerdoForm(forms.ModelForm):
    class Meta:
        model = Acuerdo_SLA
        fields = '__all__'

class SeguimientoPeticionForm(forms.ModelForm):
    class Meta:
        model = Seguimiento_Peticion
        fields = '__all__'

class CierrePeticionForm(forms.ModelForm):
    class Meta:
        model = Cierre_Peticion
        fields = '__all__'

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega_Peticion
        fields = '__all__'

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = '__all__'

class AsignacionProblemaForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Problema
        fields = '__all__'

class SeguimientoProblemaForm(forms.ModelForm):
    class Meta:
        model = Seguimiento_Problema
        fields = '__all__'

class CierreProblemaForm(forms.ModelForm):
    class Meta:
        model = Cierre_Problema
        fields = '__all__'

class DesempenoForm(forms.ModelForm):
    class Meta:
        model = Desempeno
        fields = '__all__'

class PonderacionForm(forms.ModelForm):
    class Meta:
        model = Ponderacion
        fields = '__all__'

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'

class EvaluacionProveedorForm(forms.ModelForm):
    class Meta:
        model = Evaluacion_Proveedores
        fields = '__all__'

class ReevaluacionProveedorForm(forms.ModelForm):
    class Meta:
        model = Reevaluacion_Proveedores
        fields = '__all__'

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Preguntas
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Encuestado
        fields = '__all__'

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'

class ReclamacionForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = '__all__'

class AsignacionReclamacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Reclamacion
        fields = '__all__'

class AsignacionEncuestaForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Encuesta
        fields = '__all__'

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activos
        fields = '__all__'

class AmenazaForm(forms.ModelForm):
    class Meta:
        model = Amenazas
        fields = '__all__'

class RiesgoForm(forms.ModelForm):
    class Meta:
        model = Riesgos
        fields = '__all__'

class PrioridadRiesgoForm(forms.ModelForm):
    class Meta:
        model = Prioridad_Riesgo
        fields = '__all__'

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'

class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = Cuestionario_Seguridad
        fields = '__all__'

class AnalisisRiesgoForm(forms.ModelForm):
    class Meta:
        model = Analisis_Riesgos
        fields = '__all__'

class ResultadoCuestionarioForm(forms.ModelForm):
    class Meta:
        model = Resultado_Cuestionario
        fields = '__all__'

class AuditoriaSeguridadForm(forms.ModelForm):
    class Meta:
        model = Auditoria_Seguridad
        fields = '__all__'

class ChecklistSeguridadForm(forms.ModelForm):
    class Meta:
        model = Checklist_Auditoria_Seguridad
        fields = '__all__'

class ResultadoSeguridadForm(forms.ModelForm):
    class Meta:
        model = Resultados_Auditoria_Seguridad
        fields = '__all__'


#peticion
ProductoFormSet = inlineformset_factory(Peticion, Productos_Peticion, PeticionForm, extra=1, can_delete=False)
AnalistaFormSet = inlineformset_factory(Peticion, Asignacion_Peticion, PeticionForm, extra=1, can_delete=False)
AcuerdoFormSet = inlineformset_factory(Peticion, Acuerdo_SLA, PeticionForm, extra=1, can_delete=False)
SeguimientoFormSet = inlineformset_factory(Peticion, Seguimiento_Peticion, PeticionForm, extra=1, can_delete=False)
CierreFormSet = inlineformset_factory(Peticion, Cierre_Peticion, PeticionForm, extra=1, can_delete=False)
EntregaFormSet = inlineformset_factory(Peticion, Entrega_Peticion, PeticionForm, extra=1, can_delete=False) 
#problema
AnalistaProblemaFormset = inlineformset_factory(Problema, Asignacion_Problema, ProblemaForm, extra=1, can_delete=False)
SeguimientoProblemaFormset = inlineformset_factory(Problema, Seguimiento_Problema, ProblemaForm, extra=1, can_delete=False)
CierreProblemaFormset = inlineformset_factory(Problema, Cierre_Problema, ProblemaForm, extra=1, can_delete=False)
#cambio (pend asistencia)
ExclusivoCambioFormset = inlineformset_factory(Solicitud_Cambio, Exclusivo_Cambio, CambioForm, extra=1, can_delete=False)
PlanificacionCambioFormset = inlineformset_factory(Solicitud_Cambio, Planificacion_Cambio, CambioForm, extra=1, can_delete=False)
ResponsableCambioFormset = inlineformset_factory(Solicitud_Cambio, Responsables_Cambio, CambioForm, extra=1, can_delete=False)
SeguimientoCambioFormset = inlineformset_factory(Solicitud_Cambio, Seguimiento_Cambio, CambioForm, extra=1, can_delete=False)
VerificacionCambioFormset = inlineformset_factory(Solicitud_Cambio, Verificacion_Cambio, CambioForm, extra=1, can_delete=False)
#configuracion
ImpresoraFormset = inlineformset_factory(General_Configuracion, Impresora, GeneralForm, extra=1, can_delete=False)
GranjaFormset = inlineformset_factory(General_Configuracion, Granja, GeneralForm, extra=1, can_delete=False)
LicenciaFormset = inlineformset_factory(General_Configuracion, Licencia, GeneralForm, extra=1, can_delete=False)
MaquinaFormset = inlineformset_factory(General_Configuracion, Maquina_Virtual, GeneralForm, extra=1, can_delete=False)
VlanFormset = inlineformset_factory(General_Configuracion, Vlan, GeneralForm, extra=1, can_delete=False)
ContactoFormset = inlineformset_factory(General_Configuracion, Cliente_Empleado, GeneralForm, extra=1, can_delete=False)
PCFormset = inlineformset_factory(General_Configuracion, PC_Laptop, GeneralForm, extra=1, can_delete=False)
InstalacionFormset = inlineformset_factory(General_Configuracion, Instalacion_Software, GeneralForm, extra=1, can_delete=False)
RackFormset = inlineformset_factory(General_Configuracion, Rack, GeneralForm, extra=1, can_delete=False)
ServidorFormset = inlineformset_factory(General_Configuracion, Servidor, GeneralForm, extra=1, can_delete=False)
HypervisorFormset = inlineformset_factory(General_Configuracion, Hypervisor, GeneralForm, extra=1, can_delete=False)
TelefonoFormset = inlineformset_factory(General_Configuracion, Telefono_Celular, GeneralForm, extra=1, can_delete=False)
DispositivoFormset = inlineformset_factory(General_Configuracion, Dispositivo_Red, GeneralForm, extra=1, can_delete=False)
InterfazFormset = inlineformset_factory(General_Configuracion, Interfaz_Red, GeneralForm, extra=1, can_delete=False)

AnswerFormSet = inlineformset_factory(Encuestado, 
        ClienteAnswer, exclude=('pregunta',), 
        extra=0, can_delete=False)


ProveedorFormSet = inlineformset_factory(Evaluacion_Proveedores, 
        ProveedorAnswer, exclude=('pregunta',), 
        extra=0, can_delete=False)

ReclamacionFormset = inlineformset_factory(Reclamacion, Asignacion_Reclamacion, ReclamacionForm, extra=1, can_delete=False)





