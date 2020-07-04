from django.db import models

# Create your models here.

class Supervisor(models.Model):
	salId = models.CharField(max_length=10)
	nombre = models.CharField(max_length=150)
	teamName = models.CharField(max_length=150)

class TeamManager(models.Model):
	salId = models.CharField(max_length=10)
	empSalId = models.CharField(max_length=10)
	nombre = models.CharField(max_length=150)
	teamName = models.CharField(max_length=150)
	supId = models.ForeignKey(Supervisor, null= True, on_delete=models.SET_NULL)

class Empleado(models.Model):
	salId = models.CharField(max_length=10)
	nombre = models.CharField(max_length=150)
	tmId = models.ForeignKey(TeamManager, null= True, on_delete=models.SET_NULL)
	supId = models.ForeignKey(Supervisor, null= True, on_delete=models.SET_NULL)
	windowsUser = models.CharField(max_length=150)
	peopleId = models.CharField(max_length=10)

class Ausencia(models.Model):
	idAusencia = models.IntegerField()
	salId = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL)
	dia = models.DateField()
	compliance = models.FloatField()

class Survey(models.Model):
	caseId = models.CharField(max_length=25)
	caseRecieved = models.DateField()
	caseCreated = models.DateField()
	salId = models.ForeignKey(Empleado, null= True, on_delete=models.SET_NULL)
	surveyType = models.CharField(max_length=5)# DSAT, CSAT
	surveyComments = models.CharField(max_length=1024)
	callId = models.CharField(max_length=150)
	itinerario = models.CharField(max_length=150)