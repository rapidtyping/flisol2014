from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	email = models.EmailField(max_length=100,verbose_name='Correo Electronico')
	user = models.ForeignKey(User,verbose_name='Usuario')

	def __unicode__(self):
		return self.username

	class Meta:
		ordering = ['-username']