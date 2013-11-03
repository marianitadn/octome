from django.db import models

from octo_cv.constants import ContactType


class Contact(models.Model):
    """Describe a contact information resource, like a social profile.
    Example:
        Twitter Contact:
            - name - Twitter
            - link - link to Twitter profile
            - image - Twitter logo
            - description - account description
    """

    contact_types = (
        ('Address', ContactType.ADDRESS),
        ('Email', ContactType.EMAIL),
        ('Phone', ContactType.PHONE),
        ('Social', ContactType.SOCIAL),
    )

    type = models.CharField(max_length=20, choices=contact_types)
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(null=True)
    image = models.ImageField(null=True)
    email = models.EmailField(null=True)
