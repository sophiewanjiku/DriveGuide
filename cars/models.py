from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    # state_choice = (
    #     ('AL', 'Alabama'),
    #     ('AK', 'Alaska'),
    #     ('AZ', 'Arizona'),
    #     ('AR', 'Arkansas'),
    #     ('CA', 'California'),
    #     ('CO', 'Colorado'),
    #     ('CT', 'Connecticut'),
    #     ('DE', 'Delaware'),
    #     ('DC', 'District Of Columbia'),
    #     ('FL', 'Florida'),
    #     ('GA', 'Georgia'),
    #     ('HI', 'Hawaii'),
    #     ('ID', 'Idaho'),
    #     ('IL', 'Illinois'),
    #     ('IN', 'Indiana'),
    #     ('IA', 'Iowa'),
    #     ('KS', 'Kansas'),
    #     ('KY', 'Kentucky'),
    #     ('LA', 'Louisiana'),
    #     ('ME', 'Maine'),
    #     ('MD', 'Maryland'),
    #     ('MA', 'Massachusetts'),
    #     ('MI', 'Michigan'),
    #     ('MN', 'Minnesota'),
    #     ('MS', 'Mississippi'),
    #     ('MO', 'Missouri'),
    #     ('MT', 'Montana'),
    #     ('NE', 'Nebraska'),
    #     ('NV', 'Nevada'),
    #     ('NH', 'New Hampshire'),
    #     ('NJ', 'New Jersey'),
    #     ('NM', 'New Mexico'),
    #     ('NY', 'New York'),
    #     ('NC', 'North Carolina'),
    #     ('ND', 'North Dakota'),
    #     ('OH', 'Ohio'),
    #     ('OK', 'Oklahoma'),
    #     ('OR', 'Oregon'),
    #     ('PA', 'Pennsylvania'),
    #     ('RI', 'Rhode Island'),
    #     ('SC', 'South Carolina'),
    #     ('SD', 'South Dakota'),
    #     ('TN', 'Tennessee'),
    #     ('TX', 'Texas'),
    #     ('UT', 'Utah'),
    #     ('VT', 'Vermont'),
    #     ('VA', 'Virginia'),
    #     ('WA', 'Washington'),
    #     ('WV', 'West Virginia'),
    #     ('WI', 'Wisconsin'),
    #     ('WY', 'Wyoming'),
    # )

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
    # state = models.CharField(choices=state_choice, max_length=100)
    # city = models.CharField(max_length=100)    
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    generation = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    color = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    # tire_size
    # power_steering
    # steering_type
    # assisting_systems
    # rear_brakes
    # front_brakes
    # rear_suspension
    # front_suspension
    # gears
    # drive_wheel
    # drivetrain_architecture
    # minimum_turning_circle
    # rear_overhang
    # front_overhang
    # rear_track
    # front_track
    # wheelbase
    # height
    # width
    # length
    # dimensions
    # tank_capacity
    # trunk_space
    # kerb_weight
    # coolant
    # engine_oil_capacity
    # engine_aspiration
    # fuel_system
    # compression_ratio
    # piston_stroke
    # cylinder_bore
    # cylinder_position
    # number_of_cylinders
    # engine_displacement
    # engine_code
    # engine_location
    # torque
    # power_per_litre
    # power
    # Weight_to_torque_ratio
    # Weight_to_power_ratio
    # Emission_standard
    # minimum_speed
    # acceleration
    # cO2_emissions



























































    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
