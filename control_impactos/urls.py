from django.urls import path
from . import views

urlpatterns = [
	#Paginas
	path('', views.inicio, name='inicio'),
	#Login/Logout
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	#Ejemplo lista
	path('supervisors/', views.supervisors, name='supervisors'),
	path('rendimiento/', views.rendimiento, name='rendimiento'),
	#PDF
	path('pdf_view/<str:type>/', views.ViewPDF, name="pdf_view"),
	path('pdf_download/<str:type>/', views.DownloadPDF, name="pdf_download"),
]