from django.shortcuts import render
from .models import *

from django.http import HttpResponse

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def login(request):
	return render(request, 'login.html')

def inicio(request):
	return render(request, 'control_impactos/index.html')

def supervisors(request):
	supervisors = Supervisor.objects.all()
	return render(request, 'control_impactos/supervisors.html', { "supervisors":supervisors})

#Generacion de Reportes
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Descarga de Reportes
def DownloadPDF(request, type):
	response = ViewPDF(request, type)
	filename = "%s_List.pdf" %(type)
	content = "attachment; filename='%s'" %(filename)
	response['Content-Disposition'] = content
	return response

#Obtencion de datos y seleccion de plantilla para el reporte
def ViewPDF(request, type):
	if(type == 'supervisor'):
		supervisors = Supervisor.objects.all()
		pdf = render_to_pdf('reportes/supervisor_rep.html', {"supervisors":supervisors})
		return HttpResponse(pdf, content_type='application/pdf')
