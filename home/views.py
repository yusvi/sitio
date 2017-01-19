from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .forms import *
from django.forms import ModelForm
from django.shortcuts import redirect
#from django.template import RequestContext
from django.db import connection
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.db.models import Count
from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
#from django.shortcuts import HttpResponse, render_to_response, RequestContext, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from extra_views import FormSetView, ModelFormSetView, InlineFormSetView, InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, CalendarMonthView, NamedFormsetsMixin, SortableListMixin, SearchableListMixin
from extra_views import NamedFormsetsMixin
from django.forms.models import inlineformset_factory
from extra_views.generic import GenericInlineFormSet, GenericInlineFormSetView


from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView



class indexView(TemplateView):
	template_name = 'index.html'








def verResumenGeneral(request, template_name='index.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(organizacion_id) as Total from home_encuestado where proceso_id=2;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('select count(id) as Total from home_reclamacion;')

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select count(id) as Total from home_evaluacion_proveedores;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor6 = connection.cursor()
        cursor6.execute('select count(id) as Total from home_peticion;')
        
                        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)




        cursor7 = connection.cursor()
        cursor7.execute('select count(id) as Total from home_problema;')
        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('select count(id) as Total from home_general_configuracion;')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)



        cursor9 = connection.cursor()
        cursor9.execute('select count(id) as Total from home_solicitud_cambio;')
        
        persons9 = cursor9.fetchall() 

        x9 = cursor9.description
        resultsList9 = []   
        for r9 in persons9:
            i = 0
            d = {}
            while i < len(x9):
                d[x9[i][0]] = r9[i]
                i = i+1
            resultsList9.append(d)






        cursor10 = connection.cursor()
        cursor10.execute('SELECT year(fecha_encuesta) as ano FROM home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('SELECT COUNT(id) as total FROM home_encuestado where proceso_id=2  group BY year(fecha_encuesta);')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)





        cursor12 = connection.cursor()
        cursor12.execute('SELECT year(fecha_encuesta) as ano, COUNT(id) as total, if(COUNT(id)>2,"Aprobado","No aprobado") as objetivo FROM home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)




          
        context_dict={}

        context_dict['encuestado']=resultsList3
        context_dict['reclamacion']=resultsList4
        context_dict['evaluacion']=resultsList5
        context_dict['peticion']=resultsList6
        context_dict['problema']=resultsList7
        context_dict['ec']=resultsList8
        context_dict['cambio']=resultsList9
        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        context_dict['values2']=resultsList12 

        

        return render(request, template_name, context_dict )








def verResumenRelacion(request, template_name='Procesos/informes/index2.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(organizacion_id) as Total from home_encuestado where proceso_id=2;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select count(id) as Total from home_evaluacion_proveedores;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('SELECT year(fecha_encuesta) as ano FROM home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('SELECT COUNT(id) as total FROM home_encuestado where proceso_id=2  group BY year(fecha_encuesta);')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)





        cursor12 = connection.cursor()
        cursor12.execute('SELECT year(fecha_encuesta) as ano, COUNT(id) as total, if(COUNT(id)>2,"Aprobado","No aprobado") as objetivo FROM home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('SELECT year(fecha_registro) as ano, avg(calificacion) as promedio, if(avg(calificacion)>70,"Aprobado","No aprobado") as objetivo FROM home_evaluacion_proveedores where proceso_id=5 group by year(fecha_registro);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)




        cursor14 = connection.cursor()
        cursor14.execute('SELECT year(fecha_registro) as ano FROM home_evaluacion_proveedores where proceso_id=5 group by year(fecha_registro);')
                        
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)


        cursor15 = connection.cursor()
        cursor15.execute('SELECT avg(calificacion) as promedio FROM home_evaluacion_proveedores where proceso_id=5 group by year(fecha_registro);')
        
        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)




          
        context_dict={}

        context_dict['encuestado']=resultsList3
        context_dict['evaluacion']=resultsList5

        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        context_dict['clientes']=resultsList12
        context_dict['proveedores']=resultsList13
        context_dict['labels2']=resultsList14
        context_dict['values2']=resultsList15

        

        return render(request, template_name, context_dict )



def verResumenRelacion2(request, template_name='Procesos/informes/index22.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(organizacion_id) as Total from home_encuestado where proceso_id=2;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select count(id) as Total from home_evaluacion_proveedores;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('SELECT year(fecha_encuesta) as ano FROM home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('SELECT COUNT(id) as total FROM home_encuestado where proceso_id=2  group BY year(fecha_encuesta);')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)





        cursor12 = connection.cursor()
        cursor12.execute('SELECT year(fecha_encuesta) as ano, COUNT(id) as total, if(COUNT(id)>2,"Aprobado","No aprobado") as objetivo FROM home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('SELECT year(fecha_registro) as ano, avg(calificacion) as promedio, if(avg(calificacion)>70,"Aprobado","No aprobado") as objetivo FROM home_evaluacion_proveedores where proceso_id=5 group by year(fecha_registro);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)




        cursor14 = connection.cursor()
        cursor14.execute('SELECT year(fecha_registro) as ano FROM home_evaluacion_proveedores where proceso_id=5 group by year(fecha_registro);')
                        
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)


        cursor15 = connection.cursor()
        cursor15.execute('SELECT avg(calificacion) as promedio FROM home_evaluacion_proveedores where proceso_id=5 group by year(fecha_registro);')
        
        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)




          
        context_dict={}

        context_dict['encuestado']=resultsList3
        context_dict['evaluacion']=resultsList5

        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        context_dict['clientes']=resultsList12
        context_dict['proveedores']=resultsList13
        context_dict['labels2']=resultsList14
        context_dict['values2']=resultsList15

        

        return render(request, template_name, context_dict )






def verResumenResolucion(request, template_name='Procesos/informes/index3.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(id) as Total from home_peticion;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select count(id) as Total from home_problema;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('select monthname(c.fecha_cierre) as mes, year(c.fecha_cierre) as ano from home_acuerdo_sla l, home_cierre_peticion c, home_peticion a where l.peticion_id = a.id and c.peticion_id = a.id group by month(c.fecha_cierre), year(c.fecha_cierre)')

                         
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('select count(c.fecha_cierre) as total from home_acuerdo_sla l, home_cierre_peticion c, home_peticion a where l.peticion_id = a.id and c.peticion_id = a.id group by month(c.fecha_cierre), year(c.fecha_cierre)')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)



        cursor12 = connection.cursor()
        cursor12.execute('SELECT monthname(c.fecha_cierre) as mes, year(c.fecha_cierre) as ano, if(DATEDIFF(l.fecha_solucion, c.fecha_cierre)>0, "Cumplido", "No cumplido") as objetivo, count(DATEDIFF(l.fecha_solucion, c.fecha_cierre)) as total from home_acuerdo_sla l, home_cierre_peticion c, home_peticion a  where l.peticion_id = a.id and c.peticion_id = a.id group by month(c.fecha_cierre), year(c.fecha_cierre), objetivo')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('select monthname(a.fecha_inicio) as mes, year(a.fecha_inicio) as ano from home_asignacion_problema a group by year(a.fecha_inicio), month(a.fecha_inicio);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)




        cursor14 = connection.cursor()
        cursor14.execute('select count(a.fecha_inicio) as inicio from home_asignacion_problema a group by year(a.fecha_inicio), month(a.fecha_inicio);')
                         
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)


        cursor15 = connection.cursor()
        cursor15.execute('select * from (select monthname(a.fecha_inicio) as mes, year(a.fecha_inicio) as ano, count(a.fecha_inicio) as inicio from home_asignacion_problema a group by year(a.fecha_inicio), month(a.fecha_inicio)) as A LEFT OUTER JOIN (select monthname(a.fecha_inicio) as mes2, year(a.fecha_inicio) as ano2, count(a.fecha_inicio) as cierre from home_asignacion_problema a, home_cierre_problema c where a.problema_id=c.problema_id group by year(a.fecha_inicio), month(a.fecha_inicio)) as B on A.mes=B.mes2;')

        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)




          
        context_dict={}

        context_dict['peticion']=resultsList3
        context_dict['problema']=resultsList5

        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        context_dict['tabla1']=resultsList12
        
        context_dict['labels2']=resultsList13
        context_dict['values2']=resultsList14
        context_dict['tabla2']=resultsList15

        

        return render(request, template_name, context_dict )





def verResumenResolucion2(request, template_name='Procesos/informes/index33.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(id) as Total from home_peticion;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select count(id) as Total from home_problema;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('select monthname(c.fecha_cierre) as mes, year(c.fecha_cierre) as ano from home_acuerdo_sla l, home_cierre_peticion c, home_peticion a where l.peticion_id = a.id and c.peticion_id = a.id group by month(c.fecha_cierre), year(c.fecha_cierre)')

                         
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('select count(c.fecha_cierre) as total from home_acuerdo_sla l, home_cierre_peticion c, home_peticion a where l.peticion_id = a.id and c.peticion_id = a.id group by month(c.fecha_cierre), year(c.fecha_cierre)')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)



        cursor12 = connection.cursor()
        cursor12.execute('SELECT monthname(c.fecha_cierre) as mes, year(c.fecha_cierre) as ano, if(DATEDIFF(l.fecha_solucion, c.fecha_cierre)>0, "Cumplido", "No cumplido") as objetivo, count(DATEDIFF(l.fecha_solucion, c.fecha_cierre)) as total from home_acuerdo_sla l, home_cierre_peticion c, home_peticion a  where l.peticion_id = a.id and c.peticion_id = a.id group by month(c.fecha_cierre), year(c.fecha_cierre), objetivo')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('select monthname(a.fecha_inicio) as mes, year(a.fecha_inicio) as ano from home_asignacion_problema a group by year(a.fecha_inicio), month(a.fecha_inicio);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)




        cursor14 = connection.cursor()
        cursor14.execute('select count(a.fecha_inicio) as inicio from home_asignacion_problema a group by year(a.fecha_inicio), month(a.fecha_inicio);')
                         
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)


        cursor15 = connection.cursor()
        cursor15.execute('select * from (select monthname(a.fecha_inicio) as mes, year(a.fecha_inicio) as ano, count(a.fecha_inicio) as inicio from home_asignacion_problema a group by year(a.fecha_inicio), month(a.fecha_inicio)) as A LEFT OUTER JOIN (select monthname(a.fecha_inicio) as mes2, year(a.fecha_inicio) as ano2, count(a.fecha_inicio) as cierre from home_asignacion_problema a, home_cierre_problema c where a.problema_id=c.problema_id group by year(a.fecha_inicio), month(a.fecha_inicio)) as B on A.mes=B.mes2;')

        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)




          
        context_dict={}

        context_dict['peticion']=resultsList3
        context_dict['problema']=resultsList5

        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        context_dict['tabla1']=resultsList12
        
        context_dict['labels2']=resultsList13
        context_dict['values2']=resultsList14
        context_dict['tabla2']=resultsList15

        

        return render(request, template_name, context_dict )






def verResumenControl(request, template_name='Procesos/informes/index4.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(id) as Total from home_general_configuracion;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select monthname(a.fecha_registro) as mes, year(a.fecha_registro) as ano, count(a.fecha_registro) as registro from home_general_configuracion a group by year(a.fecha_registro), month(a.fecha_registro);')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('select monthname(a.fecha_registro) as mes, year(a.fecha_registro) as ano from home_general_configuracion a group by year(a.fecha_registro), month(a.fecha_registro);')
                         
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('select count(a.fecha_registro) as registro from home_general_configuracion a group by year(a.fecha_registro), month(a.fecha_registro);')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)



        cursor12 = connection.cursor()
        cursor12.execute('select count(id) as Total from home_solicitud_cambio;')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('SELECT year(fecha) as ano, monthname(fecha) as mes, COUNT(id) as total, if(COUNT(id)>=5,"Cumplido","No cumplido") as objetivo FROM home_solicitud_cambio group by year(fecha), month(fecha);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)




        cursor14 = connection.cursor()
        cursor14.execute('SELECT year(fecha) as ano, monthname(fecha) as mes FROM home_solicitud_cambio group by year(fecha), month(fecha);')
                         
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)


        cursor15 = connection.cursor()
        cursor15.execute('SELECT COUNT(id) as total FROM home_solicitud_cambio group by year(fecha), month(fecha);')

        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)




          
        context_dict={}

        context_dict['ec']=resultsList3
        context_dict['tabla0']=resultsList5

        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        
        context_dict['cambio']=resultsList12
        context_dict['tabla1']=resultsList13
        
        context_dict['labels2']=resultsList14
        context_dict['values2']=resultsList15

        

        return render(request, template_name, context_dict )





def verResumenControl2(request, template_name='Procesos/informes/index44.html'):


        cursor3 = connection.cursor()
        cursor3.execute('select count(id) as Total from home_general_configuracion;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('select monthname(a.fecha_registro) as mes, year(a.fecha_registro) as ano, count(a.fecha_registro) as registro from home_general_configuracion a group by year(a.fecha_registro), month(a.fecha_registro);')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('select monthname(a.fecha_registro) as mes, year(a.fecha_registro) as ano from home_general_configuracion a group by year(a.fecha_registro), month(a.fecha_registro);')
                         
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)


        cursor11 = connection.cursor()
        cursor11.execute('select count(a.fecha_registro) as registro from home_general_configuracion a group by year(a.fecha_registro), month(a.fecha_registro);')
        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)



        cursor12 = connection.cursor()
        cursor12.execute('select count(id) as Total from home_solicitud_cambio;')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('SELECT year(fecha) as ano, monthname(fecha) as mes, COUNT(id) as total, if(COUNT(id)>=5,"Cumplido","No cumplido") as objetivo FROM home_solicitud_cambio group by year(fecha), month(fecha);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)




        cursor14 = connection.cursor()
        cursor14.execute('SELECT year(fecha) as ano, monthname(fecha) as mes FROM home_solicitud_cambio group by year(fecha), month(fecha);')
                         
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)


        cursor15 = connection.cursor()
        cursor15.execute('SELECT COUNT(id) as total FROM home_solicitud_cambio group by year(fecha), month(fecha);')

        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)




          
        context_dict={}

        context_dict['ec']=resultsList3
        context_dict['tabla0']=resultsList5

        context_dict['labels']=resultsList10
        context_dict['values']=resultsList11
        
        context_dict['cambio']=resultsList12
        context_dict['tabla1']=resultsList13
        
        context_dict['labels2']=resultsList14
        context_dict['values2']=resultsList15

        

        return render(request, template_name, context_dict )




	
	
class Configuracion_View(TemplateView):
    template_name = 'Procesos/Configuracion/configuracion.html'

class Cambios_View(TemplateView):
    template_name = 'Procesos/Cambios/cambios.html'

class Peticiones_View(TemplateView):
    template_name = 'Procesos/Peticiones/peticiones.html'

class Problemas_View(TemplateView):
    template_name = 'Procesos/Problemas/problemas.html'

class Proveedores_View(TemplateView):
    template_name = 'Procesos/Proveedores/proveedores.html'

class Clientes_View(TemplateView):
    template_name = 'Procesos/Clientes/clientes.html'

class Seguridad_View(TemplateView):
    template_name = 'Procesos/Seguridad/seguridad.html'

def newClasificacion(request, template_name='Procesos/Configuracion/nuevaClasificacion.html'):
        form = ClasificacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_clasificacion')
        return render(request, template_name, {'form':form})

def verClasificacion(request, template_name='Procesos/Configuracion/mostrarClasificacion.html'):
        clasificaciones = Clasificacion_EC.objects.all().order_by('id')
        data = {'clasificacion' : clasificaciones}
        data['object_list'] = clasificaciones
        return render(request, template_name, data)

def editarClasificacion(request, id, template_name='Procesos/Configuracion/editarClasificacion.html'):
        clasificacion = get_object_or_404(Clasificacion_EC, pk=id)
        form = ClasificacionForm(request.POST or None, instance=clasificacion)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_clasificacion')

        return render(request, template_name, {'form':form})

def eliminarClasificacion(request, id, template_name='Procesos/Configuracion/eliminarClasificacion.html'):
    clasificacion = get_object_or_404(Clasificacion_EC, pk=id)    
    if request.method=='POST':
        clasificacion.delete()
        return redirect('mostrar_clasificacion')
    return render(request, template_name, {'object':clasificacion})

def newEC(request, template_name='Procesos/Configuracion/nuevoEC.html'):
        form = ECForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_ec')
        return render(request, template_name, {'form':form})

def verEC(request, template_name='Procesos/Configuracion/mostrarEC.html'):
        ecs = EC.objects.all().order_by('id')
        data = {'ec' : ecs}
        data['object_list'] = ecs
        return render(request, template_name, data)

def editarEC(request, id, template_name='Procesos/Configuracion/editarEC.html'):
        ec = get_object_or_404(EC, pk=id)
        form = ECForm(request.POST or None, instance=ec)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_ec')

        return render(request, template_name, {'form':form})

def eliminarEC(request, id, template_name='Procesos/Configuracion/eliminarEC.html'):
    ec = get_object_or_404(EC, pk=id)    
    if request.method=='POST':
        ec.delete()
        return redirect('mostrar_ec')
    return render(request, template_name, {'object':ec})

def newOrganizacion(request, template_name='Procesos/Configuracion/nuevaOrganizacion.html'):
        form = OrganizacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_organizacion')
        return render(request, template_name, {'form':form})

def verOrganizacion(request, template_name='Procesos/Configuracion/mostrarOrganizacion.html'):
        organizaciones = Organizacion.objects.all().order_by('id')
        data = {'organizacion' : organizaciones}
        data['object_list'] = organizaciones
        return render(request, template_name, data)

def editarOrganizacion(request, id, template_name='Procesos/Configuracion/editarOrganizacion.html'):
        organizacion = get_object_or_404(Organizacion, pk=id)
        form = OrganizacionForm(request.POST or None, instance=organizacion)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_organizacion')

        return render(request, template_name, {'form':form})

def eliminarOrganizacion(request, id, template_name='Procesos/Configuracion/eliminarOrganizacion.html'):
    organizacion = get_object_or_404(Organizacion, pk=id)    
    if request.method=='POST':
        organizacion.delete()
        return redirect('mostrar_organizacion')
    return render(request, template_name, {'object':organizacion})

def newLocalidad(request, template_name='Procesos/Configuracion/nuevaLocalidad.html'):
        form = LocalidadForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_localidad')
        return render(request, template_name, {'form':form})

def verLocalidad(request, template_name='Procesos/Configuracion/mostrarLocalidad.html'):
        localidades = Localidad.objects.all().order_by('id')
        data = {'localidad' : localidades}
        data['object_list'] = localidades
        return render(request, template_name, data)

def editarLocalidad(request, id, template_name='Procesos/Configuracion/editarLocalidad.html'):
        localidad = get_object_or_404(Localidad, pk=id)
        form = LocalidadForm(request.POST or None, instance=localidad)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_localidad')

        return render(request, template_name, {'form':form})

def eliminarLocalidad(request, id, template_name='Procesos/Configuracion/eliminarLocalidad.html'):
    localidad= get_object_or_404(Localidad, pk=id)    
    if request.method=='POST':
        localidad.delete()
        return redirect('mostrar_localidad')
    return render(request, template_name, {'object':localidad})

def newGrupo(request, template_name='Procesos/Configuracion/nuevoGrupo.html'):
        form = GrupoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_grupo')
        return render(request, template_name, {'form':form})

def verGrupo(request, template_name='Procesos/Configuracion/mostrarGrupo.html'):
        grupos = Grupo_EC.objects.all().order_by('id')
        data = {'grupo' : grupos}
        data['object_list'] = grupos
        return render(request, template_name, data)

def editarGrupo(request, id, template_name='Procesos/Configuracion/editarGrupo.html'):
        grupo = get_object_or_404(Grupo_EC, pk=id)
        form = GrupoForm(request.POST or None, instance=grupo)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_grupo')

        return render(request, template_name, {'form':form})

def eliminarGrupo(request, id, template_name='Procesos/Configuracion/eliminarGrupo.html'):
    grupo= get_object_or_404(Grupo_EC, pk=id)    
    if request.method=='POST':
        grupo.delete()
        return redirect('mostrar_grupo')
    return render(request, template_name, {'object':grupo})

def newGeneral(request, template_name='Procesos/Configuracion/nuevoGeneral.html'):
        form = GeneralForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_general')
        return render(request, template_name, {'form':form})

def verGeneral(request, template_name='Procesos/Configuracion/mostrarGeneral.html'):
        generales = General_Configuracion.objects.all().order_by('id')
        data = {'general' : generales}
        data['object_list'] = generales
        return render(request, template_name, data)

def editarGeneral(request, id, template_name='Procesos/Configuracion/editarGeneral.html'):
        general = get_object_or_404(General_Configuracion, pk=id)
        form = GeneralForm(request.POST or None, instance=general)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_general')

        return render(request, template_name, {'form':form})

def eliminarGeneral(request, id, template_name='Procesos/Configuracion/eliminarGeneral.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    
    if request.method=='POST':
        general.delete()
        return redirect('mostrar_general')
    return render(request, template_name, {'object':general})



def newMarca(request, template_name='Procesos/Configuracion/nuevaMarca.html'):
        form = MarcaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_marca')
        return render(request, template_name, {'form':form})

def verMarca(request, template_name='Procesos/Configuracion/mostrarMarca.html'):
        marcas = Marca.objects.all().order_by('id')
        data = {'marca' : marcas}
        data['object_list'] = marcas
        return render(request, template_name, data)

def editarMarca(request, id, template_name='Procesos/Configuracion/editarMarca.html'):
        marca = get_object_or_404(Marca, pk=id)
        form = MarcaForm(request.POST or None, instance=marca)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_marca')

        return render(request, template_name, {'form':form})

def eliminarMarca(request, id, template_name='Procesos/Configuracion/eliminarMarca.html'):
    marca= get_object_or_404(Marca, pk=id)    
    if request.method=='POST':
        marca.delete()
        return redirect('mostrar_marca')
    return render(request, template_name, {'object':marca})

def newModelo(request, template_name='Procesos/Configuracion/nuevoModelo.html'):
        form = ModeloForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_modelo')
        return render(request, template_name, {'form':form})

def verModelo(request, template_name='Procesos/Configuracion/mostrarModelo.html'):
        modelos = Modelo.objects.all().order_by('id')
        data = {'modelo' : modelos}
        data['object_list'] = modelos
        return render(request, template_name, data)

def editarModelo(request, id, template_name='Procesos/Configuracion/editarModelo.html'):
        modelos = get_object_or_404(Modelo, pk=id)
        form = ModeloForm(request.POST or None, instance=modelos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_modelo')

        return render(request, template_name, {'form':form})

def eliminarModelo(request, id, template_name='Procesos/Configuracion/eliminarModelo.html'):
    modelo= get_object_or_404(Modelo, pk=id)    
    if request.method=='POST':
        modelo.delete()
        return redirect('mostrar_modelo')
    return render(request, template_name, {'object':modelo})

def newRed(request, template_name='Procesos/Configuracion/nuevaRed.html'):
        form = RedForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_red')
        return render(request, template_name, {'form':form})

def verRed(request, template_name='Procesos/Configuracion/mostrarRed.html'):
        redes = Red.objects.all().order_by('id')
        data = {'red' : redes}
        data['object_list'] = redes
        return render(request, template_name, data)

def editarRed(request, id, template_name='Procesos/Configuracion/editarRed.html'):
        redes = get_object_or_404(Red, pk=id)
        form = RedForm(request.POST or None, instance=redes)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_red')

        return render(request, template_name, {'form':form})

def eliminarRed(request, id, template_name='Procesos/Configuracion/eliminarRed.html'):
    red= get_object_or_404(Red, pk=id)    
    if request.method=='POST':
        red.delete()
        return redirect('mostrar_red')
    return render(request, template_name, {'object':red})

def newSoftware(request, template_name='Procesos/Configuracion/nuevoSoftware.html'):
        form = SoftwareForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_software')
        return render(request, template_name, {'form':form})

def verSoftware(request, template_name='Procesos/Configuracion/mostrarSoftware.html'):
        softwares = SO_Programa.objects.all().order_by('id')
        data = {'software' : softwares}
        data['object_list'] = softwares
        return render(request, template_name, data)

def editarSoftware(request, id, template_name='Procesos/Configuracion/editarSoftware.html'):
        softwares = get_object_or_404(SO_Programa, pk=id)
        form = SoftwareForm(request.POST or None, instance=softwares)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_software')

        return render(request, template_name, {'form':form})

def eliminarSoftware(request, id, template_name='Procesos/Configuracion/eliminarSoftware.html'):
    software= get_object_or_404(SO_Programa, pk=id)    
    if request.method=='POST':
        software.delete()
        return redirect('mostrar_software')
    return render(request, template_name, {'object':software})

def newVersion(request, template_name='Procesos/Configuracion/nuevaVersion.html'):
        form = VersionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_version')
        return render(request, template_name, {'form':form})

def verVersion(request, template_name='Procesos/Configuracion/mostrarVersion.html'):
        versiones = Version.objects.all().order_by('id')
        data = {'version' : versiones}
        data['object_list'] = versiones
        return render(request, template_name, data)

def editarVersion(request, id, template_name='Procesos/Configuracion/editarVersion.html'):
        versiones = get_object_or_404(Version, pk=id)
        form = VersionForm(request.POST or None, instance=versiones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_version')

        return render(request, template_name, {'form':form})

def eliminarVersion(request, id, template_name='Procesos/Configuracion/eliminarVersion.html'):
    version= get_object_or_404(Version, pk=id)    
    if request.method=='POST':
        version.delete()
        return redirect('mostrar_version')
    return render(request, template_name, {'object':version})

def newImpresora(request, template_name='Procesos/Configuracion/nuevaImpresora.html'):
        form = ImpresoraForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_impresora')
        return render(request, template_name, {'form':form})






def verImpresora(request, template_name='Procesos/Configuracion/mostrarImpresora.html'):

        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_impresora i where i.general_id=g.id) as impresora, (select i.nombre_impresora from home_impresora i where i.general_id=g.id) as nombre_impresora, (select i.numero_serie from home_impresora i where i.general_id=g.id) as numero_serie, (SELECT m.nombre_marca from home_marca m, home_impresora i  where m.id = i.marca_id and i.general_id=g.id) as marca, (SELECT d.nombre_modelo from home_modelo d, home_impresora i  where d.id = i.modelo_id and i.general_id=g.id) as modelo from home_general_configuracion g where g.nombre_ec_id=9;')

        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )








def editarImpresora(request, id, template_name='Procesos/Configuracion/editarImpresora.html'):
        impresoras = get_object_or_404(Impresora, pk=id)
        form = ImpresoraForm(request.POST or None, instance=impresoras)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_impresora')

        return render(request, template_name, {'form':form})

def eliminarImpresora(request, id, template_name='Procesos/Configuracion/eliminarImpresora.html'):

    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_impresora')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_impresora')

    return render(request, template_name, {'object':general})




def newGranja(request, template_name='Procesos/Configuracion/nuevaGranja.html'):
        form = GranjaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_granja')
        return render(request, template_name, {'form':form})

def verGranja(request, template_name='Procesos/Configuracion/mostrarGranja.html'):

        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_granja i where i.general_id=g.id) as granja, (select i.nombre_granja from home_granja i where i.general_id=g.id) as nombre_granja from home_general_configuracion g where g.nombre_ec_id=4;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )




def editarGranja(request, id, template_name='Procesos/Configuracion/editarGranja.html'):
        granjas = get_object_or_404(Granja, pk=id)
        form = GranjaForm(request.POST or None, instance=granjas)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_granja')

        return render(request, template_name, {'form':form})

def eliminarGranja(request, id, template_name='Procesos/Configuracion/eliminarGranja.html'):
        
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_granja')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_granja')

    return render(request, template_name, {'object':general})





def newLicencia(request, template_name='Procesos/Configuracion/nuevaLicencia.html'):
        form = LicenciaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_licencia')
        return render(request, template_name, {'form':form})

def verLicencia(request, template_name='Procesos/Configuracion/mostrarLicencia.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_licencia i where i.general_id=g.id) as licencia, (select i.nombre_licencia from home_licencia i where i.general_id=g.id) as nombre, (select i.cantidad from home_licencia i where i.general_id=g.id) as cantidad, (SELECT p.nombre_ec from home_ec p, home_licencia i  where p.id = i.tipo_id and i.general_id=g.id) as tipo, (select i.llave from home_licencia i where i.general_id=g.id) as llave, (select i.fecha_inicio from home_licencia i where i.general_id=g.id) as inicio, (select i.fecha_fin from home_licencia i where i.general_id=g.id) as fin, (SELECT p.nombre_software from home_so_programa p, home_licencia i  where p.id = i.software_id and i.general_id=g.id) as software, (SELECT p.nombre_version from home_version p, home_licencia i where p.id = i.version_id and i.general_id=g.id) as version from home_general_configuracion g where g.nombre_ec_id=11;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarLicencia(request, id, template_name='Procesos/Configuracion/editarLicencia.html'):
        licencias = get_object_or_404(Licencia, pk=id)
        form = LicenciaForm(request.POST or None, instance=licencias)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_licencia')

        return render(request, template_name, {'form':form})

def eliminarLicencia(request, id, template_name='Procesos/Configuracion/eliminarLicencia.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_licencia')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_licencia')

    return render(request, template_name, {'object':general})


def newMaquina(request, template_name='Procesos/Configuracion/nuevaMaquina.html'):
        form = MaquinaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_maquina')
        return render(request, template_name, {'form':form})

def verMaquina(request, template_name='Procesos/Configuracion/mostrarMaquina.html'):

        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_maquina_virtual i where i.general_id=g.id) as maquina, (select i.nombre_maquina from home_maquina_virtual i where i.general_id=g.id) as nombre_maquina, (select i.ip from home_maquina_virtual i where i.general_id=g.id) as ip, (select i.cpu from home_maquina_virtual i where i.general_id=g.id) as cpu, (select i.ram from home_maquina_virtual i where i.general_id=g.id) as ram, (SELECT p.nombre_granja from home_granja p, home_maquina_virtual i  where p.id = i.granja_id and i.general_id=g.id) as granja, (SELECT p.nombre_licencia from home_licencia p, home_maquina_virtual i  where p.id = i.licencia_id and i.general_id=g.id) as licencia, (SELECT p.nombre_software from home_so_programa p, home_maquina_virtual i  where p.id = i.software_id and i.general_id=g.id) as software from home_general_configuracion g where g.nombre_ec_id=6')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )



def editarMaquina(request, id, template_name='Procesos/Configuracion/editarMaquina.html'):
        maquinas = get_object_or_404(Maquina_Virtual, pk=id)
        form = MaquinaForm(request.POST or None, instance=maquinas)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_maquina')

        return render(request, template_name, {'form':form})

def eliminarMaquina(request, id, template_name='Procesos/Configuracion/eliminarMaquina.html'):
        
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_maquina')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_maquina')

    return render(request, template_name, {'object':general})




def newVlan(request, template_name='Procesos/Configuracion/nuevaVlan.html'):
        form = VlanForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_vlan')
        return render(request, template_name, {'form':form})

def verVlan(request, template_name='Procesos/Configuracion/mostrarVlan.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_vlan i where i.general_id=g.id) as vlan, (select i.nombre_vlan from home_vlan i where i.general_id=g.id) as nombre,  (select i.descripcion from home_vlan i where i.general_id=g.id) as descripcion  from home_general_configuracion g where g.nombre_ec_id=13;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarVlan(request, id, template_name='Procesos/Configuracion/editarVlan.html'):
        vlans = get_object_or_404(Vlan, pk=id)
        form = VlanForm(request.POST or None, instance=vlans)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_vlan')

        return render(request, template_name, {'form':form})

def eliminarVlan(request, id, template_name='Procesos/Configuracion/eliminarVlan.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_vlan')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_vlan')

    return render(request, template_name, {'object':general})


def verContacto(request, template_name='Procesos/Configuracion/mostrarContacto.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_cliente_empleado i where i.general_id=g.id) as contacto, (select i.nombre_contacto from home_cliente_empleado i where i.general_id=g.id) as nombre, (select i.apellido_contacto from home_cliente_empleado i where i.general_id=g.id) as apellido, (SELECT p.contacto from home_tipo_contacto p, home_cliente_empleado i where p.id = i.tipo_contacto_id and i.general_id=g.id) as tipo, (SELECT p.nombre_organizacion from home_organizacion p, home_cliente_empleado i where p.id = i.organizacion_id and i.general_id=g.id) as organizacion, (SELECT p.nombre_grupo from home_grupo_ec p, home_cliente_empleado i where p.id = i.grupo_id and i.general_id=g.id) as area,  (select i.correo from home_cliente_empleado i where i.general_id=g.id) as correo from home_general_configuracion g where g.nombre_ec_id=14')


                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )




def editarContacto(request, id, template_name='Procesos/Configuracion/editarContacto.html'):
        contactos = get_object_or_404(Cliente_Empleado, pk=id)
        form = ContactoForm(request.POST or None, instance=contactos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_contacto')

        return render(request, template_name, {'form':form})

def eliminarContacto(request, id, template_name='Procesos/Configuracion/eliminarContacto.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_contacto')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_contacto')

    return render(request, template_name, {'object':general})




def newPC(request, template_name='Procesos/Configuracion/nuevaPC.html'):
        form = PCForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_pc')
        return render(request, template_name, {'form':form})

def verPC(request, template_name='Procesos/Configuracion/mostrarPC.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_pc_laptop i where i.general_id=g.id) as pc, (select i.nombre_equipo from home_pc_laptop i where i.general_id=g.id) as nombre, (SELECT i.nombre_organizacion from home_organizacion i, home_pc_laptop p where i.id =p.organizacion_id and p.general_id=g.id) as organizacion, (SELECT i.nombre_contacto from home_cliente_empleado i, home_pc_laptop p where i.id = p.contacto_id and p.general_id=g.id) as nombre_contacto, (SELECT i.apellido_contacto from home_cliente_empleado i, home_pc_laptop p where i.id = p.contacto_id and p.general_id=g.id) as apellido_contacto, (SELECT i.nombre_marca from home_marca i, home_pc_laptop p where i.id = p.marca_id and p.general_id=g.id) as marca, (SELECT i.nombre_modelo from home_modelo i, home_pc_laptop p where i.id = p.modelo_id and p.general_id=g.id) as modelo, (select i.cpu from home_pc_laptop i where i.general_id=g.id) as cpu, (select i.ram from home_pc_laptop i where i.general_id=g.id) as ram, (select i.numero_serie from home_pc_laptop i where i.general_id=g.id) as serie from home_general_configuracion g where g.nombre_ec_id=7;')
                       

                       
     
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarPC(request, id, template_name='Procesos/Configuracion/editarPC.html'):
        pcs = get_object_or_404(PC_Laptop, pk=id)
        form = PCForm(request.POST or None, instance=pcs)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_pc')

        return render(request, template_name, {'form':form})

def eliminarPC(request, id, template_name='Procesos/Configuracion/eliminarPC.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_pc')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_pc')

    return render(request, template_name, {'object':general})




def newInstalacion(request, template_name='Procesos/Configuracion/nuevaInstalacion.html'):
        form = InstalacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_instalacion')
        return render(request, template_name, {'form':form})

def verInstalacion(request, template_name='Procesos/Configuracion/mostrarInstalacion.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_instalacion_software i where i.general_id=g.id) as instalacion, (SELECT i.nombre_licencia from home_licencia i, home_instalacion_software p where i.id =p.licencia_id and p.general_id=g.id) as licencia, (SELECT i.nombre_equipo from home_pc_laptop i, home_instalacion_software p where i.id = p.pc_laptop_id and p.general_id=g.id) as pc, (SELECT i.nombre_software from home_so_programa i, home_instalacion_software p where i.id = p.software_id and p.general_id=g.id) as software, (SELECT i.nombre_version from home_version i, home_instalacion_software p where i.id = p.version_id and p.general_id=g.id) as version from home_general_configuracion g where g.nombre_ec_id=10;')
     
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarInstalacion(request, id, template_name='Procesos/Configuracion/editarInstalacion.html'):
        instalaciones = get_object_or_404(Instalacion_Software, pk=id)
        form = InstalacionForm(request.POST or None, instance=instalaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_instalacion')

        return render(request, template_name, {'form':form})

def eliminarInstalacion(request, id, template_name='Procesos/Configuracion/eliminarInstalacion.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_instalacion')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_instalacion')

    return render(request, template_name, {'object':general})


def newRack(request, template_name='Procesos/Configuracion/nuevoRack.html'):
        form = RackForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_rack')
        return render(request, template_name, {'form':form})

def verRack(request, template_name='Procesos/Configuracion/mostrarRack.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_rack i where i.general_id=g.id) as rack, (select i.nombre_rack from home_rack i where i.general_id=g.id) as nombre, (select i.unidades_rack from home_rack i where i.general_id=g.id) as unidades, (SELECT i.nombre_marca from home_marca i, home_rack p where i.id = p.marca_id and p.general_id=g.id) as marca, (SELECT i.nombre_modelo from home_modelo i, home_rack p where i.id = p.modelo_id and p.general_id=g.id) as modelo from home_general_configuracion g where g.nombre_ec_id=1;')

        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )




def editarRack(request, id, template_name='Procesos/Configuracion/editarRack.html'):
        racks = get_object_or_404(Rack, pk=id)
        form = RackForm(request.POST or None, instance=racks)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_rack')

        return render(request, template_name, {'form':form})

def eliminarRack(request, id, template_name='Procesos/Configuracion/eliminarRack.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_rack')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_rack')

    return render(request, template_name, {'object':general})


def newServidor(request, template_name='Procesos/Configuracion/nuevoServidor.html'):
        form = ServidorForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_servidor')
        return render(request, template_name, {'form':form})

def verServidor(request, template_name='Procesos/Configuracion/mostrarServidor.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_servidor i where i.general_id=g.id) as servidor, (select i.nombre_servidor from home_servidor i where i.general_id=g.id) as nombre, (select i.ip from home_servidor i where i.general_id=g.id) as ip, (select i.cpu from home_servidor i where i.general_id=g.id) as cpu, (select i.ram from home_servidor i where i.general_id=g.id) as ram, (SELECT i.nombre_licencia from home_licencia i, home_servidor p where i.id = p.licencia_id and p.general_id=g.id) as licencia, (SELECT i.nombre_marca from home_marca i, home_servidor p where i.id = p.marca_id and p.general_id=g.id) as marca, (SELECT i.nombre_modelo from home_modelo i, home_servidor p where i.id = p.modelo_id and p.general_id=g.id) as modelo, (SELECT i.nombre_software from home_so_programa i, home_servidor p where i.id = p.software_id and p.general_id=g.id) as software, (SELECT i.nombre_version from home_version i, home_servidor p where i.id = p.version_id and p.general_id=g.id) as version from home_general_configuracion g where g.nombre_ec_id=2;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarServidor(request, id, template_name='Procesos/Configuracion/editarServidor.html'):
        servidores = get_object_or_404(Servidor, pk=id)
        form = ServidorForm(request.POST or None, instance=servidores)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_servidor')

        return render(request, template_name, {'form':form})

def eliminarServidor(request, id, template_name='Procesos/Configuracion/eliminarServidor.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_servidor')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_servidor')

    return render(request, template_name, {'object':general})


def newHypervisor(request, template_name='Procesos/Configuracion/nuevoHypervisor.html'):
        form = HypervisorForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_hypervisor')
        return render(request, template_name, {'form':form})

def verHypervisor(request, template_name='Procesos/Configuracion/mostrarHypervisor.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_hypervisor i where i.general_id=g.id) as hypervisor, (select i.nombre_hypervisor from home_hypervisor i where i.general_id=g.id) as nombre, (SELECT i.nombre_granja from home_granja i, home_hypervisor p where i.id = p.granja_id and p.general_id=g.id) as granja, (SELECT i.nombre_servidor from home_servidor i, home_hypervisor p where i.id = p.servidor_id and p.general_id=g.id) as servidor from home_general_configuracion g where g.nombre_ec_id=5;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarHypervisor(request, id, template_name='Procesos/Configuracion/editarHypervisor.html'):
        hypervisores = get_object_or_404(Hypervisor, pk=id)
        form = HypervisorForm(request.POST or None, instance=hypervisores)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_hypervisor')

        return render(request, template_name, {'form':form})

def eliminarHypervisor(request, id, template_name='Procesos/Configuracion/eliminarHypervisor.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_hypervisor')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_hypervisor')

    return render(request, template_name, {'object':general})

def newTelefono(request, template_name='Procesos/Configuracion/nuevoTelefono.html'):
        form = TelefonoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_telefono')
        return render(request, template_name, {'form':form})

def verTelefono(request, template_name='Procesos/Configuracion/mostrarTelefono.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_telefono_celular i where i.general_id=g.id) as telefono, (select i.numero_telefono from home_telefono_celular i where i.general_id=g.id) as numero, (select i.numero_serie from home_telefono_celular i where i.general_id=g.id) as serie, (SELECT i.nombre_marca from home_marca i, home_telefono_celular p where i.id = p.marca_id and p.general_id=g.id) as marca, (SELECT i.nombre_modelo from home_modelo i, home_telefono_celular p where i.id = p.modelo_id and p.general_id=g.id) as modelo, (SELECT i.nombre_organizacion from home_organizacion i, home_telefono_celular p where i.id =p.organizacion_id and p.general_id=g.id) as organizacion, (SELECT i.nombre_contacto from home_cliente_empleado i, home_telefono_celular p where i.id = p.contacto_id and p.general_id=g.id) as nombre, (SELECT i.apellido_contacto from home_cliente_empleado i, home_telefono_celular p where i.id = p.contacto_id and p.general_id=g.id) as apellido from home_general_configuracion g where g.nombre_ec_id=8;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarTelefono(request, id, template_name='Procesos/Configuracion/editarTelefono.html'):
        telefonos = get_object_or_404(Telefono_Celular, pk=id)
        form = TelefonoForm(request.POST or None, instance=telefonos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_telefono')

        return render(request, template_name, {'form':form})

def eliminarTelefono(request, id, template_name='Procesos/Configuracion/eliminarTelefono.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_telefono')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_telefono')

    return render(request, template_name, {'object':general})


def newDispositivo(request, template_name='Procesos/Configuracion/nuevoDispositivo.html'):
        form = DispositivoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_dispositivo')
        return render(request, template_name, {'form':form})

def verDispositivo(request, template_name='Procesos/Configuracion/mostrarDispositivo.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_dispositivo_red i where i.general_id=g.id) as dispositivo, (select i.nombre_dispositivo from home_dispositivo_red i where i.general_id=g.id) as nombre, (select i.ip from home_dispositivo_red i where i.general_id=g.id) as ip, (select i.ram from home_dispositivo_red i where i.general_id=g.id) as ram, (select i.numero_serie from home_dispositivo_red i where i.general_id=g.id) as serie, (SELECT i.nombre_marca from home_marca i, home_dispositivo_red p where i.id = p.marca_id and p.general_id=g.id) as marca, (SELECT i.nombre_modelo from home_modelo i, home_dispositivo_red p where i.id = p.modelo_id and p.general_id=g.id) as modelo, (SELECT i.nombre_software from home_so_programa i, home_dispositivo_red p where i.id = p.software_id and p.general_id=g.id) as software, (SELECT i.nombre_version from home_version i, home_dispositivo_red p where i.id = p.version_id and p.general_id=g.id) as version from home_general_configuracion g where g.nombre_ec_id=3;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarDispositivo(request, id, template_name='Procesos/Configuracion/editarDispositivo.html'):
        dispositivos = get_object_or_404(Dispositivo_Red, pk=id)
        form = DispositivoForm(request.POST or None, instance=dispositivos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_dispositivo')

        return render(request, template_name, {'form':form})

def eliminarDispositivo(request, id, template_name='Procesos/Configuracion/eliminarDispositivo.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_dispositivo')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_dispositivo')

    return render(request, template_name, {'object':general})



def newInterfaz(request, template_name='Procesos/Configuracion/nuevaInterfaz.html'):
        form = InterfazForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_interfaz')
        return render(request, template_name, {'form':form})

def verInterfaz(request, template_name='Procesos/Configuracion/mostrarInterfaz.html'):
        cursor = connection.cursor()
        cursor.execute('select g.id as ec, g.criticidad, (SELECT p.nombre_grupo from home_grupo_ec p where p.id = g.nombre_grupo_id) as grupo, g.fecha_registro, (select i.id from home_interfaz_red i where i.general_id=g.id) as interfaz, (select i.nombre_interfaz from home_interfaz_red i where i.general_id=g.id) as nombre, (select i.ip from home_interfaz_red i where i.general_id=g.id) as ip, (select i.mac from home_interfaz_red i where i.general_id=g.id) as mac, (select i.gateway from home_interfaz_red i where i.general_id=g.id) as gateway, (select i.mascara from home_interfaz_red i where i.general_id=g.id) as mascara, (select i.velocidad from home_interfaz_red i where i.general_id=g.id) as velocidad, (SELECT i.nombre_dispositivo from home_dispositivo_red i, home_interfaz_red p where i.id = p.dispositivo_id and p.general_id=g.id) as dispositivo from home_general_configuracion g  where g.nombre_ec_id=12;')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )


def editarInterfaz(request, id, template_name='Procesos/Configuracion/editarInterfaz.html'):
        interfaces = get_object_or_404(Interfaz_Red, pk=id)
        form = InterfazForm(request.POST or None, instance=interfaces)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_interfaz')

        return render(request, template_name, {'form':form})

def eliminarInterfaz(request, id, template_name='Procesos/Configuracion/eliminarInterfaz.html'):
    general= get_object_or_404(General_Configuracion, pk=id)    

    if 'cancel' in request.POST:
            return redirect('mostrar_interfaz')

    if 'save' in request.POST:
            general.delete()
            return redirect('mostrar_interfaz')

    return render(request, template_name, {'object':general})

def newCambio(request, template_name='Procesos/Cambios/nuevoCambio.html'):
        form = CambioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_cambio')
        return render(request, template_name, {'form':form})

def verCambio(request, template_name='Procesos/Cambios/mostrarCambio.html'):
        cambios = Solicitud_Cambio.objects.all().order_by('id')
        data = {'cambio' : cambios}
        data['object_list'] = cambios


        cursor = connection.cursor()
        cursor.execute('select s.id, s.fecha, s.asunto, s.estimacion_recursos, (SELECT cl.nombre_contacto from home_cliente_empleado cl where cl.id = s.contacto_id) as Nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl where cl.id = s.contacto_id) as Apellido, (SELECT e.estado from home_exclusivo_cambio e where e.folio_id = s.id) as Estado, (SELECT p.reunion_id from home_planificacion_cambio p where p.folio_id=s.id) as Reunion, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_planificacion_cambio p where cl.id = p.coordinador_id and p.folio_id=s.id) as NombreC, (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_planificacion_cambio p where cl.id = p.coordinador_id and p.folio_id=s.id) as ApellidoC, (SELECT COUNT(*) FROM home_responsables_cambio r WHERE r.folio_id = s.id) as Responsables, (SELECT COUNT(*) FROM home_seguimiento_cambio r WHERE r.folio_id = s.id) as Seguimientos, (SELECT v.fecha_verificacion from home_verificacion_cambio v where v.folio_id = s.id) as Fecha_Verificacion, (SELECT v.eficacia from home_verificacion_cambio v where v.folio_id = s.id) as Eficacia from home_solicitud_cambio s')

        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )




def editarCambio(request, id, template_name='Procesos/Cambios/editarCambio.html'):
        cambios = get_object_or_404(Solicitud_Cambio, pk=id)
        form = CambioForm(request.POST or None, instance=cambios)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_cambio')

        return render(request, template_name, {'form':form})

def eliminarCambio(request, id, template_name='Procesos/Cambios/eliminarCambio.html'):

    cambio= get_object_or_404(Solicitud_Cambio, pk=id)

    
    if 'cancel' in request.POST:
            return redirect('mostrar_cambio')

    if 'save' in request.POST:
            peticion.delete()
            return redirect('mostrar_cambio')


    return render(request, template_name, {'object':cambio})







def newExclusivo(request, template_name='Procesos/Cambios/nuevoExclusivo.html'):
        form = ExclusivoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_exclusivo')
        return render(request, template_name, {'form':form})

def verExclusivo(request, template_name='Procesos/Cambios/mostrarExclusivo.html'):
        exclusivos = Exclusivo_Cambio.objects.all().order_by('id')
        data = {'exclusivo' : exclusivos}
        data['object_list'] = exclusivos
        return render(request, template_name, data)

def editarExclusivo(request, id, template_name='Procesos/Cambios/editarExclusivo.html'):
        exclusivos = get_object_or_404(Exclusivo_Cambio, pk=id)
        form = ExclusivoForm(request.POST or None, instance=exclusivos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_exclusivo')

        return render(request, template_name, {'form':form})

def eliminarExclusivo(request, id, template_name='Procesos/Cambios/eliminarExclusivo.html'):
    exclusivo= get_object_or_404(Exclusivo_Cambio, pk=id)    
    if request.method=='POST':
        exclusivo.delete()
        return redirect('mostrar_exclusivo')
    return render(request, template_name, {'object':exclusivo})

def newReunion(request, template_name='Procesos/Cambios/nuevaReunion.html'):
        form = ReunionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_reunion')
        return render(request, template_name, {'form':form})

def verReunion(request, template_name='Procesos/Cambios/mostrarReunion.html'):
        reuniones = Reunion.objects.all().order_by('id')
        data = {'reunion' : reuniones}
        data['object_list'] = reuniones
        return render(request, template_name, data)

def editarReunion(request, id, template_name='Procesos/Cambios/editarReunion.html'):
        reuniones = get_object_or_404(Reunion, pk=id)
        form = ReunionForm(request.POST or None, instance=reuniones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_reunion')

        return render(request, template_name, {'form':form})

def eliminarReunion(request, id, template_name='Procesos/Cambios/eliminarReunion.html'):
    reunion= get_object_or_404(Reunion, pk=id)    
    if request.method=='POST':
        reunion.delete()
        return redirect('mostrar_reunion')
    return render(request, template_name, {'object':reunion})

def newAsistencia(request, template_name='Procesos/Cambios/nuevaAsistencia.html'):
        form = AsistenciaReunionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asistencia')
        return render(request, template_name, {'form':form})

def verAsistencia(request, template_name='Procesos/Cambios/mostrarAsistencia.html'):
        asistencias = Asistencia_Reunion.objects.all().order_by('id')
        data = {'asistencia' : asistencias}
        data['object_list'] = asistencias
        return render(request, template_name, data)

def editarAsistencia(request, id, template_name='Procesos/Cambios/editarAsistencia.html'):
        asistencias = get_object_or_404(Asistencia_Reunion, pk=id)
        form = AsistenciaReunionForm(request.POST or None, instance=asistencias)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_asistencia')

        return render(request, template_name, {'form':form})

def eliminarAsistencia(request, id, template_name='Procesos/Cambios/eliminarAsistencia.html'):
    asistencia= get_object_or_404(Asistencia_Reunion, pk=id)    
    if request.method=='POST':
        asistencia.delete()
        return redirect('mostrar_asistencia')
    return render(request, template_name, {'object':asistencia})

def newPlanificacionCambio(request, template_name='Procesos/Cambios/nuevaPlanificacionCambio.html'):
        form = PlanificacionCambioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_planificacion_cambio')
        return render(request, template_name, {'form':form})

def verPlanificacionCambio(request, template_name='Procesos/Cambios/mostrarPlanificacionCambio.html'):
        planificaciones = Planificacion_Cambio.objects.all().order_by('id')
        data = {'planificacion' : planificaciones}
        data['object_list'] = planificaciones
        return render(request, template_name, data)

def editarPlanificacionCambio(request, id, template_name='Procesos/Cambios/editarPlanificacionCambio.html'):
        planificaciones = get_object_or_404(Planificacion_Cambio, pk=id)
        form = PlanificacionCambioForm(request.POST or None, instance=planificaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_planificacion_cambio')

        return render(request, template_name, {'form':form})

def eliminarPlanificacionCambio(request, id, template_name='Procesos/Cambios/eliminarPlanificacionCambio.html'):
    planificacion= get_object_or_404(Planificacion_Cambio, pk=id)    
    if request.method=='POST':
        planificacion.delete()
        return redirect('mostrar_planificacion_cambio')
    return render(request, template_name, {'object':planificacion})


def newResponsableCambio(request, template_name='Procesos/Cambios/nuevoResponsableCambio.html'):
        form = ResponsableCambioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_responsable_cambio')
        return render(request, template_name, {'form':form})

def verResponsableCambio(request, template_name='Procesos/Cambios/mostrarResponsableCambio.html'):
        responsables = Responsables_Cambio.objects.all().order_by('id')
        data = {'responsable' : responsables}
        data['object_list'] = responsables
        return render(request, template_name, data)

def editarResponsableCambio(request, id, template_name='Procesos/Cambios/editarResponsableCambio.html'):
        responsables = get_object_or_404(Responsables_Cambio, pk=id)
        form = ResponsableCambioForm(request.POST or None, instance=responsables)
        if form.is_valid():
                
                form.save()
                return redirect('mostrar_responsable_cambio')

        return render(request, template_name, {'form':form})

def eliminarResponsableCambio(request, id, template_name='Procesos/Cambios/eliminarResponsableCambio.html'):
    responsable= get_object_or_404(Responsables_Cambio, pk=id)    
    if request.method=='POST':
        responsable.delete()
        return redirect('mostrar_responsable_cambio')
    return render(request, template_name, {'object':responsable})

def newSeguimientoCambio(request, template_name='Procesos/Cambios/nuevoSeguimientoCambio.html'):
        form = SeguimientoCambioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_seguimiento_cambio')
        return render(request, template_name, {'form':form})

def verSeguimientoCambio(request, template_name='Procesos/Cambios/mostrarSeguimientoCambio.html'):
        seguimientos = Seguimiento_Cambio.objects.all().order_by('id')
        data = {'seguimiento' : seguimientos}
        data['object_list'] = seguimientos
        return render(request, template_name, data)

def editarSeguimientoCambio(request, id, template_name='Procesos/Cambios/editarSeguimientoCambio.html'):
        seguimientos = get_object_or_404(Seguimiento_Cambio, pk=id)
        form = SeguimientoCambioForm(request.POST or None, instance=seguimientos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_seguimiento_cambio')

        return render(request, template_name, {'form':form})

def eliminarSeguimientoCambio(request, id, template_name='Procesos/Cambios/eliminarSeguimientoCambio.html'):
    seguimiento= get_object_or_404(Seguimiento_Cambio, pk=id)    
    if request.method=='POST':
        seguimiento.delete()
        return redirect('mostrar_seguimiento_cambio')
    return render(request, template_name, {'object':seguimiento})

def newVerificacionCambio(request, template_name='Procesos/Cambios/nuevaVerificacionCambio.html'):
        form = VerificacionCambioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_verificacion_cambio')
        return render(request, template_name, {'form':form})

def verVerificacionCambio(request, template_name='Procesos/Cambios/mostrarVerificacionCambio.html'):
        verificaciones = Verificacion_Cambio.objects.all().order_by('id')
        data = {'verificacion' : verificaciones}
        data['object_list'] = verificaciones
        return render(request, template_name, data)

def editarVerificacionCambio(request, id, template_name='Procesos/Cambios/editarVerificacionCambio.html'):
        verificaciones = get_object_or_404(Verificacion_Cambio, pk=id)
        form = VerificacionCambioForm(request.POST or None, instance=verificaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_verificacion_cambio')

        return render(request, template_name, {'form':form})

def eliminarVerificacionCambio(request, id, template_name='Procesos/Cambios/eliminarVerificacionCambio.html'):
    verificacion= get_object_or_404(Verificacion_Cambio, pk=id)    
    if request.method=='POST':
        verificacion.delete()
        return redirect('mostrar_verificacion_cambio')
    return render(request, template_name, {'object':verificacion})


def newServicio(request, template_name='Procesos/Peticiones/nuevoServicio.html'):
        form = ServicioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_servicio')
        return render(request, template_name, {'form':form})

def verServicio(request, template_name='Procesos/Peticiones/mostrarServicio.html'):
        servicios = Servicio.objects.all().order_by('id')
        data = {'servicio' : servicios}
        data['object_list'] = servicios
        return render(request, template_name, data)

def editarServicio(request, id, template_name='Procesos/Peticiones/editarServicio.html'):
        servicios = get_object_or_404(Servicio, pk=id)
        form = ServicioForm(request.POST or None, instance=servicios)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_servicio')

        return render(request, template_name, {'form':form})

def eliminarServicio(request, id, template_name='Procesos/Peticiones/eliminarServicio.html'):
    servicio= get_object_or_404(Servicio, pk=id)    
    if request.method=='POST':
        servicio.delete()
        return redirect('mostrar_servicio')
    return render(request, template_name, {'object':servicio})

def newSubcategoria(request, template_name='Procesos/Peticiones/nuevaSubcategoria.html'):
        form = SubcategoriaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_subcategoria')
        return render(request, template_name, {'form':form})

def verSubcategoria(request, template_name='Procesos/Peticiones/mostrarSubcategoria.html'):
        subcategorias = Subcategoria.objects.all().order_by('id')
        data = {'subcategoria' : subcategorias}
        data['object_list'] = subcategorias
        return render(request, template_name, data)

def editarSubcategoria(request, id, template_name='Procesos/Peticiones/editarSubcategoria.html'):
        subcategorias = get_object_or_404(Subcategoria, pk=id)
        form = SubcategoriaForm(request.POST or None, instance=subcategorias)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_subcategoria')

        return render(request, template_name, {'form':form})

def eliminarSubcategoria(request, id, template_name='Procesos/Peticiones/eliminarSubcategoria.html'):
    subcategoria= get_object_or_404(Subcategoria, pk=id)    
    if request.method=='POST':
        subcategoria.delete()
        return redirect('mostrar_subcategoria')
    return render(request, template_name, {'object':subcategoria})

def newProducto(request, template_name='Procesos/Peticiones/nuevoProducto.html'):
        form = ProductoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_producto')
        return render(request, template_name, {'form':form})


def verProducto(request, template_name='Procesos/Peticiones/mostrarProducto.html'):
        productos = Producto.objects.all().order_by('id')
        data = {'producto' : productos}
        data['object_list'] = productos
        return render(request, template_name, data)

def editarProducto(request, id, template_name='Procesos/Peticiones/editarProducto.html'):
        productos = get_object_or_404(Producto, pk=id)
        form = ProductoForm(request.POST or None, instance=productos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_producto')

        return render(request, template_name, {'form':form})

def eliminarProducto(request, id, template_name='Procesos/Peticiones/eliminarProducto.html'):
    producto= get_object_or_404(Producto, pk=id)    
    if request.method=='POST':
        producto.delete()
        return redirect('mostrar_producto')
    return render(request, template_name, {'object':producto})




def verPeticion(request, template_name='Procesos/Peticiones/mostrarPeticion.html'):
        
       cursor2 = connection.cursor()
       cursor2.execute('SELECT a.id, (SELECT o.nombre_organizacion from home_organizacion o where o.id = a.organizacion_id) as Organizacion, (SELECT t.nombre_peticion from home_tipo_peticion t where t.id = a.peticion_id) as Tipo, a.asunto as Asunto, (SELECT COUNT(*) FROM home_productos_peticion p WHERE p.peticion_id = a.id) as Productos, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_asignacion_peticion ap where cl.id = ap.contacto_id and ap.peticion_id = a.id) as Nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_asignacion_peticion ap where cl.id = ap.contacto_id and ap.peticion_id = a.id) as Apellido, (SELECT ap.fecha_asignacion from home_asignacion_peticion ap where ap.peticion_id = a.id) as Fecha_Asignacion, (SELECT l.fecha_solucion from home_acuerdo_sla l where l.peticion_id = a.id) as Fecha_Solucion, (SELECT COUNT(*) FROM home_seguimiento_peticion sp WHERE sp.peticion_id = a.id) as Seguimientos, (SELECT c.fecha_cierre from home_cierre_peticion c where c.peticion_id = a.id) as Cierre, (SELECT COUNT(*) FROM home_entrega_peticion v WHERE v.peticion_id = a.id) as Entrega FROM home_peticion a, home_asignacion_peticion ap group by a.id')         


       persons2 = cursor2.fetchall()

       x2 = cursor2.description
       resultsList2 = []
       for r2 in persons2:
               i = 0
               d = {}
               while i < len(x2):
                       d[x2[i][0]] = r2[i]
                       i = i+1
               resultsList2.append(d)

       context_dict={}
       context_dict['lista2']=resultsList2

       return render(request, template_name, context_dict )





def editarPeticion(request, id, template_name='Procesos/Peticiones/editarPeticion.html'):
        peticiones = get_object_or_404(Peticion, pk=id)
        form = PeticionForm(request.POST or None, instance=peticiones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_peticion')

        return render(request, template_name, {'form':form})

def eliminarPeticion(request, id, template_name='Procesos/Peticiones/eliminarPeticion.html'):
    peticion= get_object_or_404(Peticion, pk=id)

    
    if 'cancel' in request.POST:
            return redirect('mostrar_peticion')

    if 'save' in request.POST:
            peticion.delete()
            return redirect('mostrar_peticion')


    return render(request, template_name, {'object':peticion})



def newPeticion(request, template_name='Procesos/Peticiones/nuevaPeticion.html'):
        form = PeticionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_peticion')
        return render(request, template_name, {'form':form})

def newContacto(request, template_name='Procesos/Configuracion/nuevoContacto.html'):
        form = ContactoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_contacto')
        return render(request, template_name, {'form':form})

def newAsignacionProducto(request, template_name='Procesos/Peticiones/nuevaAsignacionProducto.html'):
        form = ProductosPeticionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_producto')
        return render(request, template_name, {'form':form})





def verAsignacionProducto(request, template_name='Procesos/Peticiones/mostrarAsignacionProducto.html'):
        asignaciones = Productos_Peticion.objects.all().order_by('id')
        data = {'asignacion' : asignaciones}
        data['object_list'] = asignaciones
        return render(request, template_name, data)

def editarAsignacionProducto(request, id, template_name='Procesos/Peticiones/editarAsignacionProducto.html'):
        asignaciones = get_object_or_404(Productos_Peticion, pk=id)
        form = ProductosPeticionForm(request.POST or None, instance=asignaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_producto')

        return render(request, template_name, {'form':form})

def eliminarAsignacionProducto(request, id, template_name='Procesos/Peticiones/eliminarAsignacionProducto.html'):
    asignacion= get_object_or_404(Productos_Peticion, pk=id)    
    if request.method=='POST':
        asignacion.delete()
        return redirect('mostrar_asignacion_producto')
    return render(request, template_name, {'object':asignacion})

def newAsignacionPeticion(request, template_name='Procesos/Peticiones/nuevaAsignacionPeticion.html'):
        form = AsignacionPeticionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_peticion')
        return render(request, template_name, {'form':form})


def verAsignacionPeticion(request, template_name='Procesos/Peticiones/mostrarAsignacionPeticion.html'):
        asignaciones = Asignacion_Peticion.objects.all().order_by('id')
        data = {'asignacion' : asignaciones}
        data['object_list'] = asignaciones
        return render(request, template_name, data)

def editarAsignacionPeticion(request, id, template_name='Procesos/Peticiones/editarAsignacionPeticion.html'):
        asignaciones = get_object_or_404(Asignacion_Peticion, pk=id)
        form = AsignacionPeticionForm(request.POST or None, instance=asignaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_peticion')

        return render(request, template_name, {'form':form})

def eliminarAsignacionPeticion(request, id, template_name='Procesos/Peticiones/eliminarAsignacionPeticion.html'):
    asignacion= get_object_or_404(Asignacion_Peticion, pk=id)    
    if request.method=='POST':
        asignacion.delete()
        return redirect('mostrar_asignacion_peticion')
    return render(request, template_name, {'object':asignacion})

def newAcuerdoSLA(request, template_name='Procesos/Niveles/nuevoAcuerdo.html'):
        form = AcuerdoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_acuerdo')
        return render(request, template_name, {'form':form})


def verAcuerdoSLA(request, template_name='Procesos/Niveles/mostrarAcuerdo.html'):
        acuerdos = Acuerdo_SLA.objects.all().order_by('id')
        data = {'acuerdo' : acuerdos}
        data['object_list'] = acuerdos
        return render(request, template_name, data)

def editarAcuerdoSLA(request, id, template_name='Procesos/Niveles/editarAcuerdo.html'):
        acuerdos = get_object_or_404(Acuerdo_SLA, pk=id)
        form = AcuerdoForm(request.POST or None, instance=acuerdos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_acuerdo')

        return render(request, template_name, {'form':form})

def eliminarAcuerdoSLA(request, id, template_name='Procesos/Niveles/eliminarAcuerdo.html'):
    acuerdo= get_object_or_404(Acuerdo_SLA, pk=id)    
    if request.method=='POST':
        acuerdo.delete()
        return redirect('mostrar_acuerdo')
    return render(request, template_name, {'object':acuerdo})

def newSeguimientoPeticion(request, template_name='Procesos/Peticiones/nuevoSeguimientoPeticion.html'):
        form = SeguimientoPeticionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_seguimiento_peticion')
        return render(request, template_name, {'form':form})


def verSeguimientoPeticion(request, template_name='Procesos/Peticiones/mostrarSeguimientoPeticion.html'):
        seguimientos = Seguimiento_Peticion.objects.all().order_by('id')
        data = {'seguimiento' : seguimientos}
        data['object_list'] = seguimientos
        return render(request, template_name, data)

def editarSeguimientoPeticion(request, id, template_name='Procesos/Peticiones/editarSeguimientoPeticion.html'):
        seguimientos = get_object_or_404(Seguimiento_Peticion, pk=id)
        form = SeguimientoPeticionForm(request.POST or None, instance=seguimientos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_seguimiento_peticion')

        return render(request, template_name, {'form':form})

def eliminarSeguimientoPeticion(request, id, template_name='Procesos/Peticiones/eliminarSeguimientoPeticion.html'):
    seguimiento= get_object_or_404(Seguimiento_Peticion, pk=id)    
    if request.method=='POST':
        seguimiento.delete()
        return redirect('mostrar_seguimiento_peticion')
    return render(request, template_name, {'object':seguimiento})

def newCierrePeticion(request, template_name='Procesos/Peticiones/nuevoCierrePeticion.html'):
        form = CierrePeticionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_cierre_peticion')
        return render(request, template_name, {'form':form})


def verCierrePeticion(request, template_name='Procesos/Peticiones/mostrarCierrePeticion.html'):
        cierres = Cierre_Peticion.objects.all().order_by('id')
        data = {'cierre' : cierres}
        data['object_list'] = cierres
        return render(request, template_name, data)

def editarCierrePeticion(request, id, template_name='Procesos/Peticiones/editarCierrePeticion.html'):
        cierres = get_object_or_404(Cierre_Peticion, pk=id)
        form = CierrePeticionForm(request.POST or None, instance=cierres)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_cierre_peticion')

        return render(request, template_name, {'form':form})

def eliminarCierrePeticion(request, id, template_name='Procesos/Peticiones/eliminarCierrePeticion.html'):
    cierre = get_object_or_404(Cierre_Peticion, pk=id)    
    if request.method=='POST':
        cierre.delete()
        return redirect('mostrar_cierre_peticion')
    return render(request, template_name, {'object':cierre})

def newEntrega(request, template_name='Procesos/Entrega/nuevaEntrega.html'):
        form = EntregaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_entrega')
        return render(request, template_name, {'form':form})


def verEntrega(request, template_name='Procesos/Entrega/mostrarEntrega.html'):
        entregas = Entrega_Peticion.objects.all().order_by('id')
        data = {'entrega' : entregas}
        data['object_list'] = entregas
        return render(request, template_name, data)

def editarEntrega(request, id, template_name='Procesos/Entrega/editarEntrega.html'):
        entregas = get_object_or_404(Entrega_Peticion, pk=id)
        form = EntregaForm(request.POST or None, instance=entregas)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_entrega')

        return render(request, template_name, {'form':form})

def eliminarEntrega(request, id, template_name='Procesos/Entrega/eliminarEntrega.html'):
    entrega = get_object_or_404(Entrega_Peticion, pk=id)    
    if request.method=='POST':
        entrega.delete()
        return redirect('mostrar_entrega')
    return render(request, template_name, {'object':entrega})

def newProblema(request, template_name='Procesos/Problemas/nuevoProblema.html'):
        form = ProblemaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_problema')
        return render(request, template_name, {'form':form})


def verProblema(request, template_name='Procesos/Problemas/mostrarProblema.html'):
       cursor2 = connection.cursor()
       cursor2.execute('select p.id, p.peticion_id, (SELECT t.nombre_peticion from home_tipo_peticion t where t.id = n.peticion_id) as Tipo, p.asunto_problema, (SELECT o.nombre_organizacion from home_organizacion o, home_lista_proveedores lp where o.id = lp.organizacion_id  and lp.id=p.proveedor_id) as Proveedor, p.urgencia, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_asignacion_problema ap where cl.id = ap.contacto_id and ap.problema_id = p.id) as Nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_asignacion_problema ap where cl.id = ap.contacto_id and ap.problema_id = p.id) as Apellido, (SELECT ap.fecha_inicio from home_asignacion_problema ap where ap.problema_id = p.id) as Fecha_Asignacion, (SELECT ap.fecha_resolucion from home_asignacion_problema ap where ap.problema_id = p.id) as Fecha_Resolucion, (SELECT COUNT(*) FROM home_seguimiento_problema sp WHERE sp.problema_id = p.id) as Seguimientos, (SELECT cp.fecha_cierre from home_cierre_problema cp, home_asignacion_problema ap where ap.problema_id = p.id and cp.problema_id=p.id) as Fecha_Cierre, (SELECT cp.error_conocido_id from home_cierre_problema cp, home_asignacion_problema ap where ap.problema_id = p.id and cp.problema_id=p.id) as Error FROM home_problema p, home_peticion n where p.peticion_id=n.id group by p.id')
                       
       persons2 = cursor2.fetchall()

       x2 = cursor2.description
       resultsList2 = []
       for r2 in persons2:
               i = 0
               d = {}
               while i < len(x2):
                       d[x2[i][0]] = r2[i]
                       i = i+1
               resultsList2.append(d)

       context_dict={}
       context_dict['problema']=resultsList2

       return render(request, template_name, context_dict )




def editarProblema(request, id, template_name='Procesos/Problemas/editarProblema.html'):
        problemas = get_object_or_404(Problema, pk=id)
        form = ProblemaForm(request.POST or None, instance=problemas)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_problema')

        return render(request, template_name, {'form':form})

def eliminarProblema(request, id, template_name='Procesos/Problemas/eliminarProblema.html'):
    problema= get_object_or_404(Problema, pk=id)

    if 'cancel' in request.POST:
            return redirect('mostrar_problema')

    if 'save' in request.POST:
            problema.delete()
            return redirect('mostrar_problema')


    return render(request, template_name, {'object':problema})



def newAsignacionProblema(request, template_name='Procesos/Problemas/nuevaAsignacionProblema.html'):
        form = AsignacionProblemaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_problema')
        return render(request, template_name, {'form':form})


def verAsignacionProblema(request, template_name='Procesos/Problemas/mostrarAsignacionProblema.html'):
        asignaciones = Asignacion_Problema.objects.all().order_by('id')
        data = {'asignacion' : asignaciones}
        data['object_list'] = asignaciones
        return render(request, template_name, data)

def editarAsignacionProblema(request, id, template_name='Procesos/Problemas/editarAsignacionProblema.html'):
        asignaciones = get_object_or_404(Asignacion_Problema, pk=id)
        form = AsignacionProblemaForm(request.POST or None, instance=asignaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_problema')

        return render(request, template_name, {'form':form})

def eliminarAsignacionProblema(request, id, template_name='Procesos/Problemas/eliminarAsignacionProblema.html'):
    asignacion = get_object_or_404(Asignacion_Problema, pk=id)    
    if request.method=='POST':
        asignacion.delete()
        return redirect('mostrar_asignacion_problema')
    return render(request, template_name, {'object':asignacion})

def newSeguimientoProblema(request, template_name='Procesos/Problemas/nuevoSeguimientoProblema.html'):
        form = SeguimientoProblemaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_seguimiento_problema')
        return render(request, template_name, {'form':form})


def verSeguimientoProblema(request, template_name='Procesos/Problemas/mostrarSeguimientoProblema.html'):
        seguimientos = Seguimiento_Problema.objects.all().order_by('id')
        data = {'seguimiento' : seguimientos}
        data['object_list'] = seguimientos
        return render(request, template_name, data)

def editarSeguimientoProblema(request, id, template_name='Procesos/Problemas/editarSeguimientoProblema.html'):
        seguimientos = get_object_or_404(Seguimiento_Problema, pk=id)
        form = SeguimientoProblemaForm(request.POST or None, instance=seguimientos)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_seguimiento_problema')

        return render(request, template_name, {'form':form})

def eliminarSeguimientoProblema(request, id, template_name='Procesos/Problemas/eliminarSeguimientoProblema.html'):
    seguimiento = get_object_or_404(Seguimiento_Problema, pk=id)    
    if request.method=='POST':
        seguimiento.delete()
        return redirect('mostrar_seguimiento_problema')
    return render(request, template_name, {'object':seguimiento})

def newCierreProblema(request, template_name='Procesos/Problemas/nuevoCierreProblema.html'):
        form = CierreProblemaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_cierre_problema')
        return render(request, template_name, {'form':form})


def verCierreProblema(request, template_name='Procesos/Problemas/mostrarCierreProblema.html'):
        cierres = Cierre_Problema.objects.all().order_by('id')
        data = {'cierre' : cierres}
        data['object_list'] = cierres
        return render(request, template_name, data)

def editarCierreProblema(request, id, template_name='Procesos/Problemas/editarCierreProblema.html'):
        cierres = get_object_or_404(Cierre_Problema, pk=id)
        form = CierreProblemaForm(request.POST or None, instance=cierres)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_cierre_problema')

        return render(request, template_name, {'form':form})

def eliminarCierreProblema(request, id, template_name='Procesos/Problemas/eliminarCierreProblema.html'):
    cierre = get_object_or_404(Cierre_Problema, pk=id)    
    if request.method=='POST':
        cierre.delete()
        return redirect('mostrar_cierre_problema')
    return render(request, template_name, {'object':cierre})

def newDesempeno(request, template_name='Procesos/Proveedores/nuevoDesempeno.html'):
        form = DesempenoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_desempeno')
        return render(request, template_name, {'form':form})


def verDesempeno(request, template_name='Procesos/Proveedores/mostrarDesempeno.html'):

        #preguntas = Preguntas.objects.all().order_by('id')
        preguntas = Preguntas.objects.filter(tipo_pregunta = '5').order_by('id')
        data = {'pregunta' : preguntas}
        data['object_list'] = preguntas
        return render(request, template_name, data)


def editarDesempeno(request, id, template_name='Procesos/Proveedores/editarDesempeno.html'):        

        preguntas = get_object_or_404(Preguntas, pk=id)
        form = PreguntaForm(request.POST or None, instance=preguntas)
        if form.is_valid():
                form.save()
                return redirect('mostrar_desempeno')

        return render(request, template_name, {'form':form})



def eliminarDesempeno(request, id, template_name='Procesos/Proveedores/eliminarDesempeno.html'):
    desempeno = get_object_or_404(Desempeno, pk=id)    
    if request.method=='POST':
        desempeno.delete()
        return redirect('mostrar_desempeno')
    return render(request, template_name, {'object':desempeno})

def newPonderacion(request, template_name='Procesos/Proveedores/nuevaPonderacion.html'):
        form = PonderacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_ponderacion')
        return render(request, template_name, {'form':form})


def verPonderacion(request, template_name='Procesos/Proveedores/mostrarPonderacion.html'):
        ponderaciones = Ponderacion.objects.all().order_by('id')
        data = {'ponderacion' : ponderaciones}
        data['object_list'] = ponderaciones
        return render(request, template_name, data)

def editarPonderacion(request, id, template_name='Procesos/Proveedores/editarPonderacion.html'):
        ponderaciones = get_object_or_404(Ponderacion, pk=id)
        form = PonderacionForm(request.POST or None, instance=ponderaciones)
        
        if form.is_valid():
                form.save()
                return redirect('mostrar_ponderacion')

        return render(request, template_name, {'form':form})

def eliminarPonderacion(request, id, template_name='Procesos/Proveedores/eliminarPonderacion.html'):
    ponderacion = get_object_or_404(Ponderacion, pk=id)    
    if request.method=='POST':
        ponderacion.delete()
        return redirect('mostrar_ponderacion')
    return render(request, template_name, {'object':ponderacion})

def newEvaluacion(request, template_name='Procesos/Proveedores/nuevaEvaluacion.html'):
        form = EvaluacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_inicio_evaluacion')
        return render(request, template_name, {'form':form})


def verEvaluacion(request, template_name='Procesos/Proveedores/mostrarEvaluacion.html'):
        evaluaciones = Evaluacion.objects.all().order_by('id')
        data = {'evaluacion' : evaluaciones}
        data['object_list'] = evaluaciones
        return render(request, template_name, data)

def editarEvaluacion(request, id, template_name='Procesos/Proveedores/editarEvaluacion.html'):
        evaluaciones = get_object_or_404(Evaluacion, pk=id)
        form = EvaluacionForm(request.POST or None, instance=evaluaciones)
        if form.is_valid():
                form.save()
                return redirect('mostrar_inicio_evaluacion')

        return render(request, template_name, {'form':form})

def eliminarEvaluacion(request, id, template_name='Procesos/Proveedores/eliminarEvaluacion.html'):
    evaluacion = get_object_or_404(Evaluacion, pk=id)    
    if request.method=='POST':
        evaluacion.delete()
        return redirect('mostrar_inicio_evaluacion')
    return render(request, template_name, {'object':evaluacion})


def newEvaluacionProveedor(request, template_name='Procesos/Proveedores/nuevaEvaluacionProveedor.html'):
        form = EvaluacionProveedorForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_evaluacion_proveedor')
        return render(request, template_name, {'form':form})




def verEvaluacionProveedor(request, template_name='Procesos/Proveedores/mostrarEvaluacionProveedor.html'):
        evaluaciones = Evaluacion_Proveedores.objects.all().order_by('id')
        data = {'evaluacion' : evaluaciones}
        data['object_list'] = evaluaciones
        return render(request, template_name, data)

def editarEvaluacionProveedor(request, id, template_name='Procesos/Proveedores/editarEvaluacionProveedor.html'):
        evaluaciones = get_object_or_404(Evaluacion_Proveedores, pk=id)
        form = EvaluacionProveedorForm(request.POST or None, instance=evaluaciones)
        if form.is_valid():
                form.save()
                return redirect('mostrar_evaluacion_proveedor')

        return render(request, template_name, {'form':form})

def eliminarEvaluacionProveedor(request, id, template_name='Procesos/Proveedores/eliminarEvaluacionProveedor.html'):

    encuesta = get_object_or_404(Evaluacion_Proveedores, pk=id)    
    if 'cancel2' in request.POST:
            return redirect('mostrar_evaluacion_proveedor')

    if 'save2' in request.POST:
            encuesta.delete()
            return redirect('mostrar_evaluacion_proveedor')
        
    return render(request, template_name, {'object':encuesta})



#def newEvaluacionProveedor(request, template_name='Procesos/Proveedores/nuevaEvaluacionProveedor.html'):
 #       form = EvaluacionProveedorForm(request.POST or None)
  #      if form.is_valid():
   #             form.save()
    #            return redirect('mostrar_evaluacion_proveedor')
     #   return render(request, template_name, {'form':form})

#def verEvaluacionProveedor(request, template_name='Procesos/Proveedores/mostrarEvaluacionProveedor.html'):
 #       evaluaciones = Evaluacion_Proveedores.objects.all().order_by('id')
  #      data = {'evaluacion' : evaluaciones}
   #     data['object_list'] = evaluaciones
    #    return render(request, template_name, data)

#def editarEvaluacionProveedor(request, id, template_name='Procesos/Proveedores/editarEvaluacionProveedor.html'):
 #       evaluaciones = get_object_or_404(Evaluacion_Proveedores, pk=id)
  #      form = EvaluacionProveedorForm(request.POST or None, instance=evaluaciones)
   #     if form.is_valid():
    #            form.save()
     #           return redirect('mostrar_evaluacion_proveedor')

      #  return render(request, template_name, {'form':form})

#def eliminarEvaluacionProveedor(request, id, template_name='Procesos/Proveedores/eliminarEvaluacionProveedor.html'):
 #   evaluacion = get_object_or_404(Evaluacion_Proveedores, pk=id)    
  #  if request.method=='POST':
   #     evaluacion.delete()
    #    return redirect('mostrar_evaluacion_proveedor')
    #return render(request, template_name, {'object':evaluacion})

def newReevaluacionProveedor(request, template_name='Procesos/Proveedores/nuevaReevaluacionProveedor.html'):
        form = ReevaluacionProveedorForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_reevaluacion_proveedor')
        return render(request, template_name, {'form':form})

def verReevaluacionProveedor(request, template_name='Procesos/Proveedores/mostrarReevaluacionProveedor.html'):
        #encuestas = Encuestado.objects.all().order_by('id')
        encuestas = Encuestado.objects.filter(proceso = '2').order_by('id')
        data = {'encuesta' : encuestas}
        data['object_list'] = encuestas
        return render(request, template_name, data)



def editarReevaluacionProveedor(request, id, template_name='Procesos/Proveedores/editarReevaluacionProveedor.html'):
        evaluaciones = get_object_or_404(Reevaluacion_Proveedores, pk=id)
        form = ReevaluacionProveedorForm(request.POST or None, instance=evaluaciones)
        if form.is_valid():
                form.save()
                return redirect('mostrar_reevaluacion_proveedor')

        return render(request, template_name, {'form':form})

def eliminarReevaluacionProveedor(request, id, template_name='Procesos/Proveedores/eliminarReevaluacionProveedor.html'):
    evaluacion = get_object_or_404(Reevaluacion_Proveedores, pk=id)    
    if request.method=='POST':
        evaluacion.delete()
        return redirect('mostrar_reevaluacion_proveedor')
    return render(request, template_name, {'object':evaluacion})

def newPregunta(request, template_name='Procesos/Clientes/nuevaPregunta.html'):
        form = PreguntaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_pregunta')
        return render(request, template_name, {'form':form})

def verPregunta(request, template_name='Procesos/Clientes/mostrarPregunta.html'):
        #preguntas = Preguntas.objects.all().order_by('id')
        preguntas = Preguntas.objects.filter(tipo_pregunta = '2').order_by('id')
        data = {'pregunta' : preguntas}
        data['object_list'] = preguntas
        return render(request, template_name, data)



def editarPregunta(request, id, template_name='Procesos/Clientes/editarPregunta.html'):
        preguntas = get_object_or_404(Preguntas, pk=id)
        form = PreguntaForm(request.POST or None, instance=preguntas)
        if form.is_valid():
                form.save()
                return redirect('mostrar_pregunta')

        return render(request, template_name, {'form':form})

def eliminarPregunta(request, id, template_name='Procesos/Clientes/eliminarPregunta.html'):
    pregunta = get_object_or_404(Preguntas, pk=id)    
    if request.method=='POST':
        pregunta.delete()
        return redirect('mostrar_pregunta')
    return render(request, template_name, {'object':pregunta})

def newCliente(request, template_name='Procesos/Clientes/nuevoCliente.html'):
        form = ClienteForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_cliente')
        return render(request, template_name, {'form':form})

def verCliente(request, template_name='Procesos/Clientes/mostrarCliente.html'):
        #clientes = Encuestado.objects.all().order_by('id')
        clientes = Encuestado.objects.filter(tipo_contacto = '1').order_by('id')
        data = {'cliente' : clientes}
        data['object_list'] = clientes
        return render(request, template_name, data)

def editarCliente(request, id, template_name='Procesos/Clientes/editarCliente.html'):
        clientes = get_object_or_404(Encuestado, pk=id)
        form = ClienteForm(request.POST or None, instance=clientes)
        if form.is_valid():
                form.save()
                return redirect('mostrar_encuesta')

        return render(request, template_name, {'form':form})

def eliminarCliente(request, id, template_name='Procesos/Clientes/eliminarCliente.html'):
    cliente = get_object_or_404(Encuestado, pk=id)    
    if request.method=='POST':
        pregunta.delete()
        return redirect('mostrar_cliente')
    return render(request, template_name, {'object':cliente})

def newEncuesta(request, template_name='Procesos/Clientes/nuevaEncuesta.html'):
        form = EncuestaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_encuesta')
        return render(request, template_name, {'form':form})

def verEncuesta(request, template_name='Procesos/Clientes/mostrarEncuesta.html'):
        #encuestas = Encuestado.objects.all().order_by('id')
        encuestas = Encuestado.objects.filter(proceso = '2').order_by('id')
        data = {'encuesta' : encuestas}
        data['object_list'] = encuestas
        return render(request, template_name, data)

def editarEncuesta(request, id, template_name='Procesos/Clientes/editarEncuesta.html'):
        encuestas = get_object_or_404(Encuesta, pk=id)
        form = EncuestaForm(request.POST or None, instance=encuestas)
        if form.is_valid():
                form.save()
                return redirect('mostrar_encuesta')

        return render(request, template_name, {'form':form})

def eliminarEncuesta(request, id, template_name='Procesos/Clientes/eliminarEncuesta.html'):
        
    encuesta = get_object_or_404(Encuestado, pk=id)    
    if 'cancel' in request.POST:
            return redirect('mostrar_encuesta')

    if 'save' in request.POST:
            encuesta.delete()
            return redirect('mostrar_encuesta')
        
    return render(request, template_name, {'object':encuesta})



def newReclamacion(request, template_name='Procesos/Clientes/nuevaReclamacion.html'):
        form = ReclamacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_reclamacion')
        return render(request, template_name, {'form':form})

def verReclamacion(request, template_name='Procesos/Clientes/mostrarReclamacion.html'):
        cursor = connection.cursor()
        cursor.execute('select s.id, s.motivo_reclamacion, (SELECT cl.nombre_servicio from home_servicio cl where cl.id = s.servicio_id) servicio, (SELECT cl.nombre_subcategoria from home_subcategoria cl where cl.id = s.subcategoria_id) subcategoria, s.valor_importancia, (SELECT cl.contacto from home_tipo_contacto cl where cl.id = s.tipo_contacto_id) cliente, (SELECT cl.nombre_organizacion from home_organizacion cl where cl.id = s.organizacion_id) organizacion, s.fecha_registro, (SELECT cl.nombre_contacto from home_cliente_empleado cl where cl.id = s.contacto_id) as nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl where cl.id = s.contacto_id) as apellido, (SELECT e.fecha_asignacion from home_asignacion_reclamacion e where e.reclamacion_id = s.id) as asignacion, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_asignacion_reclamacion p where cl.id = p.contacto_id and p.reclamacion_id=s.id) as NombreC,  (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_asignacion_reclamacion p where cl.id = p.contacto_id and p.reclamacion_id=s.id) as ApellidoC, (SELECT cl.nombre_grupo from home_grupo_ec cl, home_asignacion_reclamacion p where cl.id = p.grupo_id and p.reclamacion_id=s.id) as grupo from home_reclamacion s')
                       
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        context_dict={}
        context_dict['lista']=resultsList


        return render(request, template_name, context_dict,  )





def editarReclamacion(request, id, template_name='Procesos/Clientes/editarReclamacion.html'):
        reclamaciones = get_object_or_404(Reclamacion, pk=id)
        form = ReclamacionForm(request.POST or None, instance=reclamaciones)
        if form.is_valid():
                form.save()
                return redirect('mostrar_reclamacion')

        return render(request, template_name, {'form':form})

def eliminarReclamacion(request, id, template_name='Procesos/Clientes/eliminarReclamacion.html'):
    encuesta = get_object_or_404(Reclamacion, pk=id)    
    if 'cancel' in request.POST:
            return redirect('mostrar_reclamacion')

    if 'save' in request.POST:
            encuesta.delete()
            return redirect('mostrar_reclamacion')
        
    return render(request, template_name, {'object':encuesta})


def newAsignacionReclamacion(request, template_name='Procesos/Clientes/nuevaAsignacionReclamacion.html'):
        form = AsignacionReclamacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_reclamacion')
        return render(request, template_name, {'form':form})

def verAsignacionReclamacion(request, template_name='Procesos/Clientes/mostrarAsignacionReclamacion.html'):
        reclamaciones = Asignacion_Reclamacion.objects.all().order_by('id')
        data = {'asignacion' : reclamaciones}
        data['object_list'] = reclamaciones
        return render(request, template_name, data)

def editarAsignacionReclamacion(request, id, template_name='Procesos/Clientes/editarAsignacionReclamacion.html'):
        reclamaciones = get_object_or_404(Asignacion_Reclamacion, pk=id)
        form = AsignacionReclamacionForm(request.POST or None, instance=reclamaciones)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_reclamacion')

        return render(request, template_name, {'form':form})

def eliminarAsignacionReclamacion(request, id, template_name='Procesos/Clientes/eliminarAsignacionReclamacion.html'):
    reclamacion = get_object_or_404(Asignacion_Reclamacion, pk=id)    
    if request.method=='POST':
        reclamacion.delete()
        return redirect('mostrar_asignacion_reclamacion')
    return render(request, template_name, {'object':reclamacion})

def newAsignacionEncuesta(request, template_name='Procesos/Clientes/nuevaAsignacionEncuesta.html'):
        form = AsignacionEncuestaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_encuesta')
        return render(request, template_name, {'form':form})

def verAsignacionEncuesta(request, template_name='Procesos/Clientes/mostrarAsignacionEncuesta.html'):
        encuestas = Asignacion_Encuesta.objects.all().order_by('id')
        data = {'asignacion' : encuestas}
        data['object_list'] = encuestas
        return render(request, template_name, data)

def editarAsignacionEncuesta(request, id, template_name='Procesos/Clientes/editarAsignacionEncuesta.html'):
        encuestas = get_object_or_404(Asignacion_Encuesta, pk=id)
        form = AsignacionEncuestaForm(request.POST or None, instance=encuestas)
        if form.is_valid():
                form.save()
                return redirect('mostrar_asignacion_encuesta')

        return render(request, template_name, {'form':form})

def eliminarAsignacionEncuesta(request, id, template_name='Procesos/Clientes/eliminarAsignacionEncuesta.html'):
    encuesta = get_object_or_404(Asignacion_Encuesta, pk=id)    
    if request.method=='POST':
        encuesta.delete()
        return redirect('mostrar_asignacion_encuesta')
    return render(request, template_name, {'object':encuesta})

def newActivo(request, template_name='Procesos/Seguridad/nuevoActivo.html'):
        form = ActivoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_activo')
        return render(request, template_name, {'form':form})

def verActivo(request, template_name='Procesos/Seguridad/mostrarActivo.html'):
        activos = Activos.objects.all().order_by('id')
        data = {'activo' : activos}
        data['object_list'] = activos
        return render(request, template_name, data)

def editarActivo(request, id, template_name='Procesos/Seguridad/editarActivo.html'):
        activos = get_object_or_404(Activos, pk=id)
        form = ActivoForm(request.POST or None, instance=activos)
        if form.is_valid():
                form.save()
                return redirect('mostrar_activo')

        return render(request, template_name, {'form':form})

def eliminarActivo(request, id, template_name='Procesos/Seguridad/eliminarActivo.html'):
    activo = get_object_or_404(Activos, pk=id)    
    if request.method=='POST':
        activo.delete()
        return redirect('mostrar_activo')
    return render(request, template_name, {'object':activo})

def newAmenaza(request, template_name='Procesos/Seguridad/nuevaAmenaza.html'):
        form = AmenazaForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_amenaza')
        return render(request, template_name, {'form':form})

def verAmenaza(request, template_name='Procesos/Seguridad/mostrarAmenaza.html'):
        amenazas = Amenazas.objects.all().order_by('id')
        data = {'amenaza' : amenazas}
        data['object_list'] = amenazas
        return render(request, template_name, data)

def editarAmenaza(request, id, template_name='Procesos/Seguridad/editarAmenaza.html'):
        amenazas = get_object_or_404(Amenazas, pk=id)
        form = AmenazaForm(request.POST or None, instance=amenazas)
        if form.is_valid():
                form.save()
                return redirect('mostrar_amenaza')

        return render(request, template_name, {'form':form})

def eliminarAmenaza(request, id, template_name='Procesos/Seguridad/eliminarAmenaza.html'):
    amenaza = get_object_or_404(Amenazas, pk=id)    
    if request.method=='POST':
        amenaza.delete()
        return redirect('mostrar_amenaza')
    return render(request, template_name, {'object':amenaza})

def newRiesgo(request, template_name='Procesos/Seguridad/nuevoRiesgo.html'):
        form = RiesgoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_riesgo')
        return render(request, template_name, {'form':form})

def verRiesgo(request, template_name='Procesos/Seguridad/mostrarRiesgo.html'):
        riesgos = Riesgos.objects.all().order_by('id')
        data = {'riesgo' : riesgos}
        data['object_list'] = riesgos
        return render(request, template_name, data)

def editarRiesgo(request, id, template_name='Procesos/Seguridad/editarRiesgo.html'):
        riesgos = get_object_or_404(Riesgos, pk=id)
        form = RiesgoForm(request.POST or None, instance=riesgos)
        if form.is_valid():
                form.save()
                return redirect('mostrar_riesgo')

        return render(request, template_name, {'form':form})

def eliminarRiesgo(request, id, template_name='Procesos/Seguridad/eliminarRiesgo.html'):
    riesgo = get_object_or_404(Riesgos, pk=id)    
    if request.method=='POST':
        riesgo.delete()
        return redirect('mostrar_riesgo')
    return render(request, template_name, {'object':riesgo})

def newAnalisisRiesgo(request, template_name='Procesos/Seguridad/nuevoAnalisisRiesgo.html'):
        form = AnalisisRiesgoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_analisis_riesgo')
        return render(request, template_name, {'form':form})

def verAnalisisRiesgo(request, template_name='Procesos/Seguridad/mostrarAnalisisRiesgo.html'):
        riesgos = Analisis_Riesgos.objects.all().order_by('id')
        data = {'analisis' : riesgos}
        data['object_list'] = riesgos
        return render(request, template_name, data)

def editarAnalisisRiesgo(request, id, template_name='Procesos/Seguridad/editarAnalisisRiesgo.html'):
        riesgos = get_object_or_404(Analisis_Riesgos, pk=id)
        form = AnalisisRiesgoForm(request.POST or None, instance=riesgos)
        if form.is_valid():
                form.save()
                return redirect('mostrar_analisis_riesgo')

        return render(request, template_name, {'form':form})

def eliminarAnalisisRiesgo(request, id, template_name='Procesos/Seguridad/eliminarAnalisisRiesgo.html'):
    riesgo = get_object_or_404(Analisis_Riesgos, pk=id)    
    if request.method=='POST':
        riesgo.delete()
        return redirect('mostrar_analisis_riesgo')
    return render(request, template_name, {'object':riesgo})

def newPrioridadRiesgo(request, template_name='Procesos/Seguridad/nuevaPrioridadRiesgo.html'):
        form = PrioridadRiesgoForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_prioridad_riesgo')
        return render(request, template_name, {'form':form})

def verPrioridadRiesgo(request, template_name='Procesos/Seguridad/mostrarPrioridadRiesgo.html'):
        prioridad = Prioridad_Riesgo.objects.all().order_by('id')
        data = {'prioridad' : prioridad}
        data['object_list'] = prioridad
        return render(request, template_name, data)

def editarPrioridadRiesgo(request, id, template_name='Procesos/Seguridad/editarPrioridadRiesgo.html'):
        prioridades = get_object_or_404(Prioridad_Riesgo, pk=id)
        form = PrioridadRiesgoForm(request.POST or None, instance=prioridades)
        if form.is_valid():
                form.save()
                return redirect('mostrar_prioridad_riesgo')

        return render(request, template_name, {'form':form})

def eliminarPrioridadRiesgo(request, id, template_name='Procesos/Seguridad/eliminarPrioridadRiesgo.html'):
    prioridad = get_object_or_404(Prioridad_Riesgo, pk=id)    
    if request.method=='POST':
        prioridad.delete()
        return redirect('mostrar_prioridad_riesgo')
    return render(request, template_name, {'object':prioridad})

def newCalificacion(request, template_name='Procesos/Seguridad/nuevaCalificacion.html'):
        form = CalificacionForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_calificacion')
        return render(request, template_name, {'form':form})

def verCalificacion(request, template_name='Procesos/Seguridad/mostrarCalificacion.html'):
        calificacion = Calificacion.objects.all().order_by('id')
        data = {'calificacion' : calificacion}
        data['object_list'] = calificacion
        return render(request, template_name, data)

def editarCalificacion(request, id, template_name='Procesos/Seguridad/editarCalificacion.html'):
        calificaciones = get_object_or_404(Calificacion, pk=id)
        form = CalificacionForm(request.POST or None, instance=calificaciones)
        if form.is_valid():
                form.save()
                return redirect('mostrar_calificacion')

        return render(request, template_name, {'form':form})

def eliminarCalificacion(request, id, template_name='Procesos/Seguridad/eliminarCalificacion.html'):
    calificacion = get_object_or_404(Calificacion, pk=id)    
    if request.method=='POST':
        calificacion.delete()
        return redirect('mostrar_calificacion')
    return render(request, template_name, {'object':calificacion})

def newCuestionario(request, template_name='Procesos/Seguridad/nuevoCuestionario.html'):
        form = CuestionarioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_cuestionario')
        return render(request, template_name, {'form':form})

def verCuestionario(request, template_name='Procesos/Seguridad/mostrarCuestionario.html'):
        cuestionario = Cuestionario_Seguridad.objects.all().order_by('id')
        data = {'cuestionario' : cuestionario}
        data['object_list'] = cuestionario
        return render(request, template_name, data)

def editarCuestionario(request, id, template_name='Procesos/Seguridad/editarCuestionario.html'):
        cuestionarios = get_object_or_404(Cuestionario_Seguridad, pk=id)
        form = CuestionarioForm(request.POST or None, instance=cuestionarios)
        if form.is_valid():
                form.save()
                return redirect('mostrar_cuestionario')

        return render(request, template_name, {'form':form})

def eliminarCuestionario(request, id, template_name='Procesos/Seguridad/eliminarCuestionario.html'):
    cuestionario = get_object_or_404(Cuestionario_Seguridad, pk=id)    
    if request.method=='POST':
        cuestionario.delete()
        return redirect('mostrar_cuestionario')
    return render(request, template_name, {'object':cuestionario})

def newResultadoCuestionario(request, template_name='Procesos/Seguridad/nuevoResultadoCuestionario.html'):
        form = ResultadoCuestionarioForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_resultado_cuestionario')
        return render(request, template_name, {'form':form})

def verResultadoCuestionario(request, template_name='Procesos/Seguridad/mostrarResultadoCuestionario.html'):
        cuestionario = Resultado_Cuestionario.objects.all().order_by('id')
        data = {'resultado' : cuestionario}
        data['object_list'] = cuestionario
        return render(request, template_name, data)

def editarResultadoCuestionario(request, id, template_name='Procesos/Seguridad/editarResultadoCuestionario.html'):
        cuestionarios = get_object_or_404(Resultado_Cuestionario, pk=id)
        form = ResultadoCuestionarioForm(request.POST or None, instance=cuestionarios)
        if form.is_valid():
                form.save()
                return redirect('mostrar_resultado_cuestionario')

        return render(request, template_name, {'form':form})

def eliminarResultadoCuestionario(request, id, template_name='Procesos/Seguridad/eliminarResultadoCuestionario.html'):
    cuestionario = get_object_or_404(Resultado_Cuestionario, pk=id)    
    if request.method=='POST':
        cuestionario.delete()
        return redirect('mostrar_resultado_cuestionario')
    return render(request, template_name, {'object':cuestionario})

def newAuditoriaSeguridad(request, template_name='Procesos/Seguridad/nuevaAuditoriaSeguridad.html'):
        form = AuditoriaSeguridadForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_auditoria_seguridad')
        return render(request, template_name, {'form':form})

def verAuditoriaSeguridad(request, template_name='Procesos/Seguridad/mostrarAuditoriaSeguridad.html'):
        auditoria = Auditoria_Seguridad.objects.all().order_by('id')
        data = {'auditoria' : auditoria}
        data['object_list'] = auditoria
        return render(request, template_name, data)

def editarAuditoriaSeguridad(request, id, template_name='Procesos/Seguridad/editarAuditoriaSeguridad.html'):
        auditorias = get_object_or_404(Auditoria_Seguridad, pk=id)
        form = AuditoriaSeguridadForm(request.POST or None, instance=auditorias)
        if form.is_valid():
                form.save()
                return redirect('mostrar_auditoria_seguridad')

        return render(request, template_name, {'form':form})

def eliminarAuditoriaSeguridad(request, id, template_name='Procesos/Seguridad/eliminarAuditoriaSeguridad.html'):
    auditoria = get_object_or_404(Auditoria_Seguridad, pk=id)    
    if request.method=='POST':
        auditoria.delete()
        return redirect('mostrar_auditoria_seguridad')
    return render(request, template_name, {'object':auditoria})

def newChecklistSeguridad(request, template_name='Procesos/Seguridad/nuevoChecklistSeguridad.html'):
        form = ChecklistSeguridadForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_checklist_seguridad')
        return render(request, template_name, {'form':form})

def verChecklistSeguridad(request, template_name='Procesos/Seguridad/mostrarChecklistSeguridad.html'):
        checklist = Checklist_Auditoria_Seguridad.objects.all().order_by('id')
        data = {'checklist' : checklist}
        data['object_list'] = checklist
        return render(request, template_name, data)

def editarChecklistSeguridad(request, id, template_name='Procesos/Seguridad/editarChecklistSeguridad.html'):
        checklist = get_object_or_404(Checklist_Auditoria_Seguridad, pk=id)
        form = ChecklistSeguridadForm(request.POST or None, instance=checklist)
        if form.is_valid():
                form.save()
                return redirect('mostrar_checklist_seguridad')

        return render(request, template_name, {'form':form})

def eliminarChecklistSeguridad(request, id, template_name='Procesos/Seguridad/eliminarChecklistSeguridad.html'):
    checklist = get_object_or_404(Checklist_Auditoria_Seguridad, pk=id)    
    if request.method=='POST':
        checklist.delete()
        return redirect('mostrar_checklist_seguridad')
    return render(request, template_name, {'object':checklist})


def newResultadoSeguridad(request, template_name='Procesos/Seguridad/nuevoResultadoSeguridad.html'):
        form = ResultadoSeguridadForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('mostrar_resultado_seguridad')
        return render(request, template_name, {'form':form})

def verResultadoSeguridad(request, template_name='Procesos/Seguridad/mostrarResultadoSeguridad.html'):
        resultado = Resultados_Auditoria_Seguridad.objects.all().order_by('id')
        data = {'resultado' : resultado}
        data['object_list'] = resultado
        return render(request, template_name, data)

def editarResultadoSeguridad(request, id, template_name='Procesos/Seguridad/editarResultadoSeguridad.html'):
        resultado = get_object_or_404(Resultados_Auditoria_Seguridad, pk=id)
        form = ResultadoSeguridadForm(request.POST or None, instance=resultado)
        if form.is_valid():
                form.save()
                return redirect('mostrar_resultado_seguridad')

        return render(request, template_name, {'form':form})

def eliminarResultadoSeguridad(request, id, template_name='Procesos/Seguridad/eliminarResultadoSeguridad.html'):
    resultado = get_object_or_404(Resultados_Auditoria_Seguridad, pk=id)    
    if request.method=='POST':
        resultado.delete()
        return redirect('mostrar_resultado_seguridad')
    return render(request, template_name, {'object':resultado})


def verResumenConfiguracion(request, template_name='Procesos/Configuracion/mostrarResumenConfiguracion.html'):

        ec_obj = General_Configuracion.objects.all().values('criticidad').annotate(num=Count('criticidad')).order_by('num')

        #ec_obj2 = General_Configuracion.objects.all().values('nombre_ec').annotate(num=Count('nombre_ec')).order_by('num')
        cursor = connection.cursor()
        cursor.execute('SELECT e.nombre_ec, g.nombre_ec_id, count(*) as num FROM home_general_configuracion g, home_EC e where g.nombre_ec_id = e.id group by g.nombre_ec_id')

        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)






        cursor3 = connection.cursor()
        cursor3.execute('SELECT cl.nombre_ec as ec from home_ec cl, home_general_configuracion pc where cl.id = pc.nombre_ec_id and pc.nombre_ec_id!=14 group by pc.nombre_ec_id;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('select count(nombre_ec_id) as total from home_general_configuracion where nombre_ec_id!=14 group by nombre_ec_id;')

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('SELECT activo from home_general_configuracion group by activo;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor6 = connection.cursor()
        cursor6.execute('select count(activo) as total from home_general_configuracion group by activo;')
        
                        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)




        cursor7 = connection.cursor()
        cursor7.execute('SELECT criticidad from home_general_configuracion group by criticidad;')
        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('select count(criticidad) as total from home_general_configuracion group by criticidad;')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)



        cursor9 = connection.cursor()
        cursor9.execute('SELECT cl.nombre_ec as ec, count(pc.nombre_ec_id) as total, (select count(pc.activo) from home_general_configuracion pc where pc.activo=1 and cl.id = pc.nombre_ec_id) as activo, (select count(pc.activo) from home_general_configuracion pc where pc.activo=0 and cl.id = pc.nombre_ec_id) as inactivo, (select count(pc.criticidad) from home_general_configuracion pc where pc.criticidad="alto" and cl.id = pc.nombre_ec_id) as alto, (select count(pc.criticidad) from home_general_configuracion pc where pc.criticidad="medio" and cl.id = pc.nombre_ec_id) as medio, (select count(pc.criticidad) from home_general_configuracion pc where pc.criticidad="bajo" and cl.id = pc.nombre_ec_id) as bajo from home_ec cl, home_general_configuracion pc  where cl.id = pc.nombre_ec_id group by pc.nombre_ec_id;')
        
        persons9 = cursor9.fetchall() 

        x9 = cursor9.description
        resultsList9 = []   
        for r9 in persons9:
            i = 0
            d = {}
            while i < len(x9):
                d[x9[i][0]] = r9[i]
                i = i+1
            resultsList9.append(d)




        cursor10 = connection.cursor()
        cursor10.execute('select if(c.tipo_contacto_id=2, "Excel", "Cliente") as contacto from home_cliente_empleado c group by c.tipo_contacto_id;')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)



        cursor11 = connection.cursor()
        cursor11.execute('select count(c.tipo_contacto_id) as total from home_cliente_empleado c group by c.tipo_contacto_id;')

                        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)
            





          
        context_dict={}
        context_dict['lista']=ec_obj
        context_dict['lista2']=resultsList


        context_dict['labels']=resultsList3
        context_dict['values']=resultsList4

        labels2 = resultsList5
        values2 = resultsList6
        set=zip(values2, labels2)
        context_dict['set']=set

        labels3 = resultsList7
        values3 = resultsList8
        set2=zip(values3, labels3)
        context_dict['set2']=set2

        context_dict['lista3']=resultsList9

        labels4=resultsList10
        values4=resultsList11
        set3=zip(values4, labels4)
        context_dict['set3']=set3
        

        

        

        return render(request, template_name, context_dict )





def verResumenCambios(request, template_name='Procesos/Cambios/mostrarResumenCambios.html'):

        cursor = connection.cursor()
        cursor.execute('SELECT g.nombre_grupo, s.grupo_id, count(*) as num FROM home_solicitud_cambio s, home_grupo_ec g  where s.grupo_id = g.id group by s.grupo_id;')
        
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)
          

        cursor2 = connection.cursor()
        cursor2.execute('SELECT a.id, (SELECT COUNT(*) FROM home_planificacion_cambio p WHERE p.folio_id = a.id) as Planificacion, (SELECT COUNT(*)  FROM home_responsables_cambio r WHERE r.folio_id = a.id) as Responsables,(SELECT COUNT(*) FROM home_verificacion_cambio v  WHERE v.folio_id = a.id) as Verificacion FROM home_solicitud_cambio a;')
        
        persons2 = cursor2.fetchall() 

        x2 = cursor2.description
        resultsList2 = []   
        for r2 in persons2:
            i = 0
            d = {}
            while i < len(x2):
                d[x2[i][0]] = r2[i]
                i = i+1
            resultsList2.append(d)






        cursor3 = connection.cursor()
        cursor3.execute('SELECT cl.nombre_contacto as Nombre, apellido_contacto as Apellido  from home_cliente_empleado cl, home_solicitud_cambio sc where cl.id = sc.contacto_id group by sc.contacto_id;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('select count(contacto_id) as Total from home_solicitud_cambio group by contacto_id;')

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)





        cursor5 = connection.cursor()
        cursor5.execute('SELECT estimacion_recursos as Recursos from home_solicitud_cambio group by estimacion_recursos;')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor6 = connection.cursor()
        cursor6.execute('select count(estimacion_recursos) as Total from home_solicitud_cambio group by estimacion_recursos;')
                        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)




        cursor7 = connection.cursor()
        cursor7.execute('SELECT Estado from home_exclusivo_cambio group by Estado;')
        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('select count(Estado) as Total from home_exclusivo_cambio group by Estado;')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)


        cursor9 = connection.cursor()
        cursor9.execute('select s.id, s.fecha, s.asunto, s.estimacion_recursos, (SELECT cl.nombre_contacto from home_cliente_empleado cl where cl.id = s.contacto_id) as Nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl where cl.id = s.contacto_id) as Apellido, (SELECT e.estado from home_exclusivo_cambio e where e.folio_id = s.id) as Estado, (SELECT p.reunion_id from home_planificacion_cambio p where p.folio_id=s.id) as Reunion, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_planificacion_cambio p where cl.id = p.coordinador_id and p.folio_id=s.id) as NombreC, (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_planificacion_cambio p where cl.id = p.coordinador_id and p.folio_id=s.id) as ApellidoC, (SELECT COUNT(*) FROM home_responsables_cambio r WHERE r.folio_id = s.id) as Responsables, (SELECT COUNT(*) FROM home_seguimiento_cambio r WHERE r.folio_id = s.id) as Seguimientos, (SELECT v.fecha_verificacion from home_verificacion_cambio v where v.folio_id = s.id) as Fecha_Verificacion, (SELECT v.eficacia from home_verificacion_cambio v where v.folio_id = s.id) as Eficacia from home_solicitud_cambio s')
                        
        persons9 = cursor9.fetchall() 

        x9 = cursor9.description
        resultsList9 = []   
        for r9 in persons9:
            i = 0
            d = {}
            while i < len(x9):
                d[x9[i][0]] = r9[i]
                i = i+1
            resultsList9.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('SELECT cl.nombre_contacto as Nombre, apellido_contacto as Apellido from home_cliente_empleado cl, home_planificacion_cambio pc where cl.id = pc.coordinador_id group by pc.coordinador_id;')

                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)



        cursor11 = connection.cursor()
        cursor11.execute('select count(coordinador_id) as Total from home_planificacion_cambio group by coordinador_id;')
                        
        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)
            



        cursor12 = connection.cursor()
        cursor12.execute('SELECT monthname(fecha_verificacion) as mes, year(fecha_verificacion) as ano FROM home_verificacion_cambio GROUP BY year(fecha_verificacion), month(fecha_verificacion);')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)



        cursor13 = connection.cursor()
        cursor13.execute('SELECT COUNT(id) as total FROM home_verificacion_cambio GROUP BY year(fecha_verificacion), month(fecha_verificacion);')
        
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)



        cursor14 = connection.cursor()
        cursor14.execute('SELECT eficacia from home_verificacion_cambio group by eficacia;')
        
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)



        cursor15 = connection.cursor()
        cursor15.execute('select count(eficacia) as total from home_verificacion_cambio group by eficacia;')
                         
        persons15 = cursor15.fetchall() 

        x15 = cursor15.description
        resultsList15 = []   
        for r15 in persons15:
            i = 0
            d = {}
            while i < len(x15):
                d[x15[i][0]] = r15[i]
                i = i+1
            resultsList15.append(d)

          
        context_dict={}
        context_dict['lista']=resultsList
        context_dict['lista2']=resultsList2

        context_dict['labels']=resultsList3
        context_dict['values']=resultsList4

        labels2 = resultsList5
        values2 = resultsList6
        set=zip(values2, labels2)
        context_dict['set']=set

        labels3 = resultsList7
        values3 = resultsList8
        set2=zip(values3, labels3)
        context_dict['set2']=set2

        context_dict['lista3']=resultsList9

        context_dict['labels4']=resultsList10
        context_dict['values4']=resultsList11

        context_dict['labels5']=resultsList12
        context_dict['values5']=resultsList13


        labels6 = resultsList14
        values6 = resultsList15
        set3=zip(values6, labels6)
        context_dict['set3']=set3
        

        return render(request, template_name, context_dict )


def verResumenProblemas(request, template_name='Procesos/Problemas/mostrarResumenProblemas.html'):

        cursor = connection.cursor()
        cursor.execute('select p.id, p.peticion_id, (SELECT t.nombre_peticion from home_tipo_peticion t where t.id = n.peticion_id) as Tipo, p.asunto_problema, (SELECT o.nombre_organizacion from home_organizacion o, home_lista_proveedores lp where o.id = lp.organizacion_id and lp.id=p.proveedor_id) as Proveedor, p.urgencia, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_asignacion_problema ap where cl.id = ap.contacto_id and ap.problema_id = p.id) as Nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_asignacion_problema ap where cl.id = ap.contacto_id and ap.problema_id = p.id) as Apellido, (SELECT ap.fecha_inicio from home_asignacion_problema ap where ap.problema_id = p.id) as Fecha_Asignacion, (SELECT ap.fecha_resolucion from home_asignacion_problema ap where ap.problema_id = p.id) as Fecha_Resolucion, (SELECT COUNT(*) FROM home_seguimiento_problema sp WHERE sp.problema_id = p.id) as Seguimientos, (SELECT cp.fecha_cierre from home_cierre_problema cp, home_asignacion_problema ap where ap.problema_id = p.id and cp.problema_id=p.id) as Fecha_Cierre, (SELECT cp.error_conocido_id from home_cierre_problema cp, home_asignacion_problema ap where ap.problema_id = p.id and cp.problema_id=p.id) as Error FROM home_problema p, home_peticion n where p.peticion_id=n.id group by p.id')

        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)
          
        context_dict={}
        context_dict['lista']=resultsList

        cursor2 = connection.cursor()
        cursor2.execute('SELECT a.id, (SELECT COUNT(*) FROM home_seguimiento_problema s WHERE s.problema_id = a.id) as Seguimiento, (SELECT COUNT(*) FROM home_cierre_problema c WHERE c.problema_id = a.id) as Cierre FROM home_problema a;')
        persons2 = cursor2.fetchall() 

        x2 = cursor2.description
        resultsList2 = []   
        for r2 in persons2:
            i = 0
            d = {}
            while i < len(x2):
                d[x2[i][0]] = r2[i]
                i = i+1
            resultsList2.append(d)



        cursor3 = connection.cursor()
        cursor3.execute('SELECT o.nombre_organizacion as Proveedor from home_organizacion o, home_lista_proveedores lp, home_problema p where o.id = lp.organizacion_id and lp.id=p.proveedor_id group by lp.id;')

        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('SELECT COUNT(o.nombre_organizacion) as Total from home_organizacion o, home_lista_proveedores lp, home_problema p where o.id = lp.organizacion_id and lp.id=p.proveedor_id group by lp.id;')

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)


        cursor5 = connection.cursor()
        cursor5.execute('SELECT distinct p.urgencia from home_problema p group by p.urgencia;')

                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor6 = connection.cursor()
        cursor6.execute('SELECT COUNT(p.urgencia) as total from home_problema p group by p.urgencia;')

                        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)


        cursor7 = connection.cursor()
        cursor7.execute('SELECT monthname(fecha_cierre) as mes, year(fecha_cierre) as ano FROM home_cierre_problema GROUP BY year(fecha_cierre), month(fecha_cierre);')
                        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('SELECT COUNT(id) as total FROM home_cierre_problema GROUP BY year(fecha_cierre), month(fecha_cierre);')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)


        cursor9 = connection.cursor()
        cursor9.execute('SELECT cl.nombre_contacto as Nombre, apellido_contacto as Apellido from home_cliente_empleado cl, home_asignacion_problema ap, home_problema a  where cl.id = ap.contacto_id and ap.problema_id = a.id group by ap.contacto_id;')
                        
        persons9 = cursor9.fetchall() 

        x9 = cursor9.description
        resultsList9 = []   
        for r9 in persons9:
            i = 0
            d = {}
            while i < len(x9):
                d[x9[i][0]] = r9[i]
                i = i+1
            resultsList9.append(d)



        cursor10 = connection.cursor()
        cursor10.execute('select count(contacto_id) as Total from home_asignacion_problema group by contacto_id;')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)

          
        context_dict={}
        context_dict['lista']=resultsList
        context_dict['lista2']=resultsList2
        context_dict['labels']=resultsList3
        context_dict['values']=resultsList4

        labels2 = resultsList5
        values2 = resultsList6
        set=zip(values2, labels2)
        context_dict['set']=set

        context_dict['labels2']=resultsList7
        context_dict['values2']=resultsList8
        context_dict['labels3']=resultsList9
        context_dict['values3']=resultsList10
        

        return render(request, template_name, context_dict )


def verResumenPeticiones(request, template_name='Procesos/Peticiones/mostrarResumenPeticiones.html'):

        cursor = connection.cursor()
        cursor.execute('SELECT t.id, t.nombre_peticion, p.peticion_id, count(*) as num FROM home_tipo_peticion t,  home_peticion p where t.id = p.peticion_id group by p.peticion_id;')
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)


        cursor2 = connection.cursor()
        cursor2.execute('SELECT a.id, (SELECT o.nombre_organizacion from home_organizacion o where o.id = a.organizacion_id) as Organizacion, (SELECT t.nombre_peticion from home_tipo_peticion t where t.id = a.peticion_id) as Tipo, a.asunto as Asunto, (SELECT COUNT(*) FROM home_productos_peticion p WHERE p.peticion_id = a.id) as Productos, (SELECT cl.nombre_contacto from home_cliente_empleado cl, home_asignacion_peticion ap where cl.id = ap.contacto_id and ap.peticion_id = a.id) as Nombre, (SELECT cl.apellido_contacto from home_cliente_empleado cl, home_asignacion_peticion ap where cl.id = ap.contacto_id and ap.peticion_id = a.id) as Apellido, (SELECT ap.fecha_asignacion from home_asignacion_peticion ap where ap.peticion_id = a.id) as Fecha_Asignacion, (SELECT l.fecha_solucion from home_acuerdo_sla l where l.peticion_id = a.id) as Fecha_Solucion, (SELECT COUNT(*) FROM home_seguimiento_peticion sp WHERE sp.peticion_id = a.id) as Seguimientos, (SELECT c.fecha_cierre from home_cierre_peticion c where c.peticion_id = a.id) as Cierre, (SELECT COUNT(*) FROM home_entrega_peticion v WHERE v.peticion_id = a.id) as Entrega FROM home_peticion a, home_asignacion_peticion ap group by a.id')         


        persons2 = cursor2.fetchall() 

        x2 = cursor2.description
        resultsList2 = []   
        for r2 in persons2:
            i = 0
            d = {}
            while i < len(x2):
                d[x2[i][0]] = r2[i]
                i = i+1
            resultsList2.append(d)



        cursor3 = connection.cursor()
        cursor3.execute('SELECT cl.nombre_contacto as Nombre, apellido_contacto as Apellido from home_cliente_empleado cl, home_asignacion_peticion ap, home_peticion a where cl.id = ap.contacto_id and ap.peticion_id = a.id group by ap.contacto_id')

        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('select count(contacto_id) as Total from home_asignacion_peticion group by contacto_id')
        

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)



        cursor5 = connection.cursor()
        cursor5.execute('SELECT t.nombre_peticion as tipo FROM home_tipo_peticion t,  home_peticion p where t.id = p.peticion_id group by p.peticion_id')

        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)



        cursor6 = connection.cursor()
        cursor6.execute('SELECT count(*) as num FROM home_tipo_peticion t,  home_peticion p where t.id = p.peticion_id group by p.peticion_id')
                        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)



        cursor7 = connection.cursor()
        cursor7.execute('SELECT monthname(fecha_cierre) as mes, year(fecha_cierre) as ano FROM home_cierre_peticion GROUP BY year(fecha_cierre), month(fecha_cierre);')
                        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('SELECT COUNT(id) as total FROM home_cierre_peticion GROUP BY year(fecha_cierre), month(fecha_cierre);')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)
            

        context_dict={}
        context_dict['lista']=resultsList
        context_dict['lista2']=resultsList2
        context_dict['labels']=resultsList3
        context_dict['values']=resultsList4

        labels2 = resultsList5
        values2 = resultsList6
        set=zip(values2, labels2)
        context_dict['set']=set

        context_dict['labels3']=resultsList7
        context_dict['values3']=resultsList8

        return render(request, template_name, context_dict,  )







def verResumenProveedores(request, template_name='Procesos/Proveedores/mostrarResumenProveedores.html'):

        cursor = connection.cursor()
        cursor.execute('SELECT p.id, p.estado, t.estado_id, count(*) as num FROM home_ponderacion p,  home_evaluacion_proveedores t where p.id = t.estado_id group by t.estado_id;')
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)
          
        context_dict={}
        context_dict['lista']=resultsList

        cursor2 = connection.cursor()
        cursor2.execute('SELECT a.id, (SELECT COUNT(*) FROM home_productos_peticion p WHERE p.peticion_id = a.id) as Productos, ap.fecha_asignacion, l.fecha_solucion, (SELECT COUNT(*) FROM home_seguimiento_peticion sp WHERE sp.peticion_id = a.id) as Seguimientos, (SELECT COUNT(*) FROM home_cierre_peticion cp WHERE cp.peticion_id = a.id) as Cierre, (SELECT COUNT(*) FROM home_entrega_peticion v WHERE v.peticion_id = a.id) as Entrega FROM home_peticion a, home_asignacion_peticion ap, home_acuerdo_sla l, home_cierre_peticion cp WHERE ap.peticion_id=a.id and l.peticion_id=a.id')
        persons2 = cursor2.fetchall() 

        x2 = cursor2.description
        resultsList2 = []   
        for r2 in persons2:
            i = 0
            d = {}
            while i < len(x2):
                d[x2[i][0]] = r2[i]
                i = i+1
            resultsList2.append(d)











        cursor3 = connection.cursor()
        cursor3.execute('SELECT cl.nombre_organizacion as proveedor from home_organizacion cl, home_lista_proveedores l, home_evaluacion_proveedores pc where cl.id = l.organizacion_id and l.id=pc.proveedor_id and pc.proceso_id=5 group by pc.proveedor_id;')

        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('SELECT count(cl.nombre_organizacion) as total from home_organizacion cl, home_lista_proveedores l, home_evaluacion_proveedores pc where cl.id = l.organizacion_id and l.id=pc.proveedor_id and pc.proceso_id=5 group by pc.proveedor_id;')

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)


        cursor5 = connection.cursor()
        cursor5.execute('SELECT monthname(fecha_registro) as mes, year(fecha_registro) as ano FROM home_evaluacion_proveedores group by year(fecha_registro), month(fecha_registro); ')

                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor6 = connection.cursor()
        cursor6.execute('SELECT COUNT(id) as total FROM home_evaluacion_proveedores group BY year(fecha_registro), month(fecha_registro);')

                        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)


        cursor7 = connection.cursor()
        cursor7.execute('SELECT cl.estado as incidente from home_ponderacion cl, home_evaluacion_proveedores pc where cl.id = pc.estado_id and pc.proceso_id=5 group by pc.estado_id')
                        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('SELECT count(cl.estado) as total from home_ponderacion cl, home_evaluacion_proveedores pc where cl.id = pc.estado_id and pc.proceso_id=5 group by pc.estado_id')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)


        cursor9 = connection.cursor()
        cursor9.execute('SELECT estado2 as desempeno from home_evaluacion_proveedores where proceso_id=5 group by estado2;')
                        
        persons9 = cursor9.fetchall() 

        x9 = cursor9.description
        resultsList9 = []   
        for r9 in persons9:
            i = 0
            d = {}
            while i < len(x9):
                d[x9[i][0]] = r9[i]
                i = i+1
            resultsList9.append(d)



        cursor10 = connection.cursor()
        cursor10.execute('SELECT count(estado2) as total from home_evaluacion_proveedores where proceso_id=5 group by estado2;')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)

          
        context_dict={}
                                
          
        context_dict={}
        context_dict['lista']=resultsList
        context_dict['lista2']=resultsList2


        context_dict['labels']=resultsList3
        context_dict['values']=resultsList4


        context_dict['labels2']=resultsList5
        context_dict['values2']=resultsList6


        labels4 = resultsList7
        values4 = resultsList8
        set=zip(values4, labels4)
        context_dict['set']=set


        labels5 = resultsList9
        values5 = resultsList10
        set2=zip(values5, labels5)
        context_dict['set2']=set2
                                

        return render(request, template_name, context_dict )


def verResumenClientes(request, template_name='Procesos/Clientes/mostrarResumenClientes.html'):

        cursor = connection.cursor()
        cursor.execute('SELECT distinct e.encuestado_id, o.nombre_organizacion, c.fecha_encuesta, c.id  from home_encuesta e, home_encuestado c, home_organizacion o  where c.id = e.encuestado_id and o.id=c.organizacion_id')
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)
          
        context_dict={}
        context_dict['lista']=resultsList

        cursor2 = connection.cursor()
        cursor2.execute('SELECT a.id, (SELECT COUNT(*) FROM home_productos_peticion p WHERE p.peticion_id = a.id) as Productos, ap.fecha_asignacion, l.fecha_solucion, (SELECT COUNT(*) FROM home_seguimiento_peticion sp WHERE sp.peticion_id = a.id) as Seguimientos, (SELECT COUNT(*) FROM home_cierre_peticion cp WHERE cp.peticion_id = a.id) as Cierre, (SELECT COUNT(*) FROM home_entrega_peticion v WHERE v.peticion_id = a.id) as Entrega FROM home_peticion a, home_asignacion_peticion ap, home_acuerdo_sla l, home_cierre_peticion cp WHERE ap.peticion_id=a.id and l.peticion_id=a.id')
        persons2 = cursor2.fetchall() 

        x2 = cursor2.description
        resultsList2 = []   
        for r2 in persons2:
            i = 0
            d = {}
            while i < len(x2):
                d[x2[i][0]] = r2[i]
                i = i+1
            resultsList2.append(d)
          




        cursor3 = connection.cursor()
        cursor3.execute('SELECT cl.nombre_organizacion as organizacion from db_home.home_organizacion cl, db_home.home_encuestado pc where cl.id = pc.organizacion_id and pc.proceso_id=2 group by pc.organizacion_id;')
                        
        persons3 = cursor3.fetchall() 

        x3 = cursor3.description
        resultsList3 = []   
        for r3 in persons3:
            i = 0
            d = {}
            while i < len(x3):
                d[x3[i][0]] = r3[i]
                i = i+1
            resultsList3.append(d)


        cursor4 = connection.cursor()
        cursor4.execute('select count(organizacion_id) as Total from db_home.home_encuestado where proceso_id=2 group by organizacion_id;')

        persons4 = cursor4.fetchall() 

        x4 = cursor4.description
        resultsList4 = []   
        for r4 in persons4:
            i = 0
            d = {}
            while i < len(x4):
                d[x4[i][0]] = r4[i]
                i = i+1
            resultsList4.append(d)




        cursor5 = connection.cursor()
        cursor5.execute('SELECT year(fecha_encuesta) as ano FROM db_home.home_encuestado where proceso_id=2 group by year(fecha_encuesta);')
                        
        persons5 = cursor5.fetchall() 

        x5 = cursor5.description
        resultsList5 = []   
        for r5 in persons5:
            i = 0
            d = {}
            while i < len(x5):
                d[x5[i][0]] = r5[i]
                i = i+1
            resultsList5.append(d)


        cursor6 = connection.cursor()
        cursor6.execute('SELECT COUNT(id) as total FROM db_home.home_encuestado where proceso_id=2  group BY year(fecha_encuesta);')
        
        persons6 = cursor6.fetchall() 

        x6 = cursor6.description
        resultsList6 = []   
        for r6 in persons6:
            i = 0
            d = {}
            while i < len(x6):
                d[x6[i][0]] = r6[i]
                i = i+1
            resultsList6.append(d)



        cursor7 = connection.cursor()
        cursor7.execute('SELECT estado from db_home.home_encuestado where proceso_id=2 group by estado;')
                        
        persons7 = cursor7.fetchall() 

        x7 = cursor7.description
        resultsList7 = []   
        for r7 in persons7:
            i = 0
            d = {}
            while i < len(x7):
                d[x7[i][0]] = r7[i]
                i = i+1
            resultsList7.append(d)


        cursor8 = connection.cursor()
        cursor8.execute('select count(estado) as total from db_home.home_encuestado where proceso_id=2 group by estado;')
                        
        persons8 = cursor8.fetchall() 

        x8 = cursor8.description
        resultsList8 = []   
        for r8 in persons8:
            i = 0
            d = {}
            while i < len(x8):
                d[x8[i][0]] = r8[i]
                i = i+1
            resultsList8.append(d)



        cursor9 = connection.cursor()
        cursor9.execute('SELECT cl.nombre_organizacion as organizacion from db_home.home_organizacion cl, db_home.home_reclamacion pc where cl.id = pc.organizacion_id group by pc.organizacion_id;')
                        
        persons9 = cursor9.fetchall() 

        x9 = cursor9.description
        resultsList9 = []   
        for r9 in persons9:
            i = 0
            d = {}
            while i < len(x9):
                d[x9[i][0]] = r9[i]
                i = i+1
            resultsList9.append(d)


        cursor10 = connection.cursor()
        cursor10.execute('select count(organizacion_id) as total from db_home.home_reclamacion group by organizacion_id;')
                        
        persons10 = cursor10.fetchall() 

        x10 = cursor10.description
        resultsList10 = []   
        for r10 in persons10:
            i = 0
            d = {}
            while i < len(x10):
                d[x10[i][0]] = r10[i]
                i = i+1
            resultsList10.append(d)



        cursor11 = connection.cursor()
        cursor11.execute('SELECT monthname(fecha_registro) as mes, year(fecha_registro) as ano FROM db_home.home_reclamacion group by year(fecha_registro), month(fecha_registro);')

        persons11 = cursor11.fetchall() 

        x11 = cursor11.description
        resultsList11 = []   
        for r11 in persons11:
            i = 0
            d = {}
            while i < len(x11):
                d[x11[i][0]] = r11[i]
                i = i+1
            resultsList11.append(d)
            



        cursor12 = connection.cursor()
        cursor12.execute('SELECT COUNT(id) as total FROM db_home.home_reclamacion group BY year(fecha_registro), month(fecha_registro);')
        
        persons12 = cursor12.fetchall() 

        x12 = cursor12.description
        resultsList12 = []   
        for r12 in persons12:
            i = 0
            d = {}
            while i < len(x12):
                d[x12[i][0]] = r12[i]
                i = i+1
            resultsList12.append(d)


        cursor13 = connection.cursor()
        cursor13.execute('SELECT s.nombre_servicio from db_home.home_servicio s, db_home.home_reclamacion r where r.servicio_id=s.id group by r.id;')
        persons13 = cursor13.fetchall() 

        x13 = cursor13.description
        resultsList13 = []   
        for r13 in persons13:
            i = 0
            d = {}
            while i < len(x13):
                d[x13[i][0]] = r13[i]
                i = i+1
            resultsList13.append(d)



        cursor14 = connection.cursor()
        cursor14.execute('SELECT count(r.id) as total from db_home.home_reclamacion r group by r.id; ')
        
        persons14 = cursor14.fetchall() 

        x14 = cursor14.description
        resultsList14 = []   
        for r14 in persons14:
            i = 0
            d = {}
            while i < len(x14):
                d[x14[i][0]] = r14[i]
                i = i+1
            resultsList14.append(d)




        context_dict={}
        context_dict['lista']=resultsList
        context_dict['lista2']=resultsList2

        context_dict['labels']=resultsList3
        context_dict['values']=resultsList4

        context_dict['labels2']=resultsList5
        context_dict['values2']=resultsList6


        labels3 = resultsList7
        values3 = resultsList8
        set=zip(values3, labels3)
        context_dict['set']=set


        context_dict['labels4']=resultsList9
        context_dict['values4']=resultsList10
        context_dict['labels5']=resultsList11
        context_dict['values5']=resultsList12


        labels6 = resultsList13
        values6 = resultsList14
        set2=zip(values6, labels6)
        context_dict['set2']=set2        
        

        return render(request, template_name, context_dict )


def verResumenSeguridad(request, template_name='Procesos/Seguridad/mostrarResumenSeguridad.html'):

        cursor = connection.cursor()
        cursor.execute('SELECT e.encuestado_id, e.calificacion, o.nombre_organizacion, t.id, p.nombre_contacto, p.apellido_contacto from db_home.home_resultado_cuestionario e, db_home.home_organizacion o,  db_home.home_encuestado t, db_home.home_cliente_empleado p where t.id = e.encuestado_id and o.id=t.organizacion_id and t.contacto_id = p.id')
        persons = cursor.fetchall() 

        x = cursor.description
        resultsList = []   
        for r in persons:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)
          
        context_dict={}
        context_dict['lista']=resultsList

        cursor2 = connection.cursor()
        cursor2.execute('SELECT a.id, (SELECT COUNT(*) FROM db_home.home_productos_peticion p WHERE p.peticion_id = a.id) as Productos, ap.fecha_asignacion, l.fecha_solucion, (SELECT COUNT(*) FROM db_home.home_seguimiento_peticion sp WHERE sp.peticion_id = a.id) as Seguimientos, (SELECT COUNT(*) FROM db_home.home_cierre_peticion cp WHERE cp.peticion_id = a.id) as Cierre, (SELECT COUNT(*) FROM db_home.home_entrega_peticion v WHERE v.peticion_id = a.id) as Entrega FROM db_home.home_peticion a, db_home.home_asignacion_peticion ap, db_home.home_acuerdo_sla l, db_home.home_cierre_peticion cp WHERE ap.peticion_id=a.id and l.peticion_id=a.id')
        persons2 = cursor2.fetchall() 

        x2 = cursor2.description
        resultsList2 = []   
        for r2 in persons2:
            i = 0
            d = {}
            while i < len(x2):
                d[x2[i][0]] = r2[i]
                i = i+1
            resultsList2.append(d)
          
        context_dict={}
        context_dict['lista']=resultsList
        context_dict['lista2']=resultsList2

        return render(request, template_name, context_dict )



def allEC(request, template_name='Procesos/Configuracion/allEC.html'):


        return render(request, template_name )



class CreateMarca(CreateView):
    model = Marca
    template_name = 'Procesos/Peticiones/popups/marca_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('nuevo_producto')

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('nuevo_producto')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, 'message info')
            return HttpResponseRedirect(reverse('nuevo_producto'))
        else:
            return super(CreateMarca, self).post(request, *args, **kwargs)

class CreateModelo(CreateView):
    model = Modelo
    template_name = 'Procesos/Peticiones/popups/modelo_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('nuevo_producto')

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('nuevo_producto')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, 'message info')
            return HttpResponseRedirect(reverse('nuevo_producto'))
        else:
            return super(CreateModelo, self).post(request, *args, **kwargs)

class CreateOrganizacion(CreateView):
    model = Organizacion
    template_name = 'Procesos/Peticiones/popups/organizacion_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('nuevo_peticion')

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('nuevo_peticion')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, 'message info')
            return HttpResponseRedirect(reverse('nuevo_peticion'))
        else:
            return super(CreateOrganizacion, self).post(request, *args, **kwargs)

class CreateProducto(CreateView):
    model = Producto
    template_name = 'Procesos/Peticiones/popups/producto_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('nuevo_asignacion_producto')

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('nuevo_asignacion_producto')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, 'message info')
            return HttpResponseRedirect(reverse('nuevo_asignacion_producto'))
        else:
            return super(CreateProducto, self).post(request, *args, **kwargs)


class CreateContacto(CreateView):
    model = Cliente_Empleado
    template_name = 'Procesos/Peticiones/popups/contacto_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('nuevo_peticion')

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('nuevo_peticion')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, 'message info')
            return HttpResponseRedirect(reverse('nuevo_peticion'))
        else:
            return super(CreateContacto, self).post(request, *args, **kwargs)





class CreateEvaluacion(CreateView):
    model = Encuestado
    template_name = 'Procesos/Peticiones/popups/evaluacion_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        new_contact = form.save()

        return redirect('/encuesta/%s/#section1' % new_contact.pk)


    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('mostrar_encuesta')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
                return redirect('mostrar_encuesta')
        if 'save' in request.POST:
            return super(CreateEvaluacion, self).post(request, *args, **kwargs)



class CreateEvaluacionProveedores(CreateView):
    model = Evaluacion_Proveedores
    template_name = 'Procesos/Peticiones/popups/evaluacion_proveedor_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        new_contact = form.save()

        return redirect('/evaluacion/%s/#section1' % new_contact.pk)

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return redirect('mostrar_evaluacion_proveedor')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
                return redirect('mostrar_evaluacion_proveedor')
        if 'save' in request.POST:
            return super(CreateEvaluacionProveedores, self).post(request, *args, **kwargs)





class CreatePeticion(CreateView):
    model = Peticion
    template_name = 'Procesos/Peticiones/popups/peticion_add.html'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('nuevo_asignacion_producto')

    def get_success_url(self):
        messages.success(self.request, 'message success')
        return reverse('nuevo_asignacion_producto')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(self.request, 'message info')
            return HttpResponseRedirect(reverse('nuevo_asignacion_producto'))
        else:
            return super(CreatePeticion, self).post(request, *args, **kwargs)


def create_peticion(request):
        if request.method == 'POST':
                peticion = request.POST['peticion']
                tipo_contacto = request.POST['tipo_contacto']
                organizacion = request.POST['organizacion']
                contacto = request.POST['contacto']
                origen = request.POST['origen']
                asunto = request.POST['asunto']
                descripcion = request.POST['descripcion']
                impacto = request.POST['impacto']
                urgencia = request.POST['urgencia']

                Peticion.objects.create(
                peticion = peticion,
                tipo_contacto = tipo_contacto,
                organizacion = organizacion,
                contacto = contacto,
                origen = origen,
                asunto = asunto,
                descripcion = descripcion,
                impacto = impacto,
                urgencia = urgencia,
                )

        return HttpResponse('')

def create_contacto(request):
        if request.method == 'POST':
                nombre_contacto = request.POST['nombre_contacto']
                apellido_contacto = request.POST['apellido_contacto']
                activo = request.POST['activo']
                tipo_contacto = request.POST['tipo_contacto']
                organizacion = request.POST['organizacion']
                grupo = request.POST['grupo']
                funcion = request.POST['funcion']
                jefe = request.POST['jefe']
                correo = request.POST['correo']

                Cliente_Empleado.objects.create(
                nombre_contacto = nombre_contacto,
                apellido_contacto = apellido_contacto,
                activo = activo,
                tipo_contacto_id = tipo_contacto,
                organizacion_id = organizacion,
                grupo_id = grupo,
                funcion = funcion,
                jefe = jefe,
                correo = correo,
                )

        return HttpResponse('')







class PeticionCreateView(CreateView):
    template_name = 'Procesos/Peticiones/peticion_and_productos.html'
    model = Peticion
    form_class = PeticionForm


    def get_success_url(self):
        return '/peticion/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        producto_form = ProductoFormSet()
        analista_form = AnalistaFormSet()
        acuerdo_form = AcuerdoFormSet()
        seguimiento_form = SeguimientoFormSet()
        cierre_form = CierreFormSet()
        entrega_form = EntregaFormSet()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  producto_form=producto_form,
                                  analista_form=analista_form,
                                  acuerdo_form=acuerdo_form,
                                  seguimiento_form=seguimiento_form,
                                  cierre_form=cierre_form,
                                  entrega_form=entrega_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        producto_form = ProductoFormSet(self.request.POST)
        analista_form = AnalistaFormSet(self.request.POST)
        acuerdo_form = AcuerdoFormSet(self.request.POST)
        seguimiento_form = SeguimientoFormSet(self.request.POST)
        cierre_form = CierreFormSet(self.request.POST)
        entrega_form = EntregaFormSet(self.request.POST)
        
        if (form.is_valid() and producto_form.is_valid() and
            analista_form.is_valid() and
            acuerdo_form.is_valid() and
            seguimiento_form.is_valid() and
            cierre_form.is_valid() and
            entrega_form.is_valid()):
            return self.form_valid(form, producto_form, analista_form, acuerdo_form,
                                   seguimiento_form, cierre_form, entrega_form)
        else:
            return self.form_invalid(form, producto_form, analista_form, acuerdo_form,
                                     seguimiento_form, cierre_form, entrega_form)

    def form_valid(self, form, producto_form, analista_form, acuerdo_form,
                   seguimiento_form, cierre_form, entrega_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        producto_form.instance = self.object
        producto_form.save()
        
        analista_form.instance = self.object
        analista_form.save()

        acuerdo_form.instance = self.object
        acuerdo_form.save()

        seguimiento_form.instance = self.object
        seguimiento_form.save()

        cierre_form.instance = self.object
        cierre_form.save()

        entrega_form.instance = self.object
        entrega_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, producto_form, analista_form, acuerdo_form,
                     seguimiento_form, cierre_form, entrega_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  producto_form=producto_form,
                                  analista_form=analista_form,
                                  acuerdo_form=acuerdo_form,
                                  seguimiento_form=seguimiento_form,
                                  cierre_form=cierre_form,
                                  entrega_form=entrega_form))



class PeticionUpdateView(UpdateView):
    model = Peticion
    form_class = PeticionForm
    template_name = 'Procesos/Peticiones/peticion_and_productos.html'

    def get_success_url(self):
        return '/peticion/%i/#section1' % self.object.id

    def get_object(self):
        return Peticion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        producto_form = ProductoFormSet(instance=self.object)
        analista_form = AnalistaFormSet(instance=self.object)
        acuerdo_form = AcuerdoFormSet(instance=self.object)
        seguimiento_form = SeguimientoFormSet(instance=self.object)
        cierre_form = CierreFormSet(instance=self.object)
        entrega_form = EntregaFormSet(instance=self.object)
        
        return self.render_to_response(self.get_context_data(form=form,
                                                             producto_form=producto_form,
                                                             analista_form=analista_form,
                                                             acuerdo_form=acuerdo_form,
                                                             seguimiento_form=seguimiento_form,
                                                             cierre_form=cierre_form,
                                                             entrega_form=entrega_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 
        producto_form = ProductoFormSet(self.request.POST, instance=self.object)
        analista_form = AnalistaFormSet(self.request.POST, instance=self.object)
        acuerdo_form = AcuerdoFormSet(self.request.POST, instance=self.object)
        seguimiento_form = SeguimientoFormSet(self.request.POST, instance=self.object)
        cierre_form = CierreFormSet(self.request.POST, instance=self.object)
        entrega_form = EntregaFormSet(self.request.POST, instance=self.object)


        if (form.is_valid() and producto_form.is_valid() and
            analista_form.is_valid() and
            acuerdo_form.is_valid() and
            seguimiento_form.is_valid() and
            cierre_form.is_valid() and
            entrega_form.is_valid()):
            return self.form_valid(form, producto_form, analista_form, acuerdo_form,
                                   seguimiento_form, cierre_form, entrega_form)
        else:
            return self.form_invalid(form, producto_form, analista_form, acuerdo_form,
                                     seguimiento_form, cierre_form, entrega_form)

    def form_valid(self, form, producto_form, analista_form, acuerdo_form,
                   seguimiento_form, cierre_form, entrega_form):

        self.object = form.save()
        producto_form.instance = self.object
        producto_form.save()
        
        analista_form.instance = self.object
        analista_form.save()

        acuerdo_form.instance = self.object
        acuerdo_form.save()

        seguimiento_form.instance = self.object
        seguimiento_form.save()

        cierre_form.instance = self.object
        cierre_form.save()

        entrega_form.instance = self.object
        entrega_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, producto_form, analista_form, acuerdo_form,
                     seguimiento_form, cierre_form, entrega_form):
        return self.render_to_response(self.get_context_data(form=form,
                                                             producto_form=producto_form,
                                                             analista_form=analista_form,
                                                             acuerdo_form=acuerdo_form,
                                                             seguimiento_form=seguimiento_form,
                                                             cierre_form=cierre_form,
                                                             entrega_form=entrega_form))





class ProblemaCreateView(CreateView):
    template_name = 'Procesos/Problemas/problema_and_otros.html'
    model = Problema
    form_class = ProblemaForm


    def get_success_url(self):
        return '/problema/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        analista_form = AnalistaProblemaFormset()
        seguimiento_form = SeguimientoProblemaFormset()
        cierre_form = CierreProblemaFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  analista_form=analista_form,
                                  seguimiento_form=seguimiento_form,
                                  cierre_form=cierre_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        analista_form = AnalistaProblemaFormset(self.request.POST)
        seguimiento_form = SeguimientoProblemaFormset(self.request.POST)
        cierre_form = CierreProblemaFormset(self.request.POST)
        
        if (form.is_valid() and
            analista_form.is_valid() and
            seguimiento_form.is_valid() and
            cierre_form.is_valid()):
            return self.form_valid(form, analista_form,
                                   seguimiento_form, cierre_form)
        else:
            return self.form_invalid(form, analista_form,
                                     seguimiento_form, cierre_form)

    def form_valid(self, form, analista_form,
                   seguimiento_form, cierre_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        analista_form.instance = self.object
        analista_form.save()

        seguimiento_form.instance = self.object
        seguimiento_form.save()

        cierre_form.instance = self.object
        cierre_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, analista_form,
                     seguimiento_form, cierre_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  analista_form=analista_form,
                                  seguimiento_form=seguimiento_form,
                                  cierre_form=cierre_form))



class ProblemaUpdateView(UpdateView):
    model = Problema
    form_class = ProblemaForm
    template_name = 'Procesos/Problemas/problema_and_otros.html'

    def get_success_url(self):
        return '/problema/%i/#section1' % self.object.id

    def get_object(self):
        return Problema.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        analista_form = AnalistaProblemaFormset(instance=self.object)
        seguimiento_form = SeguimientoProblemaFormset(instance=self.object)
        cierre_form = CierreProblemaFormset(instance=self.object)
        
        return self.render_to_response(self.get_context_data(form=form,
                                                             analista_form=analista_form,
                                                             seguimiento_form=seguimiento_form,
                                                             cierre_form=cierre_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 
        analista_form = AnalistaProblemaFormset(self.request.POST, instance=self.object)
        seguimiento_form = SeguimientoProblemaFormset(self.request.POST, instance=self.object)
        cierre_form = CierreProblemaFormset(self.request.POST, instance=self.object)


        if (form.is_valid() and 
            analista_form.is_valid() and
            seguimiento_form.is_valid() and
            cierre_form.is_valid()):
            return self.form_valid(form, analista_form,
                                   seguimiento_form, cierre_form)
        else:
            return self.form_invalid(form, analista_form,
                                     seguimiento_form, cierre_form)

    def form_valid(self, form, analista_form, 
                   seguimiento_form, cierre_form):

        self.object = form.save()
        
        analista_form.instance = self.object
        analista_form.save()

        seguimiento_form.instance = self.object
        seguimiento_form.save()

        cierre_form.instance = self.object
        cierre_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, analista_form, 
                     seguimiento_form, cierre_form):
        return self.render_to_response(self.get_context_data(form=form,
                                                             analista_form=analista_form,
                                                             seguimiento_form=seguimiento_form,
                                                             cierre_form=cierre_form))



class CambioCreateView(CreateView):
    template_name = 'Procesos/Cambios/cambio_and_otros.html'
    model = Solicitud_Cambio
    form_class = CambioForm


    def get_success_url(self):
        return '/cambio/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        exclusivo_form = ExclusivoCambioFormset()
        planificacion_form = PlanificacionCambioFormset()
        responsable_form = ResponsableCambioFormset()
        seguimiento_form = SeguimientoCambioFormset()
        verificacion_form = VerificacionCambioFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  exclusivo_form=exclusivo_form,
                                  planificacion_form=planificacion_form,
                                  responsable_form=responsable_form,
                                  seguimiento_form=seguimiento_form,
                                  verificacion_form=verificacion_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        exclusivo_form = ExclusivoCambioFormset(self.request.POST)
        planificacion_form = PlanificacionCambioFormset(self.request.POST)
        responsable_form = ResponsableCambioFormset(self.request.POST)
        seguimiento_form = SeguimientoCambioFormset(self.request.POST)
        verificacion_form = VerificacionCambioFormset(self.request.POST)
        
        if (form.is_valid() and
            exclusivo_form.is_valid() and
            planificacion_form.is_valid() and
            responsable_form.is_valid() and
            seguimiento_form.is_valid() and
            verificacion_form.is_valid()):
            return self.form_valid(form, exclusivo_form,
                                   planificacion_form,
                                   responsable_form, seguimiento_form,
                                   verificacion_form)
        else:
            return self.form_invalid(form, exclusivo_form,
                                     planificacion_form,
                                     responsable_form, seguimiento_form,
                                     verificacion_form)

    def form_valid(self, form, exclusivo_form,
                   planificacion_form,
                   responsable_form, seguimiento_form,
                   verificacion_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        exclusivo_form.instance = self.object
        exclusivo_form.save()

        planificacion_form.instance = self.object
        planificacion_form.save()

        responsable_form.instance = self.object
        responsable_form.save()

        seguimiento_form.instance = self.object
        seguimiento_form.save()

        verificacion_form.instance = self.object
        verificacion_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, exclusivo_form,
                     planificacion_form,
                     responsable_form, seguimiento_form,
                     verificacion_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, exclusivo_form=exclusivo_form,
                                  planificacion_form=planificacion_form,
                                  responsable_form=responsable_form,
                                  seguimiento_form=seguimiento_form,
                                  verificacion_form=verificacion_form))




class CambioUpdateView(UpdateView):
    model = Solicitud_Cambio
    form_class = CambioForm
    template_name = 'Procesos/Cambios/cambio_and_otros.html'

    def get_success_url(self):
        return '/cambio/%i/#section1' % self.object.id

    def get_object(self):
        return Solicitud_Cambio.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        exclusivo_form = ExclusivoCambioFormset(instance=self.object)
        planificacion_form = PlanificacionCambioFormset(instance=self.object)
        responsable_form = ResponsableCambioFormset(instance=self.object)
        seguimiento_form = SeguimientoCambioFormset(instance=self.object)
        verificacion_form = VerificacionCambioFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, exclusivo_form=exclusivo_form,
                                                             planificacion_form=planificacion_form,
                                                             responsable_form=responsable_form,
                                                             seguimiento_form=seguimiento_form,
                                                             verificacion_form=verificacion_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        exclusivo_form = ExclusivoCambioFormset(self.request.POST, instance=self.object)
        planificacion_form = PlanificacionCambioFormset(self.request.POST, instance=self.object)
        responsable_form = ResponsableCambioFormset(self.request.POST, instance=self.object)
        seguimiento_form = SeguimientoCambioFormset(self.request.POST, instance=self.object)
        verificacion_form = VerificacionCambioFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            exclusivo_form.is_valid() and
            planificacion_form.is_valid() and
            responsable_form.is_valid() and
            seguimiento_form.is_valid() and
            verificacion_form.is_valid()):
            return self.form_valid(form, exclusivo_form,
                                   planificacion_form,
                                   responsable_form, seguimiento_form,
                                   verificacion_form)
        else:
            return self.form_invalid(form, exclusivo_form,
                                     planificacion_form,
                                     responsable_form, seguimiento_form,
                                     verificacion_form)

    def form_valid(self, form, exclusivo_form,
                   planificacion_form,
                   responsable_form, seguimiento_form,
                   verificacion_form):

        self.object = form.save()

        exclusivo_form.instance = self.object
        exclusivo_form.save()

        planificacion_form.instance = self.object
        planificacion_form.save()

        responsable_form.instance = self.object
        responsable_form.save()

        seguimiento_form.instance = self.object
        seguimiento_form.save()

        verificacion_form.instance = self.object
        verificacion_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, exclusivo_form,
                     planificacion_form,
                     responsable_form, seguimiento_form,
                     verificacion_form):
        return self.render_to_response(self.get_context_data(form=form, exclusivo_form=exclusivo_form,
                                                             planificacion_form=planificacion_form,
                                                             responsable_form=responsable_form,
                                                             seguimiento_form=seguimiento_form,
                                                             verificacion_form=verificacion_form))






class ImpresoraCreateView(CreateView):
    template_name = 'Procesos/Configuracion/impresora_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/impresora/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        impresora_form = ImpresoraFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  impresora_form=impresora_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        impresora_form = ImpresoraFormset(self.request.POST)
        
        if (form.is_valid() and
            impresora_form.is_valid()):
            return self.form_valid(form, impresora_form)
        else:
            return self.form_invalid(form, impresora_form)

    def form_valid(self, form, impresora_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        impresora_form.instance = self.object
        impresora_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, impresora_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, impresora_form=impresora_form))





class ImpresoraUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/impresora_and_otros.html'

    def get_success_url(self):
        return '/impresora/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        impresora_form = ImpresoraFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, impresora_form=impresora_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        impresora_form = ImpresoraFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            impresora_form.is_valid()):
            return self.form_valid(form, impresora_form)
        else:
            return self.form_invalid(form, impresora_form)

    def form_valid(self, form, impresora_form):

        self.object = form.save()

        impresora_form.instance = self.object
        impresora_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, impresora_form):
        return self.render_to_response(self.get_context_data(form=form, impresora_form=impresora_form))



class GranjaCreateView(CreateView):
    template_name = 'Procesos/Configuracion/granja_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/granja/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        granja_form = GranjaFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  granja_form=granja_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        granja_form = GranjaFormset(self.request.POST)
        
        if (form.is_valid() and
            granja_form.is_valid()):
            return self.form_valid(form, granja_form)
        else:
            return self.form_invalid(form, granja_form)

    def form_valid(self, form, granja_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        granja_form.instance = self.object
        granja_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, granja_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, granja_form=granja_form))





class GranjaUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/granja_and_otros.html'

    def get_success_url(self):
        return '/granja/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        granja_form = GranjaFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, granja_form=granja_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        granja_form = GranjaFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            granja_form.is_valid()):
            return self.form_valid(form, granja_form)
        else:
            return self.form_invalid(form, granja_form)

    def form_valid(self, form, granja_form):

        self.object = form.save()

        granja_form.instance = self.object
        granja_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, granja_form):
        return self.render_to_response(self.get_context_data(form=form, granja_form=granja_form))





class MaquinaCreateView(CreateView):
    template_name = 'Procesos/Configuracion/maquina_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/maquina_virtual/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        maquina_form = MaquinaFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  maquina_form=maquina_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        maquina_form = MaquinaFormset(self.request.POST)
        
        if (form.is_valid() and
            maquina_form.is_valid()):
            return self.form_valid(form, maquina_form)
        else:
            return self.form_invalid(form, maquina_form)

    def form_valid(self, form, maquina_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        maquina_form.instance = self.object
        maquina_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, maquina_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, maquina_form=maquina_form))





class MaquinaUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/maquina_and_otros.html'

    def get_success_url(self):
        return '/maquina_virtual/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        maquina_form = MaquinaFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, maquina_form=maquina_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        maquina_form = MaquinaFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            maquina_form.is_valid()):
            return self.form_valid(form, maquina_form)
        else:
            return self.form_invalid(form, maquina_form)

    def form_valid(self, form, maquina_form):

        self.object = form.save()

        maquina_form.instance = self.object
        maquina_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, maquina_form):
        return self.render_to_response(self.get_context_data(form=form, maquina_form=maquina_form))




class LicenciaCreateView(CreateView):
    template_name = 'Procesos/Configuracion/licencia_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/licencia/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        licencia_form = LicenciaFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  licencia_form=licencia_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        licencia_form = LicenciaFormset(self.request.POST)
        
        if (form.is_valid() and
            licencia_form.is_valid()):
            return self.form_valid(form, licencia_form)
        else:
            return self.form_invalid(form, licencia_form)

    def form_valid(self, form, licencia_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        licencia_form.instance = self.object
        licencia_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, licencia_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, licencia_form=licencia_form))





class LicenciaUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/licencia_and_otros.html'

    def get_success_url(self):
        return '/licencia/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        licencia_form = LicenciaFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, licencia_form=licencia_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        licencia_form = LicenciaFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            licencia_form.is_valid()):
            return self.form_valid(form, licencia_form)
        else:
            return self.form_invalid(form, licencia_form)

    def form_valid(self, form, licencia_form):

        self.object = form.save()

        licencia_form.instance = self.object
        licencia_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, licencia_form):
        return self.render_to_response(self.get_context_data(form=form, licencia_form=licencia_form))







class VlanCreateView(CreateView):
    template_name = 'Procesos/Configuracion/vlan_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/vlan/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        vlan_form = VlanFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  vlan_form=vlan_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        vlan_form = VlanFormset(self.request.POST)
        
        if (form.is_valid() and
            vlan_form.is_valid()):
            return self.form_valid(form, vlan_form)
        else:
            return self.form_invalid(form, vlan_form)

    def form_valid(self, form, vlan_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        vlan_form.instance = self.object
        vlan_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, vlan_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, vlan_form=vlan_form))





class VlanUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/vlan_and_otros.html'

    def get_success_url(self):
        return '/vlan/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        vlan_form = VlanFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, vlan_form=vlan_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        vlan_form = VlanFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            vlan_form.is_valid()):
            return self.form_valid(form, vlan_form)
        else:
            return self.form_invalid(form, vlan_form)

    def form_valid(self, form, vlan_form):

        self.object = form.save()

        vlan_form.instance = self.object
        vlan_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, vlan_form):
        return self.render_to_response(self.get_context_data(form=form, vlan_form=vlan_form))








class ContactoCreateView(CreateView):
    template_name = 'Procesos/Configuracion/contacto_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/contacto/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        contacto_form = ContactoFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  contacto_form=contacto_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        contacto_form = ContactoFormset(self.request.POST)
        
        if (form.is_valid() and
            contacto_form.is_valid()):
            return self.form_valid(form, contacto_form)
        else:
            return self.form_invalid(form, contacto_form)

    def form_valid(self, form, contacto_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        contacto_form.instance = self.object
        contacto_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, contacto_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, contacto_form=contacto_form))





class ContactoUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/contacto_and_otros.html'

    def get_success_url(self):
        return '/contacto/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        contacto_form = ContactoFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, contacto_form=contacto_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        contacto_form = ContactoFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            contacto_form.is_valid()):
            return self.form_valid(form, contacto_form)
        else:
            return self.form_invalid(form, contacto_form)

    def form_valid(self, form, contacto_form):

        self.object = form.save()

        contacto_form.instance = self.object
        contacto_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, contacto_form):
        return self.render_to_response(self.get_context_data(form=form, contacto_form=contacto_form))





class PCCreateView(CreateView):
    template_name = 'Procesos/Configuracion/pc_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/pc_laptop/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        pc_form = PCFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  pc_form=pc_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        pc_form = PCFormset(self.request.POST)
        
        if (form.is_valid() and
            pc_form.is_valid()):
            return self.form_valid(form, pc_form)
        else:
            return self.form_invalid(form, pc_form)

    def form_valid(self, form, pc_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        pc_form.instance = self.object
        pc_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, pc_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, pc_form=pc_form))





class PCUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/pc_and_otros.html'

    def get_success_url(self):
        return '/pc_laptop/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        pc_form = PCFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, pc_form=pc_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        pc_form = PCFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            pc_form.is_valid()):
            return self.form_valid(form, pc_form)
        else:
            return self.form_invalid(form, pc_form)

    def form_valid(self, form, pc_form):

        self.object = form.save()

        pc_form.instance = self.object
        pc_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, pc_form):
        return self.render_to_response(self.get_context_data(form=form, pc_form=pc_form))






class InstalacionCreateView(CreateView):
    template_name = 'Procesos/Configuracion/instalacion_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/instalacion_software/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        instalacion_form = InstalacionFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  instalacion_form=instalacion_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        instalacion_form = InstalacionFormset(self.request.POST)
        
        if (form.is_valid() and
            instalacion_form.is_valid()):
            return self.form_valid(form, instalacion_form)
        else:
            return self.form_invalid(form, instalacion_form)

    def form_valid(self, form, instalacion_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        instalacion_form.instance = self.object
        instalacion_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, instalacion_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, instalacion_form=instalacion_form))





class InstalacionUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/instalacion_and_otros.html'

    def get_success_url(self):
        return '/instalacion_software/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        instalacion_form = InstalacionFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, instalacion_form=instalacion_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        instalacion_form = InstalacionFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            instalacion_form.is_valid()):
            return self.form_valid(form, instalacion_form)
        else:
            return self.form_invalid(form, instalacion_form)

    def form_valid(self, form, instalacion_form):

        self.object = form.save()

        instalacion_form.instance = self.object
        instalacion_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, instalacion_form):
        return self.render_to_response(self.get_context_data(form=form, instalacion_form=instalacion_form))






class RackCreateView(CreateView):
    template_name = 'Procesos/Configuracion/rack_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/rack/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        rack_form = RackFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  rack_form=rack_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        rack_form = RackFormset(self.request.POST)
        
        if (form.is_valid() and
            rack_form.is_valid()):
            return self.form_valid(form, rack_form)
        else:
            return self.form_invalid(form, rack_form)

    def form_valid(self, form, rack_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        rack_form.instance = self.object
        rack_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, rack_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, rack_form=rack_form))





class RackUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/rack_and_otros.html'

    def get_success_url(self):
        return '/rack/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        rack_form = RackFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, rack_form=rack_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        rack_form = RackFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            rack_form.is_valid()):
            return self.form_valid(form, rack_form)
        else:
            return self.form_invalid(form, rack_form)

    def form_valid(self, form, rack_form):

        self.object = form.save()

        rack_form.instance = self.object
        rack_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, rack_form):
        return self.render_to_response(self.get_context_data(form=form, rack_form=rack_form))



class ServidorCreateView(CreateView):
    template_name = 'Procesos/Configuracion/servidor_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/servidor/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        servidor_form = ServidorFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  servidor_form=servidor_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        servidor_form = ServidorFormset(self.request.POST)
        
        if (form.is_valid() and
            servidor_form.is_valid()):
            return self.form_valid(form, servidor_form)
        else:
            return self.form_invalid(form, servidor_form)

    def form_valid(self, form, servidor_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        servidor_form.instance = self.object
        servidor_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, servidor_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, servidor_form=servidor_form))





class ServidorUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/servidor_and_otros.html'

    def get_success_url(self):
        return '/servidor/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        servidor_form = ServidorFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, servidor_form=servidor_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        servidor_form = ServidorFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            servidor_form.is_valid()):
            return self.form_valid(form, servidor_form)
        else:
            return self.form_invalid(form, servidor_form)

    def form_valid(self, form, servidor_form):

        self.object = form.save()

        servidor_form.instance = self.object
        servidor_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, servidor_form):
        return self.render_to_response(self.get_context_data(form=form, servidor_form=servidor_form))





class HypervisorCreateView(CreateView):
    template_name = 'Procesos/Configuracion/hypervisor_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/hypervisor/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        hypervisor_form = HypervisorFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  hypervisor_form=hypervisor_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        hypervisor_form = HypervisorFormset(self.request.POST)
        
        if (form.is_valid() and
            hypervisor_form.is_valid()):
            return self.form_valid(form, hypervisor_form)
        else:
            return self.form_invalid(form, hypervisor_form)

    def form_valid(self, form, hypervisor_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        hypervisor_form.instance = self.object
        hypervisor_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, hypervisor_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, hypervisor_form=hypervisor_form))





class HypervisorUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/hypervisor_and_otros.html'

    def get_success_url(self):
        return '/hypervisor/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        hypervisor_form = HypervisorFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, hypervisor_form=hypervisor_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        hypervisor_form = HypervisorFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            hypervisor_form.is_valid()):
            return self.form_valid(form, hypervisor_form)
        else:
            return self.form_invalid(form, hypervisor_form)

    def form_valid(self, form, hypervisor_form):

        self.object = form.save()

        hypervisor_form.instance = self.object
        hypervisor_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, hypervisor_form):
        return self.render_to_response(self.get_context_data(form=form, hypervisor_form=hypervisor_form))








class TelefonoCreateView(CreateView):
    template_name = 'Procesos/Configuracion/telefono_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/telefono_celular/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        telefono_form = TelefonoFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  telefono_form=telefono_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        telefono_form = TelefonoFormset(self.request.POST)
        
        if (form.is_valid() and
            telefono_form.is_valid()):
            return self.form_valid(form, telefono_form)
        else:
            return self.form_invalid(form, telefono_form)

    def form_valid(self, form, telefono_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        telefono_form.instance = self.object
        telefono_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, telefono_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, telefono_form=telefono_form))





class TelefonoUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/telefono_and_otros.html'

    def get_success_url(self):
        return '/telefono_celular/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        telefono_form = TelefonoFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, telefono_form=telefono_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        telefono_form = TelefonoFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            telefono_form.is_valid()):
            return self.form_valid(form, telefono_form)
        else:
            return self.form_invalid(form, telefono_form)

    def form_valid(self, form, telefono_form):

        self.object = form.save()

        telefono_form.instance = self.object
        telefono_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, telefono_form):
        return self.render_to_response(self.get_context_data(form=form, telefono_form=telefono_form))






class DispositivoCreateView(CreateView):
    template_name = 'Procesos/Configuracion/dispositivo_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/dispositivo_red/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        dispositivo_form = DispositivoFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  dispositivo_form=dispositivo_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        dispositivo_form = DispositivoFormset(self.request.POST)
        
        if (form.is_valid() and
            dispositivo_form.is_valid()):
            return self.form_valid(form, dispositivo_form)
        else:
            return self.form_invalid(form, dispositivo_form)

    def form_valid(self, form, dispositivo_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        dispositivo_form.instance = self.object
        dispositivo_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, dispositivo_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, dispositivo_form=dispositivo_form))





class DispositivoUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/dispositivo_and_otros.html'

    def get_success_url(self):
        return '/dispositivo_red/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        dispositivo_form = DispositivoFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, dispositivo_form=dispositivo_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        dispositivo_form = DispositivoFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            dispositivo_form.is_valid()):
            return self.form_valid(form, dispositivo_form)
        else:
            return self.form_invalid(form, dispositivo_form)

    def form_valid(self, form, dispositivo_form):

        self.object = form.save()

        dispositivo_form.instance = self.object
        dispositivo_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, dispositivo_form):
        return self.render_to_response(self.get_context_data(form=form, dispositivo_form=dispositivo_form))






class InterfazCreateView(CreateView):
    template_name = 'Procesos/Configuracion/interfaz_and_otros.html'
    model = General_Configuracion
    form_class = GeneralForm


    def get_success_url(self):
        return '/interfaz_red/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        interfaz_form = InterfazFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  interfaz_form=interfaz_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        interfaz_form = InterfazFormset(self.request.POST)
        
        if (form.is_valid() and
            interfaz_form.is_valid()):
            return self.form_valid(form, interfaz_form)
        else:
            return self.form_invalid(form, interfaz_form)

    def form_valid(self, form, interfaz_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        interfaz_form.instance = self.object
        interfaz_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, interfaz_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, interfaz_form=interfaz_form))


class InterfazUpdateView(UpdateView):
    model = General_Configuracion
    form_class = GeneralForm
    template_name = 'Procesos/Configuracion/interfaz_and_otros.html'

    def get_success_url(self):
        return '/interfaz_red/%i/#section1' % self.object.id

    def get_object(self):
        return General_Configuracion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        interfaz_form = InterfazFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, interfaz_form=interfaz_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        interfaz_form = InterfazFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            interfaz_form.is_valid()):
            return self.form_valid(form, interfaz_form)
        else:
            return self.form_invalid(form, interfaz_form)

    def form_valid(self, form, interfaz_form):

        self.object = form.save()

        interfaz_form.instance = self.object
        interfaz_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, interfaz_form):
        return self.render_to_response(self.get_context_data(form=form, interfaz_form=interfaz_form))







class ReclamacionCreateView(CreateView):
    template_name = 'Procesos/Clientes/reclamacion_and_otros.html'
    model = Reclamacion
    form_class = ReclamacionForm


    def get_success_url(self):
        return '/reclamacion/%i/#section1' % self.object.id

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        reclamacion_form = ReclamacionFormset()
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  reclamacion_form=reclamacion_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        reclamacion_form = ReclamacionFormset(self.request.POST)
        
        if (form.is_valid() and
            reclamacion_form.is_valid()):
            return self.form_valid(form, reclamacion_form)
        else:
            return self.form_invalid(form, reclamacion_form)

    def form_valid(self, form, reclamacion_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        reclamacion_form.instance = self.object
        reclamacion_form.save()
        
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, reclamacion_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, reclamacion_form=reclamacion_form))


class ReclamacionUpdateView(UpdateView):
    model = Reclamacion
    form_class = ReclamacionForm
    template_name = 'Procesos/Clientes/reclamacion_and_otros.html'

    def get_success_url(self):
        return '/reclamacion/%i/#section1' % self.object.id

    def get_object(self):
        return Reclamacion.objects.get(id=self.kwargs.get("id"))
    
    def get(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)

        reclamacion_form = ReclamacionFormset(instance=self.object)
        
        
        return self.render_to_response(self.get_context_data(form=form, reclamacion_form=reclamacion_form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        form_class=self.get_form_class()
        form = self.get_form(form_class)
 

        reclamacion_form = ReclamacionFormset(self.request.POST, instance=self.object)
        


        if (form.is_valid() and 
            reclamacion_form.is_valid()):
            return self.form_valid(form, reclamacion_form)
        else:
            return self.form_invalid(form, reclamacion_form)

    def form_valid(self, form, reclamacion_form):

        self.object = form.save()

        reclamacion_form.instance = self.object
        reclamacion_form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, reclamacion_form):
        return self.render_to_response(self.get_context_data(form=form, reclamacion_form=reclamacion_form))












def prepare_blank_answers(encuestado):
    for pregunta in encuestado.proceso.preguntas_set.all():
        respuesta = ClienteAnswer(encuestado=encuestado,
                                         pregunta=pregunta)
        respuesta.save()



def answer_form(request, id):
    encuestado = get_object_or_404(Encuestado, id=id)
    
    if len(encuestado.clienteanswer_set.all()) == 0:
        prepare_blank_answers(encuestado)
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST, instance=encuestado)
        if formset.is_valid():
            formset.save()
            new_encuesta = formset.save()

            if encuestado.proceso_id==2:
                    total= ClienteAnswer.objects.values('respuesta').filter(encuestado_id=id).aggregate(Sum('respuesta')).values()[0]

                    try:
                            encuestado.calificacion=(total*100)/28
                    except TypeError:
                            total = 0
                            encuestado.calificacion=None


                    encuestado.save(update_fields=["calificacion"])


                    if encuestado.calificacion==None:
                            encuestado.estado=""
                            encuestado.save(update_fields=["estado"]) 

                    elif encuestado.calificacion<70:
                            encuestado.estado="No aprobado"
                            encuestado.save(update_fields=["estado"])
                            
                    elif encuestado.calificacion>70:
                            encuestado.estado="Aprobado"
                            encuestado.save(update_fields=["estado"])


            if encuestado.proceso_id==3:
                    total= ClienteAnswer.objects.values('respuesta').filter(encuestado_id=id).aggregate(Sum('respuesta')).values()[0]

                    try:
                            encuestado.calificacion=(total*100)/16
                    except TypeError:
                            total = 0
                            encuestado.calificacion=None


                    encuestado.save(update_fields=["calificacion"])


                    if encuestado.calificacion==None:
                            encuestado.estado=""
                            encuestado.save(update_fields=["estado"]) 

                    elif encuestado.calificacion<70:
                            encuestado.estado="No aprobado"
                            encuestado.save(update_fields=["estado"])
                            
                    elif encuestado.calificacion>70:
                            encuestado.estado="Aprobado"
                            encuestado.save(update_fields=["estado"])                        


            if encuestado.proceso_id==4:
                    total= ClienteAnswer.objects.values('respuesta').filter(encuestado_id=id).aggregate(Sum('respuesta')).values()[0]

                    try:
                            encuestado.calificacion=(total*100)/52
                    except TypeError:
                            total = 0
                            encuestado.calificacion=None


                    encuestado.save(update_fields=["calificacion"])


                    if encuestado.calificacion==None:
                            encuestado.estado=""
                            encuestado.save(update_fields=["estado"]) 

                    elif encuestado.calificacion<70:
                            encuestado.estado="No aprobado"
                            encuestado.save(update_fields=["estado"])
                            
                    elif encuestado.calificacion>70:
                            encuestado.estado="Aprobado"
                            encuestado.save(update_fields=["estado"])
            
            return redirect('/encuesta/%s/#section1' % id)
    else:
        formset = AnswerFormSet(instance=encuestado)
    return render(request, 'Procesos/Clientes/respuesta_form.html',
            {'formset':formset, 'encuestado':encuestado})



def crearEncuesta(request, template_name='Procesos/Clientes/crearEvaluacion.html'):
        form = ClienteForm(request.POST or None)
        if form.is_valid():
                form.save()
                new_contact = form.save()
                return redirect('/encuesta/%s/#section1' % new_contact.pk)
        return render(request, template_name, {'form':form})






def prepare_blank_answers2(evaluacion_proveedores):
    for pregunta in evaluacion_proveedores.proceso.preguntas_set.all():
        respuesta = ProveedorAnswer(evaluacion_proveedores=evaluacion_proveedores,
                                         pregunta=pregunta)
        respuesta.save()



def answer_form2(request, id):
    evaluacion_proveedores = get_object_or_404(Evaluacion_Proveedores, id=id)
    
    if len(evaluacion_proveedores.proveedoranswer_set.all()) == 0:
        prepare_blank_answers2(evaluacion_proveedores)
    if request.method == 'POST':
        formset = ProveedorFormSet(request.POST, instance=evaluacion_proveedores)
        if formset.is_valid():
            formset.save()
            new_encuesta = formset.save()

            if evaluacion_proveedores.proceso_id==5:
                    total= ProveedorAnswer.objects.values('respuesta').filter(evaluacion_proveedores_id=id).aggregate(Sum('respuesta')).values()[0]
                    #hacer calculo mas cercano a porcentajes de desempeno

                    try:
                            evaluacion_proveedores.calificacion=((total+4)*100)/16
                    except TypeError:
                            total = 0
                            evaluacion_proveedores.calificacion=None


                    evaluacion_proveedores.save(update_fields=["calificacion"])


                    if evaluacion_proveedores.calificacion==None:
                            evaluacion_proveedores.estado2=""
                            evaluacion_proveedores.save(update_fields=["estado2"]) 

                    elif evaluacion_proveedores.calificacion<70:
                            evaluacion_proveedores.estado2="No aprobado"
                            evaluacion_proveedores.save(update_fields=["estado2"])
                            
                    elif evaluacion_proveedores.calificacion>70:
                            evaluacion_proveedores.estado2="Aprobado"
                            evaluacion_proveedores.save(update_fields=["estado2"])


            
            return redirect('/evaluacion/%s/#section1' % id)
    else:
        formset = ProveedorFormSet(instance=evaluacion_proveedores)
    return render(request, 'Procesos/Proveedores/respuesta_form.html',
            {'formset':formset, 'encuestado':evaluacion_proveedores})


