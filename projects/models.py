from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile/' ,blank=True, default='media/profile/male.png')
    bio=models.TextField(blank=True,default='*No Bio*')
    phone_no=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username 
    @classmethod
    def get_profile(cls,username):
        userd=cls.objects.get(user=username)
        return userd
        
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
