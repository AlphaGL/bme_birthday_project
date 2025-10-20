from django.db import models
from cloudinary.models import CloudinaryField

class Student(models.Model):
    LEVEL_CHOICES = [
        ('100', '100 Level'),
        ('200', '200 Level'),
        ('300', '300 Level'),
        ('400', '400 Level'),
        ('500', '500 Level'),
    ]
    
    MONTH_CHOICES = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Prefer not to say'),
    ]
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    birth_month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    birth_day = models.IntegerField()
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    alias = models.CharField(max_length=100, blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    held_office = models.BooleanField(default=False)
    office_position = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['birth_month', 'birth_day']
        verbose_name = 'Student Birthday'
        verbose_name_plural = 'Student Birthdays'
    
    def __str__(self):
        return f"{self.full_name} - {self.get_birth_month_display()} {self.birth_day}"
    
    @property
    def birthday_display(self):
        return f"{self.get_birth_month_display()} {self.birth_day}"