from django.contrib import admin
from flisol.apps.home.models import UserProfile

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password','email','user')
	search_fields = ['username']
	fields = ('username','password','email','user')

admin.site.register(UserProfile,UserAdmin)