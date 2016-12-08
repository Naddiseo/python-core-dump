
from django.http.response import HttpResponse
from spam.models import Egg

def fail(request, *args, **kwargs):
	Egg.objects.get_or_create(color=1,breed=2)
	list(Egg.objects.all().only('color'))
	return HttpResponse('SUCCESS?')
