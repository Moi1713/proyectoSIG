from django.db import models

# Create your models here.

class Supervisor(models.Model):
	SALID = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=150)
	Team_Name = models.CharField(max_length=150)

class TeamManager(models.Model):
	SALID = models.CharField(max_length=10)
	Emp_SALID = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=150)
	Team_Name = models.CharField(max_length=150)
	Sup_Id = models.ForeignKey(Supervisor, null= True, on_delete=models.SET_NULL)

class Empleado(models.Model):
	SALID = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=150)
	TM_ID = models.ForeignKey(TeamManager, null= True, on_delete=models.SET_NULL)
	Sup_ID = models.ForeignKey(Supervisor, null= True, on_delete=models.SET_NULL)
	Windows_User = models.CharField(max_length=150)
	People_ID = models.CharField(max_length=10)

class Ausencia(models.Model):
	ID_Ausencia = models.IntegerField()
	SALID = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL)
	Dia = models.DateField()
	Compliance = models.FloatField()

class Survey(models.Model):
	Case_id = models.CharField(max_length=25)
	Case_Recieved = models.DateField()
	Case_Created = models.DateField()
	SALID = models.ForeignKey(Empleado, null= True, on_delete=models.SET_NULL)
	Survey_Type = models.CharField(max_length=5)# DSAT, CSAT
	Survey_Comments = models.CharField(max_length=1024)
	Call_ID = models.CharField(max_length=150)
	Itinerario = models.CharField(max_length=150)