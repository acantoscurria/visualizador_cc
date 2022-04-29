from email.policy import default
from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for visualizador_cc.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    supervisor = BooleanField(default=False, help_text="Marque si es supervisor", verbose_name='¿Es supervisor?')
    name = CharField(_("Name of User"), blank=True, max_length=255)
    
    regiones_edu = [
        ('', 'No es supervisor'),
        ('Regional 1', 'R.E. 1'),
        ('Sub-Regional 1A', 'SUB. R.E. 1-A'),
        ('Regional 2', 'R.E. 2'),
        ('Sub-Regional 2', 'SUB. R.E. 2'),
        ('Regional 3', 'R.E. 3'),
        ('Sub-Regional 3', 'SUB. R.E. 3'),
        ('Regional 4A', 'R.E. 4-A'),
        ('Regional 4B', 'R.E. 4-B'),
        ('Regional 5', 'R.E. 5'),
        ('Sub-Regional 5', 'SUB. R.E. 5'),
        ('Regional 6', 'R.E. 6'),
        ('Regional 7', 'R.E. 7'),
        ('Regional 8A', 'R.E. 8-A'),
        ('Regional 8B', 'R.E. 8-B'),
        ('Regional 9', 'R.E. 9'),
        ('Regional 10A', 'R.E. 10-A'),
        ('Regional 10B', 'R.E. 10-B'),
        ('Regional 10C', 'R.E. 10-C'),
        ('Sub-Regional 1B', 'SUB. R.E. 1-B'),
        ]
    region = CharField(max_length=20, choices=regiones_edu, verbose_name='Regional Educativa', help_text='Seleccione la regional del supervisor', default=None, null=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    def __str__(self):
        return self.email