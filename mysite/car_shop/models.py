from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField


STATUS_CHOICES = (
    ('owner', 'owner'),
    ('client', 'client')
)
class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)], null=True, blank=True)
    phone_number = PhoneNumberField()
    picture = models.ImageField(upload_to='profile_image', null=True, blank=True)


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Owner(UserProfile):
    BUSINESS_CHOICES = (
        ('базовый', 'базовый'),
        ('стандарт', 'стандарт'),
        ('продвинутый', 'продвинутый')
    )
    business_account = models.CharField(choices=BUSINESS_CHOICES, max_length=32, default='базовый')
    status_owner = models.CharField(choices=STATUS_CHOICES, max_length=24, default='owner')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name_plural = 'owners'

class Contact(models.Model):
    user = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='contact')
    title = models.CharField(max_length=32)
    contact_number = PhoneNumberField()
    social_network = models.URLField(null=True, blank=True)


    def __str__(self):
        return f'{self.user}'


class Client(UserProfile):
    status = models.CharField(choices=STATUS_CHOICES, max_length=24, default='client')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        verbose_name_plural = 'clients'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class CarMake(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    carmake_name = models.CharField(max_length=32, unique=True)
    carmake_image = models.ImageField(upload_to='car_make_images')

    def __str__(self):
        return self.carmake_name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    carmodel_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.car_make}, {self.carmodel_name}'


class Generation (models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    caremodel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    generation = models.CharField(max_length=32)


    def __str__(self):
        return f'{self.carmake}, {self.caremodel}, {self.generation}'


class Car(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='carmake')
    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    year = models.DateField()
    CAR_BODY_TYPE_CHOICES = (
        ('седан', 'седан'),
        ('универсад', 'универсал'),
        ('внедорожник', 'внедорожник'),
        ('пикап', 'пикап'),
        ('хетчбек', 'хетчбек'),
        ('крассовер', 'крассовер')
    )
    car_body = models.CharField(choices=CAR_BODY_TYPE_CHOICES, max_length=36, default='седан')
    ENGINE_CHOICES = (
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
        ('гибрид', 'гибрид'),
        ('электр', 'электр')
    )
    engine = models.CharField(choices=ENGINE_CHOICES, max_length=12, default='бензин')
    DRIVE_CHOICES = (
        ('полный', 'полный'),
        ('задний', 'задний'),
        ('передний', 'передний')
    )
    drive = models.CharField(choices=DRIVE_CHOICES, max_length=32, default='полный')
    TRANSMISSION_CHOICES = (
        ('автамат', 'автамат'),
        ('механика', 'механика')
    )
    transmission = models.CharField(max_length=24, choices=TRANSMISSION_CHOICES, default='механика')
    MODIFICATION_CHOICES = (
        ('1.8', '1.8'),
        ('2.0', '2.0'),
        ('2.4', '2.4'),
        ('2.5', '2.5'),
        ('3.0', '3.0'),
        ('3.4', '3.4'),
    )
    modification = models.CharField(max_length=24, choices=MODIFICATION_CHOICES, default='1.8')
    RULE_CHOICES = (
        ('рул слева', 'рул слева'),
        ('рул справа', 'рул справа')
    )
    rule = models.CharField(choices=RULE_CHOICES, max_length=16, default='слева')
    video = models.URLField(null=True, blank=True)
    address_country = models.CharField(max_length=64)
    address_city = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    color = models.FileField()
    STATE_CHOICES = (
        (' хорошее', ' хорошее'),
        (' идеальное', ' идеальное'),
        (' аварийное / не на ходу', ' аварийное / не на ходу'),
        (' новое', ' новое')
    )
    state = MultiSelectField(choices=STATE_CHOICES, max_length=64, max_choices=4)
    mileage = models.CharField(max_length=62)
    description = models.TextField()
    APPEARANCE_CHOICE = (
        ('обвес', 'обвес'),
        ('багажник', 'багажник'),
        ('панорамная крыша', 'панорамная крыша'),
        ('тонировка', 'тонировка'),
        ('спойлер', 'спойлер'),
    )
    appearance = MultiSelectField(choices=APPEARANCE_CHOICE, max_length=72, max_choices=6)
    SALON_CHOICES = (
        ('комбинированный', 'комбинированный'),
        ('велюр', 'велюр'),
        ('шторки', 'шторки'),
        ('кожа', 'кожа')
    )
    salon = MultiSelectField(choices=SALON_CHOICES, max_length=72, max_choices=4)
    SECURITY_CHOICES = (
        ('подушки безопасности', 'подушки безопасности'),
        ('антипробуксовочная система', 'антипробуксовочная система'),
        ('камера 360', 'камера 360')
    )
    security = MultiSelectField(choices=SECURITY_CHOICES, max_length=72, max_choices=3)
    STOCK_CHOICES = (
        ('в наличие', 'в наличие'),
        ('на заказ', 'на заказ'),
        ('в пути', 'в пути'),
    )
    stock_kyrgyzstan = models.CharField(choices=STOCK_CHOICES, max_length=24, default='в наличие')
    CUSTOMS_CHOICES = (
        ('растаможен', 'растаможен'),
        ('не растаможен', 'не растаможен')
    )
    customs_kyrgyzstan = models.CharField(choices=CUSTOMS_CHOICES, max_length=64, default='растаможен')
    REGISTER_COUNTRY = (
        ('Кыргызстан', 'Кыргызстан'),
        ('не стоит в учете', 'не стоит в учуте')
    )
    register_country = models.CharField(choices=REGISTER_COUNTRY, max_length=34, verbose_name='страна регистрации')
    price = models.PositiveSmallIntegerField(default=1)
    CHANGE_CHOICES = (
        ('обмен не предлагать', 'обмен не предлагать'),
        ('рассмотрю варианты', 'рассмотрю варианты'),
        ('обмен на недвижимость', 'обмен на недвижимость')
    )
    change = MultiSelectField(choices=CHANGE_CHOICES, max_length=82, max_choices=3)
    rassrochka = models.BooleanField(default=False)
    OTHER_CHOICES = (
        ('свежепригнан', 'свежепригнан'),
        ('налог уплачен', 'налог уплачен'),
        ('техосмотр пройден', 'техосмотр пройден'),
        ('вложений не требует', 'вложений не требует'),
    )
    other = models.CharField(choices=OTHER_CHOICES, max_length=80, default='техосмотр пройден')

    def __str__(self):
        return f'{self.carmake}, {self.carmodel}, {self.generation}'


class CarImage(models.Model):
    car_image = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='cars_image')


class StateNumber(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    body_number = models.CharField(max_length=64)
    tex_passport_picture = models.ImageField(upload_to='tex_passport_picture', null=True, blank=True)
    car_number = models.CharField(max_length=64)


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rating')
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user}, {self.text}'