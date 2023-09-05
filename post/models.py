from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    
    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images_2 = models.ImageField(upload_to='turs/', blank=True, null=True)
    destinations = models.ManyToManyField(Destination)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    traveler_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    booking_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking for {self.traveler_name} on {self.booking_date}"


