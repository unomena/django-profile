from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from profile import utils

# add profile inline to user admin
profile_model = utils.get_profile_model()

if profile_model:
    # setup profile inline
    class ProfileInline(admin.StackedInline):
        model = profile_model
        fk_name = 'user'

    class UserAdmin(UserAdmin):
        inlines = [
            ProfileInline,
        ]

    # Unregister default django User admin 
    admin.site.unregister(User)

    # Register our customized User admin 
    admin.site.register(User, UserAdmin)
