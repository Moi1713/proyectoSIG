from django.shortcuts import render, redirect
from django.http import HttpResponse

#import para modelos
from .models import *

#import para login y logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#import de decorators para permisos
from django.contrib.auth.decorators import login_required

#import para generar reportes
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import psycopg2

# Create your views here.

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('usuario')
		password = request.POST.get('contrasenia')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('inicio')
		else:
			messages.info(request, 'Usuario o contraseña incorrectos')
			return render(request, 'login.html')

	return render(request, 'login.html')

def logoutUser(request):
	logout(request)
	messages.info(request, 'Gracias. Lo esperamos nuevamente.')
	return redirect('login')

@login_required(login_url='login')
def inicio(request):
	return render(request, 'control_impactos/index.html')

def supervisors(request):
	supervisors = Supervisor.objects.all()
	return render(request, 'control_impactos/supervisors.html', { "supervisors":supervisors })

def desempenio(request):
	
	return render(request, 'control_impactos/desempenio.html')

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
	else:
		if(type == 'desempenio'):
			
			pdf = render_to_pdf('reportes/desempenio_rep.html')
			return HttpResponse(pdf, content_type='application/pdf')
