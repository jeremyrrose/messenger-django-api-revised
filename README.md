# Messenger API

Forked from [Magdalena K's Cloud Message API](https://github.com/studiosemantica/p4backend/) for collaborative use.

## Description
### Cloud Message

A simple messaging app to help connect you with other Cloud Message users. 
        
User story:  
- Quinn is a musician that wants to connect with other artists.
- He can register an account with the Cloud Message app to have his login info saved.
- In order to access his inbox, he will input his registered account information into the login form on the landing page.
- Upon logging in, he will see the main inbox, with a list of messages received from senders and a preview of the messages last received or sent from that user.
- To access a conversation, the user can click on the individual conversation in the list and a new view with the conversation between the users will appear.
- A popup text field in the conversation view will either create or update the message from the user upon submission depending on the models used.
- A upper navbar giving the option to select profile settings or to log out of the account.
- A user settings modal that allows user to change their avatar or delete their account.

## Models
```python
User:
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
UserProfile:
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    avatar = models.CharField(max_length=800)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
Message:
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False
```

## Endpoints
/cloud_msg/UserProfiles : Standard viewset endpoints
/cloud_msg/messages : Standard viewset endpoints
/cloud_msg/user_search/<str:search_string> : GET returns UserProfiles whose `user.username` partially matches `search_string`