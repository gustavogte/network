from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# Add models for: post, likes, followers.... comments too (I think)
class Post(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%d %b %Y %H:%M:%S')}"


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_who_is_following"
    )
    user_follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_being_followed"
    )
    def __str__(self) -> str:
        return f"{ self.user } is following { self.user_follower }"