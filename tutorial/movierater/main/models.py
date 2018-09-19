from django.db import models


class ExtraInfo(models.Model):
    GATUNKI ={
        (0, 'Nieznany'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-Fi'),
        (4, 'Dramat'),

    }
    czas_trwania = models.IntegerField(default=0)
    gatunek = models.IntegerField(default=0, choices=GATUNKI)


class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
    photo = models.ImageField(null=True, blank=True, upload_to='plakaty')
    info = models.OneToOneField(ExtraInfo,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + " (" + str(self.year) + ")"


class Review(models.Model):
    text = models.CharField(default='',
                            blank=True,
                            null=True,
                            max_length=120)

    stars = models.IntegerField(default=5)

    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    filmy = models.ManyToManyField(Movie)



