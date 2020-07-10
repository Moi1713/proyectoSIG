from django.db import models

# Create your models here.

class Supervisor(models.Model):
	salid = models.CharField(max_length=10)
	nombre = models.CharField(max_length=150)
	teamname = models.CharField(max_length=150)

class TeamManager(models.Model):
	salid = models.CharField(max_length=10)
	empsalid = models.CharField(max_length=10)
	nombre = models.CharField(max_length=150)
	teamname = models.CharField(max_length=150)
	supid = models.ForeignKey(Supervisor, null= True, on_delete=models.SET_NULL)

class Empleado(models.Model):
	salid = models.CharField(max_length=10)
	nombre = models.CharField(max_length=150)
	tmid = models.ForeignKey(TeamManager, null= True, on_delete=models.SET_NULL)
	supid = models.ForeignKey(Supervisor, null= True, on_delete=models.SET_NULL)
	windowsuser = models.CharField(max_length=150)
	peopleid = models.CharField(max_length=10)

class Ausencia(models.Model):
	idausencia = models.IntegerField()
	salid = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL)
	dia = models.DateField()
	compliance = models.FloatField()

class Survey(models.Model):
	caseid = models.CharField(max_length=25)
	caserecieved = models.DateField()
	casecreated = models.DateField()
	salid = models.ForeignKey(Empleado, null= True, on_delete=models.SET_NULL)
	surveytype = models.CharField(max_length=5)# DSAT, CSAT
	surveycomments = models.CharField(max_length=1024)
	callid = models.CharField(max_length=150)
	itinerario = models.CharField(max_length=150)