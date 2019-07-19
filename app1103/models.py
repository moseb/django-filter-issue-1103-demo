from django.db.models import Model, ManyToManyField


class Product(Model):
    def __str__(self):
        return f'Product with tags {self.tags}'


class ProductTag(Model):
    products = ManyToManyField(
        'Product',
        related_name='tags'
    )
