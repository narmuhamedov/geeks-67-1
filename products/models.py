from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#MANY TO MANY
class CategoryCar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='укажите название машины')
    person = models.CharField(max_length=50, null=True, verbose_name='укажите фио покупателя')
    categories = models.ManyToManyField(CategoryCar, null=True)

    def __str__(self):
        return f'{self.title} - {', '.join(i.name for i in self.categories.all())}'

    class Meta:
        verbose_name = 'машину'
        verbose_name_plural = 'машины'

    
# ONE TO ONE
class StateNumberCar(models.Model):
    car_title = models.OneToOneField(Car, on_delete=models.CASCADE)
    number_car = models.CharField(max_length=100, default='0_KG_____')

    def __str__(self):
        return f'{self.number_car} - {self.car_title}'

#ONE TO MANY
class CommentCar(models.Model):
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=5, 
                                       validators=[MinValueValidator(1), 
                                                   MaxValueValidator(5)])
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car} - {self.mark}'