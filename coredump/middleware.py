class Foo:
	def __init__(self, get_response = None):
		self.get_response = get_response
	
	def __call__(self, request):
		response = None
		if self.get_response is not None:
			response = self.get_response(request)
		return response
