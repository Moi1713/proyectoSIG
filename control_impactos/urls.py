from django.urls import path
from . import views

urlpatterns = [
	path('', views.inicio, name='inicio'),

	path('login/', views.login, name='login'),

	path('supervisors/', views.supervisors, name='supervisors'),
	#PDF
	path('pdf_view/<str:type>/', views.ViewPDF, name="pdf_view"),
	path('pdf_download/<str:type>/', views.DownloadPDF, name="pdf_download"),
]