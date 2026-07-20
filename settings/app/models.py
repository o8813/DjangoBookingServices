from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'Country name: {self.name}'

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'City: {self.name}\nCountry: {self.country.name}'

class Hotel(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    owner = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.city}'

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    room_number = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField(default=5000)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.room_number} - {self.quantity}'