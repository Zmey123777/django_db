from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=100)  # Имя телефона
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена телефона
    image = models.URLField(max_length=200)
    release_date = models.DateField()  # Дата выхода телефона
    lte_exists = models.BooleanField(default=False)  # Наличие LTE
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Слаг, генерируется из поля name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Слагифицируем значение name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
