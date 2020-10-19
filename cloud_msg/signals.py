def auto_profile(user, *args, **kwargs):
    from cloud_msg.models import UserProfile
    user = UserProfile.objects.create(user=user, avatar=kwargs.get('avatar'))
    return user
