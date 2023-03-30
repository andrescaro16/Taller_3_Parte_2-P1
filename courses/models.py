from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='courses/images/')
    url = models.URLField(blank=True)
    start_date = models.DateField()

    def __str__(self):
        return self.title