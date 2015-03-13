# uhauth/backends.py
"""
	Using/subclassing django-cas downloaded from here:
	https://bitbucket.org/cpcc/django-cas/overview

	Installed with python setup.py install in a virtualenv of course
"""
from django_cas.backends import CASBackend



class UHCASBackend(CASBackend):
	
	"""CAS authentication backend with user data populated from UH LDAP"""
	
	def authenticate(self, ticket, service, request):
		"""
		Authenticates CAS ticket and authenticates a user. No additional attributes other than username are returned.
		Works with CAS_VERSION = '1' set in settings file.
		"""
		
		user = super(UHCASBackend, self).authenticate(ticket, service, request)
		return user

class UHCASAttributesBackend(CASBackend):
	
	"""CAS authentication backend with user data populated from UH LDAP"""
	
	def authenticate(self, ticket, service, request):
		"""
		Authenticates CAS ticket and retrieves additional (exposed) user data.
		Works only if CAS_VERSION = 'CAS_2_SAML_1_0' is set in the settings file.
		"""

		user= super(UHCASAttributesBackend, self).authenticate(ticket, service, request)
		
		user_attrs = request.session['attributes']
		if not user.first_name:
			user.first_name = user_attrs['givenName']
		if not user.last_name:
			user.last_name = user_attrs['sn']
		user.save()
		# Can use this if you need this logic.
		# affiliation = attrs['eduPersonAffiliation']
		
		return user

