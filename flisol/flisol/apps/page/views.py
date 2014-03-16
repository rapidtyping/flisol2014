from django.shortcuts import render_to_response
from django.template import RequestContext
from flisol.apps.page.forms import addInscritoForm
from flisol.apps.page.models import Inscrito
from django.http import HttpResponseRedirect

def index_view(request):
	info = "iniciado"
	if request.method == "POST":
		form = addInscritoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			info = "Guardado satisfactoriamente"
			#return HttpResponseRedirect('/producto/%s'%add.id)
	else:
		form = addInscritoForm()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/index.html',ctx,context_instance = RequestContext(request))