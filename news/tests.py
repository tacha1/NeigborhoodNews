from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Business,Neighborhood

class ProfileTestClass(TestCase):    
    # Setup method
    def setUp(self):
        self.user = User.objects.create(id = 1,username = 'Rosine')
        self.profile = Profile(location = 'remera',profile_picture = 'p1.jpeg', bio = 'cool', user = self.user)
 
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # testing the save method
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 1)
        
    def test_delete_method(self):
       self.profile.save_profile()
       self.profile.delete_profile()
       profile = Profile.objects.all()
       self.assertTrue(len(profile) >= 0)


class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1,username = 'Rosine')
        self.profile = Profile(location = 'remera',profile_picture = 'p1.jpeg', bio = 'cool', user = self.user)
        self.new_neighborhood = Neighborhood(id = 1,neighborhood_name = 'natacha')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_create_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_neighborhood(self):
        self.new_neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)

    def test_filter_neighborhood_by_id(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood = Neighborhood.filter_neighborhood_by_id(1)

    def test_update_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood = Neighborhood.filter_neighborhood_by_id(1)
        neighborhood.new_neighborhood = 'Another Neighborhood'

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(id = 1,username = 'Rosine')
        self.new_neighborhood = Neighborhood(id = 1,neighborhood_name = 'natacha')
        self.new_neighborhood.save()
        self.new_business = Business(id = 1,business_name='Business',user=self.new_user,location='Location',email='business@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_create_business(self):
        self.new_business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.new_business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_filter_business_by_id(self):
        self.new_business.create_business()
        business = Business.filter_business_by_id(1)

    def test_update_business(self):
        self.new_business.create_business()
        business = Business.filter_business_by_id(1)
        business.update_business('Another Business')
    
    