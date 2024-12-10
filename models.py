from django.db import models

class Appointment(models.Model):
    agree_terms = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=128)  
    birthdate = models.DateField()
    appointment = models.DateTimeField()
    time = models.TimeField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    HOBBIES_CHOICES = [('reading', 'Reading'),
        ('sports', 'Sports'),
    ]
    hobbies = models.CharField(max_length=100, choices=HOBBIES_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file_upload = models.FileField(upload_to='uploads/')
    website = models.URLField(blank=True, null=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.name
