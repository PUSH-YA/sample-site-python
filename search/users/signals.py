
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

# create profile when user is created, instance and created are automatic
# @receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    print('Profile created for user :)', 
        '\nInstance: ', instance,
        '\nCreated: ',created)
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

# delete user with profile
def delete_user(sender, instance, **kwargs):
    user = instance.user
    print('User Deleted :(')
    print('Instance: ', instance)
    user.delete()

    

# after saving/delete, callback to update user/profile
post_save.connect(create_profile, sender = User)
post_save.connect(update_user, sender = Profile)
post_delete.connect(delete_user, sender = Profile)