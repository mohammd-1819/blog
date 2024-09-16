from django.db import models


class ContactUsMessage(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.CharField(max_length=70)
    text = models.TextField()

    def __str__(self):
        return self.subject
