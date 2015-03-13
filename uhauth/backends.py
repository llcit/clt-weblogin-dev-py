# uhauth/backends.py
from django_cas.backends import CASBackend



class UHCASBackend(CASBackend):
	
	"""CAS authentication backend with user data populated from UH LDAP"""
	
	def authenticate(self, ticket, service, request):
		"""
		Authenticates CAS ticket and authenticates a user. No additional attributes other than username are returned.
		Works with CAS_VERSION = '1' set in settings file.
		"""
		# ssl.PROTOCOL_TLSv1
		print 'uhauth'
		user = super(UHCASBackend, self).authenticate(ticket, service, request)
		return user

class UHCASAttributesBackend(CASBackend):
	
	"""CAS authentication backend with user data populated from UH LDAP"""
	
	def authenticate(self, ticket, service, request):
		"""
		Authenticates CAS ticket and retrieves additional (exposed) user data.
		Works only if CAS_VERSION = 'CAS_2_SAML_1_0' is set in the settings file.
		"""
		user = super(UHCASAttributesBackend, self).authenticate(ticket, service, request)
		
		print 'USER==>', user
		print 'SESSION DATA? ==>', request.session['attributes']
		return user

