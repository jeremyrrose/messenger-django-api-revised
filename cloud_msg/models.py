from django.db import models
from authentication.models import User


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'UserProfiles'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    avatar = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str("Avatar is :  " + str(self.avatar) + "   " +
                   "Username is :  " + str(self.username) + "   " +
                   str(self.last_update_at))


# Create your models here.
class Message(models.Model):
    class Meta:
        verbose_name_plural = 'messages'
        ordering = ('timestamp',)

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str("Sender:  " + str(self.sender) + "   " +
                   "Receiver:  " + str(self.receiver) + "   " +
                   '"' + str(self.message) + '"' +
                   "   " + str(self.last_update_at))
