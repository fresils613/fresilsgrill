from django.db import models
from phone_field import PhoneField

# Create your models here.
from django.contrib.auth.models import User 

class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits = 7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("Order Sent", "Order Sent"),
)

LOCATIONS = (
    ("Abule Egba", 500),
    ("Abule Egba - ekoro", 700),
    ("Acme", 500),
    ("Adeniyi jones", 500),
    ("Admiralty rd lekki phase 1", 1500),
    ("Agboyi ketu", 700),
    ("Agege abattior", 500),
    ("Agidingbi", 500),
    ("Ajao estate", 1000),
    ("Akilo ogba", 500),
    ("Akoka UNILAG", 1000),
    ("Akoka", 1000),
    ("Akowonjo", 700),
    ("Alapere", 700),
    ("Alimosho", 600),
    ("Anthony village", 700),
    ("Anthony mende", 700),
    ("Anthony – ajao estate", 700),
    ("Ayobo rd", 700),
    ("Banana island", 1200),
    ("Bariga", 1000),
    ("CMD rd", 700),
    ("Command – Ipaja", 700),
    ("Dolphin estate", 1000),
    ("Dopemu", 700),
    ("E-centre –Yaba ", 700),
    ("Egbeda", 700),
    ("Ejigbo", 800),
    ("Eko Atlantic City", 1200),
    ("Eleko", 1200),
    ("Eleko beach", 1200),
    ("Fadeyi", 700),
    ("Festac Town", 1000),
    ("Garage Ojota", 700),
    ("Gbagada General Hosptial ", 800),
    ("Gbagada Ifako", 800),
    ("Gbagada Phase 1 &2", 800),
    ("Gbagada Soluyi ", 800),
    ("Gbagada UPS", 800),
    ("Gowon Estate", 800),
    ("Idimu", 800),
    ("Ifako Agege", 500),
    ("Igando", 1000),
    ("Ijesha Tedo", 800),
    ("Iju Train Station ", 600),
    ("Ikeja –Alausa", 500),
    ("Ikeja GRA", 500),
    ("Ikeja Opebi", 500),
    ("Ikeja Oba Akran", 500),
    ("Ikeja Allen Avenue",500),
    ("Ikeja Maryland ",500),
    ("Ikosi Ketu", 700),
    ("Ikotun", 700),
    ("Ikoyi Awolowo", 1200),
    ("Ikoyi Bourdillon", 1200),
    ("Ikoyi Alfred Rewane", 1200),
    ("Ikoyi Glover", 1200),
    ("Ikoyi Osborne", 1200),
    ("Ikoyi Prisons ", 1200),
    ("Ilasamaja", 800),
    ("Ilupeju Bye pass", 800),
    ("Ipaja road", 700),
    ("Ire Akari", 800),
    ("Isheri –Idimu", 700),
    ("Isolo", 700),
    ("Jakande – Isheri ", 700),
    ("Jakande – Isolo",700),
    ("Ketu",700),
    ("Kosofe", 700),
    ("Ladi Laki – Somolu", 700),
    ("Lagos Island", 1000),
    ("Lekki Phase 1", 1500),
    ("Ligali Ayorinde ", 1200),
    ("Mafoluku", 700),
    ("Magodo Phase 1", 700),
    ("Magodo Phase 2", 700),
    ("Marina", 1000),
    ("Marina Express", 1000),
    ("Mile 12", 800),
    ("Mushin ", 800),
    ("National Theatre", 1000),
    ("New Garage Gbagada", 800),
    ("Obalende", 1000),
    ("Obanikoro", 700),
    ("Obanikoro Pedro", 700),
    ("Obawole", 500),
    ("Ogba", 500),
    ("Ogudu", 700),
    ("Ojodu", 500),
    ("Oke Afa", 700),
    ("Oke odo ", 600),
    ("Oko Oba", 500),
    ("Okota", 800),
    ("Olowora", 500),
    ("Omole Phase 1", 500),
    ("Omole Phase 2", 700),
    ("Onigbongbo", 600),
    ("Onike", 800),
    ("Onipanu", 700),
    ("Oniru", 1200),
    ("Oregun", 500),
    ("Orile – Coker", 1000),
    ("Orile –Iganmu", 1000),
    ("Orile Agege", 500),
    ("Oshodi", 800),
    ("Papa AJao", 800),
    ("Shasha", 700),
    ("Shogunle – Ikeja", 700),
    ("Sungas – Shomolu", 700),
    ("Surulere – Aguda", 800),
    ("Surulere – Bode Thomas ", 800),
    ("Surulere – Idi Araba",800),
    ("Surulere – Ojuelegba",800),
    ("Surulere – Stadium ", 800),
    ("Surulere – Adelabu", 800),
    ("Surulere – Animashaun", 800),
    ("Surulere – Barracks", 800),
    ("Surulere – Idi oro", 800),
    ("Town Planning", 800),
    ("VI – Ahmadu Bello", 1200),
    ("Victoria Island", 1200),
    ("Yaba – Abule Ijesha", 800),
    ("Yaba – Alagomeji", 800),
    ("Yaba – Makoko", 800),
    ("Yaba – Market ", 700),
    ("Yaba – Oyingbo", 700),
    ("Yaba – Tejuosho", 700),
    ("Yaba – Fola Agoro", 800),
    ("Yaba – Adekunle ", 800),
    ("Yaba – Bajulaye rd", 800),
    ("Yaba – Ebutte Meta", 800),
    ("Yaba – Empire", 800),
    ("Yaba – Iddo ", 800),
    ("Yaba – Iwaya",800),
    ("Yaba – Jibowu", 800),
    ("Yaba – Sabo ", 800),
    ("Yaba – Tech", 700),
    ("Yaba – Total", 700),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField(null=True)
    order_status = models.CharField(max_length = 100, choices = ORDER_STATUS, default="Order Processing")

    def __str__(self):
        return str(self.transaction_id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def total_order(self):
        order = self.Order.all()
        total = sum([item for item in order])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.order.transaction_id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

PAYMENT_METHOD = (
    ("Pay On Delivery", "Pay On Delivery"),
    ("Card Payment", "Card Payment"),
)
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    full_address = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    date_added= models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100,null=True)
    Payment_method = models.CharField(max_length = 100,null=True)
    

    def __str__(self):
        return self.address



    



