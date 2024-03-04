from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):    

    year_choice = []
    for r in range(1980, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)     
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    generation = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    color = models.CharField(max_length=100)
    modification_engine = models.CharField(max_length=100)
    powertrain_architecture = models.CharField(max_length=100)
    body_style = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)
    doors = models.CharField(choices=door_choices, max_length=10)
    wheelbase = models.CharField(max_length=50)
    height= models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    # dimensions = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    tank_capacity= models.CharField(max_length=50)
    fuel_system= models.CharField(max_length=50,  blank=True, null=True)
    acceleration = models.CharField(max_length=50,  blank=True, null=True)
    engine = models.CharField(max_length=100,  blank=True, null=True)
    engine_displacement = models.CharField(max_length=50, blank=True, null=True)
    engine_code = models.CharField(max_length=50, blank=True, null=True)
    engine_location= models.CharField(max_length=50, blank=True, null=True)
    engine_oil_capacity= models.CharField(max_length=50, blank=True, null=True)
    engine_aspiration= models.CharField(max_length=50, blank=True, null=True)
    torque = models.CharField(max_length=50, blank=True, null=True)
    power_per_litre = models.CharField(max_length=50, blank=True, null=True)
    power = models.CharField(max_length=50, blank=True, null=True)
    Weight_to_torque_ratio = models.CharField(max_length=50, blank=True, null=True)
    Weight_to_power_ratio = models.CharField(max_length=50, blank=True, null=True)
    tire_size = models.CharField(max_length=50, blank=True, null=True)
    power_steering = models.CharField(max_length=50, blank=True, null=True)
    steering_type = models.CharField(max_length=50, blank=True, null=True)
    assisting_systems = models.CharField(max_length=50, blank=True, null=True)
    rear_brakes = models.CharField(max_length=50, blank=True, null=True)
    front_brakes = models.CharField(max_length=50, blank=True, null=True)
    rear_suspension = models.CharField(max_length=50, blank=True, null=True)
    front_suspension= models.CharField(max_length=50,blank=True, null=True)
    gears = models.CharField(max_length=50, blank=True, null=True)
    drive_wheel= models.CharField(max_length=50, blank=True, null=True)   
    price = models.CharField(max_length=50, blank=True, null=True)   

    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = RichTextField()
    features = MultiSelectField(choices=features_choices)       
    transmission = models.CharField(max_length=100)     
    passengers = models.IntegerField()    
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
