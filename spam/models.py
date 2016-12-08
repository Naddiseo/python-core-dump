
from django.db import models
from django.db.models.expressions import Expression
from django.db.models.signals import post_init
from django.dispatch.dispatcher import receiver

class Egg(models.Model):
	color = models.IntegerField(unique = True)
	breed = models.IntegerField()

# private
@receiver([post_init], dispatch_uid = '#_reset_state')
def _reset_state(sender, instance, **kwargs):
	if not isinstance(instance, Egg):
		return
	
	update_fields = kwargs.pop('update_fields', None)
	
	if instance.pk:
		state = _instance_state_dict(instance, update_fields = update_fields)
	else:
		state = {
			f.attname: None for f in type(instance)._meta.fields
			if f.editable and not f.primary_key
		}
	
	instance._saved_state = state


# private
def _instance_state_dict(instance, update_fields = None):
	model = type(instance)
	meta = model._meta
	fields = meta.fields
	
	fields = [f for f in fields if f.editable and not f.primary_key]
	
	return {
		f.attname: _get_attr(f, instance)
		for f in fields
	}

def _get_attr(f, instance):
	v = getattr(instance, f.attname)
	if isinstance(v, Expression):
		# F() nodes aren't representable as python values
		return v
	return f.to_python(v)
