from django.db import models


class Person(models.Model):

    SEX_OPTIONS = (
        ('m', ('Masculino')),  # m = Male
        ('f', ('Femenino')),  # f = Female
    )

    TYPE_DOCUMENT_OPTIONS = (
        (1, ('DNI')),
        (2, ('Carnet de Extranjeria')),
        (3, ('Pasaporte'))
    )

    type_document = models.PositiveIntegerField(choices=TYPE_DOCUMENT_OPTIONS)
    document_number = models.CharField(max_length=45)
    birthdate = models.DateField(null=True)
    phone = models.CharField(max_length=25, blank=True)
    father_last_name = models.CharField(max_length=150)
    mother_last_name = models.CharField(max_length=150)
    email_score = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=255, blank=True)
    entry_date = models.DateField(null=True)
    termination_date = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS, blank=True)
