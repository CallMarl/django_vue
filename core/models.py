from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Account(AbstractUser) :

    is_active   = models.BooleanField(default = False)

    def __str__(self) :
        return \
            "Account : "    + str(self.pk) + "\n" \
            "\tuser\t: "    + str(self.username) + "\n" \
            "\temail\t: "   + str(self.email) + "\n" \
            "\tactive\t: "  + str(self.is_active) + "\n"
