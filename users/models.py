""" Profile - BaseUser Model """
from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    """ Adding data to Base User model """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    enrollment = models.IntegerField(blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    carrer = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.user.get_full_name()