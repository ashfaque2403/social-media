from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Post(models.Model):
    body=models.TextField()
    image=models.ImageField(upload_to='uploads/post_photos',blank=True)
    created_on=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,blank=True,related_name='likes')
    dislikes=models.ManyToManyField(User,blank=True,related_name='dislikes')

class Comment(models.Model):
    comment=models.TextField()
    created_on=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

class UserProfile(models.Model):
    user=models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE,primary_key=True,related_name='profile',)
    name=models.CharField(max_length=30,blank=True,null=True)
    bio=models.TextField(max_length=500,blank=True,null=True)
    date_birth=models.DateField(null=True,blank=True)
    picture=models.ImageField(upload_to='uploads/profile_pictures',default='uploads/profile_picture/default.jpg',blank=True)
    followers=models.ManyToManyField(User,blank=True,related_name='followers')
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

class Notification(models.Model):
    notification_type=models.IntegerField()
    to_user=models.ForeignKey(User,related_name='notification_to', on_delete=models.CASCADE,null=True) 
    from_user=models.ForeignKey(User,related_name='notification_from', on_delete=models.CASCADE,null=True) 
    post=models.ForeignKey(Post,related_name='+',blank=True,null=True, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,related_name='+',blank=True,null=True, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    user_has_seen=models.BooleanField(default=False)