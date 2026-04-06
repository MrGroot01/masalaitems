from django.db import models

class  MasalItems(models.Model):
    CATEGORY_CHOICES = [
        ('oil', 'Oil'),
        ('masala', 'Masala'),
        ('desighee', 'DesiGhee'),
        ('saltsugar', 'SaltSugar'),
    ]

    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=90)
    price = models.IntegerField()
    description = models.TextField(max_length=90)
    images = models.ImageField(upload_to='pictures/', null=True, blank=True)
    rating = models.FloatField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  

    def __str__(self):
        return self.name