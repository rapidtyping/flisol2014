from django.db import models
from flisol.apps.home.models import UserProfile

class Inscrito(models.Model):
	dni = models.CharField(max_length=8,verbose_name='DNI')
	nombres = models.CharField(max_length=120,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=120,verbose_name='Apellidos')
	email = models.EmailField(max_length=200,verbose_name='E-Mail')
	telefono = models.CharField(max_length=15,verbose_name='Telefono - Celular')
	organizacion = models.CharField(max_length=200)
	fecha = models.DateTimeField(auto_now_add=True,editable=False,blank=True)
	certificado = models.BooleanField(default=False)
	asistencia = models.BooleanField(default=False)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

	class Meta:
		ordering = ['-fecha']

class Publicacion(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Publicacion/%s/%s"%(self.titulo,str(filename))
		return ruta

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True

	titulo = models.CharField(max_length=120,verbose_name='Titulo de la Publicacion')
	descripcion = models.TextField(verbose_name='Contenido de la publicacion')
	imagen = models.ImageField(upload_to=url,null=True,blank=True)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	fecha_edicion = models.DateTimeField(auto_now=True)
	etiquetas = models.CharField(max_length=225)
	userProfile = models.ForeignKey(UserProfile,verbose_name='Usuario')

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['-fecha_registro']

class Encuesta(models.Model):
	titulo = models.CharField(max_length=120,verbose_name='Titulo de la Encuesta')
	descripcion = models.TextField(verbose_name='Descripcion de la Encuesta')
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	userProfile = models.ForeignKey(UserProfile,verbose_name='Usuario')

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['-fecha_creacion']

class Pregunta(models.Model):
	formulacion = models.CharField(max_length=250,verbose_name='Pregunta')
	obligatoria = models.BooleanField(default=True)
	encuesta = models.ForeignKey(Encuesta,verbose_name='Encuesta')

	def __unicode__(self):
		return self.formulacion

	class Meta:
		ordering = ['-encuesta']

class Opcion(models.Model):
	opcion = models.CharField(max_length=300)
	votos = models.IntegerField(null=True)
	pregunta = models.ForeignKey(Pregunta,verbose_name='Pregunta')

	def __unicode__(self):
		return self.opcion

	class Meta:
		ordering = ['-pregunta']

class Grupo(models.Model):
	nombre_grupo = models.CharField(max_length=120,verbose_name='Nombre del Grupo')

	def __unicode__(self):
		return self.nombre_grupo

class Asignacion(models.Model):
	fecha_inicio = models.DateTimeField(auto_now_add=True,editable=True,blank=True)
	fecha_finalizacion = models.DateTimeField(auto_now=True,editable=False,blank=True)
	activo = models.BooleanField(default=False)
	encuesta = models.ForeignKey(Encuesta)
	grupo = models.ForeignKey(Grupo)

	class Meta:
		ordering = ['-fecha_inicio']