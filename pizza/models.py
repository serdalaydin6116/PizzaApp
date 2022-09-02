from turtle import title
from django.db import models

# Create your models here.
TOPPINGS=[

        ('Pesto' , 'Pesto'),
        ('Tomatoes' , 'Tomatoes'),
        ('Cheese' , 'Cheese'),
        ('Pepperoni' , 'Pepperoni'),
        ('Olive' , 'Olive'),

]

PROPORTIONS=(
        ( 'Family_Size', '1'),
        ('Hungry_Size', '2'),
        ('Big_Size', '3'),
        ('Middle_Size', '4'),
        ('Small_Size', '5'),

)
class Size(models.Model):
    title = models.CharField(max_length=20, choices=PROPORTIONS)
    

    class Meta:
        verbose_name_plural='Sizes'

    def __str__(self):
        return f"{self.title} "

class Pizza(models.Model):
    topping1=models.CharField(max_length=50, choices=TOPPINGS)
    topping2=models.CharField(max_length=50, choices=TOPPINGS)
    piece=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)

    size= models.ForeignKey(Size, default=1, verbose_name="Size", on_delete=models.CASCADE)
    # size= models.OneToOneField(Size, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.size} topped with  {self.topping1} and {self.topping2} "
