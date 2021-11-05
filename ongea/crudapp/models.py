from django.db import models

# Create your models here.

class messg(models.Model):
    message = models.CharField(max_length=300)
    

    def save_message(self):
        self.message

    def delete_message(self):
        self.delete
    







    
    

    