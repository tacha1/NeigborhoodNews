from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = models.CharField(max_length =300)
    location = models.CharField(max_length =30)  

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def __str__(self):
        return str(self.user)


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    occupants = models.IntegerField(default = 0, null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def update_neighborhood(cls,id,value):
        cls.objects.filter(id = id).update(neighborhood_name = new_hood)

    @classmethod
    def filter_neighborhood_by_id(cls,id):
        neigborhood = cls.objects.filter(id = id)
        return neigborhood

    @classmethod
    def update_occupants(cls,id,value):
        cls.objects.filter(id = id).update(occupants = new_occupant)

    def __str__(self):
        return self.neighborhood_name

class Business(models.Model):
    business_name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    email = models.EmailField(null= True, unique= True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def update_business(cls,id,value):
        cls.objects.filter(id = id).update(business_name = new_business)

    @classmethod
    def filter_business_by_id(cls,id):
        neigborhood = cls.objects.filter(id = id)
        return neigborhood

    @classmethod
    def search_by_business_name(cls,search_term):
        busineses = cls.objects.filter(business_name__icontains = search_term)
        return busineses

    def __str__(self):
        return self.business_name

class Post(models.Model):
    name = models.CharField(max_length = 250)
    # picture = models.ImageField(upload_to = 'photos/', null=True)
    description = models.CharField(max_length = 300)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def get_all_posts(cls):
        post = cls.objects.all()
        return post

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def filter_post_by_id(cls,id):
        post = cls.objects.filter(id = id)
        return post
        
    def __str__(self):
        return self.name