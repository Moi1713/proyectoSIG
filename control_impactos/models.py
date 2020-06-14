from django.db import models

# Create your models here.

'''
class Supervisor(models.Model):
	SALID = models.CharField(max_length=10)
	Tea_SALID = 
	Nombre = models.CharField(max_length=150)
	Team_Name = models.CharField(max_length=150)
	Sup_Id = IntegerField()

class TeamManager(models.Model):
	SALID = models.CharField(max_length=10)
	Emp_SALID = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=150)
	Team_Name = models.CharField(max_length=150)

class Empleado(models.Model):
	SALID = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=150)
	TM_ID = 
	Sup_ID = 
	Windows_User = models.CharField(max_length=150)
	People_ID = 

class Ausencias(models.Model):
	ID_Ausencia = models.IntegerField()
	SALID = models.ForeignKey(Empleado, on_delete=models.SET_NULL)
	Dia = models.DateField()
	Compliance = 

class Survey(models.Model):
	Case_id = models.CharField(max_length=25)
	Case_Recieved = models.DateField()
	Case_Created = models.DateField()
	SALID = models.CharField(max_length=10)
	Survey_Type = models.CharField(max_length=15)
	Survey_Comments = models.CharField(max_length=1024)
	Call_ID = 
	Itinerario = 
'''