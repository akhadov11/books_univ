from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount


class Country(models.Model):
    """ a model representing Country entity """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """ a model representing City entity """
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    """ a model representing Author entity """
    name = models.CharField(max_length=255)
    num_of_books = models.SmallIntegerField(blank=True, null=True)
    bio = models.TextField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_books_count(self):
        return f"{self.book_set.all().count()}"

    get_books_count.short_description = "Books count"


class Genre(models.Model):
    """ a model representing Genre entity """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])


class Book(models.Model):
    """ a model representing Book entity """
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')
    price = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    image = models.FileField(blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-pub_date", ]
