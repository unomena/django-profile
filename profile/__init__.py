from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured

from profile import utils
    
auth_profile_module = getattr(settings, 'AUTH_PROFILE_MODULE', None)
if not auth_profile_module:
    raise ImproperlyConfigured("You must provide an AUTH_PROFILE_MODULE setting.")
   
# connect profile property to user

def get_profile(user):
    profile_model = utils.get_profile_model()
    return profile_model.objects.get_or_create(user=user)[0]

User.profile = property(lambda user: get_profile(user))