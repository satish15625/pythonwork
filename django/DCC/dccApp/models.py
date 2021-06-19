from django.db import models
# models.py 
class UploadImages(models.Model): 
	name = models.CharField(max_length=50) 
	image_Img = models.ImageField(upload_to='images/') 
