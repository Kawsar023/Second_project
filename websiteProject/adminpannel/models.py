from distutils.command import upload
from django.db import models

class aboutus(models.Model):
    about_pic             = models.ImageField(upload_to='about/', blank= True, null= True)
    about_title           = models.CharField(max_length=200, default= False)
    about_description_1   = models.TextField(blank= True, null= True)
    about_description_2   = models.TextField(blank= True, null= True)
    # status = models.BooleanField(default= False)
    is_active = models.BooleanField(default= False)


class designations(models.Model):
    designations_title = models.CharField(max_length=255)


# class speakers (models.Model):
#     speakers_pic             = models.ImageField(upload_to='speaker/', blank= True, null= True)
#     speakers_name            = models.CharField(max_length=255)
#     desi            = models.ForeignKey('designations', on_delete=models.CASCADE)
#     description              = models.CharField(max_length=500, blank=True, null=True)
#     email                    = models.EmailField(unique= True)
#     mobile                   = models.CharField(max_length=12)
#     facebook                 = models.CharField(max_length=255, blank=True, null=True)
#     twitter                 = models.CharField(max_length=255, blank=True, null=True)
#     linkedin               = models.CharField(max_length=255, blank=True, null=True)
#     pinterest              = models.CharField(max_length=255, blank=True, null=True)
#     is_active               = models.BooleanField(default= False)
#     approved               = models.BooleanField(default= False)
    

class speakers(models.Model):
    speaker_pic             = models.ImageField(upload_to='speaker/', blank= True, null= True)
    speaker_name            = models.CharField(max_length=200, default= False)
    speaker_description_1   = models.TextField(blank= True, null= True)
    designations             = models.ForeignKey('designations', on_delete=models.CASCADE)
    facebook                 = models.CharField(max_length=255, blank=True, null=True)
    twitter                 = models.CharField(max_length=255, blank=True, null=True)
    linkedin               = models.CharField(max_length=255, blank=True, null=True)
    pinterest              = models.CharField(max_length=255, blank=True, null=True)
    # status = models.BooleanField(default= False)
    is_active = models.BooleanField(default= False)
    
