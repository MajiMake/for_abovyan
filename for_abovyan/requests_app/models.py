from django.db import models


class User(models.Model):

    id: str
    email: str = models.CharField(max_length=20, unique=True)
    name: str = models.CharField(max_length=20)
    text: str = models.TextField()

    def __str__(self):

        """
        representing in admin
        """

        return self.email




