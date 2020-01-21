from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=60, verbose_name='Name')

    def __str__(self):
        return self.name


class Jobs(models.Model):
    name = models.CharField(max_length=60, verbose_name='Name')
    descripion = models.TextField(
        verbose_name='Description', null=True, blank=True)
    status = models.BooleanField(verbose_name='Status', default=True)
    salary = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Salary')
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60, verbose_name='Name')
    email = models.EmailField(max_length=70, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Telephone')
    status = models.BooleanField(verbose_name='Status', default=True)
    bio = models.TextField(max_length=500, verbose_name='Bio')
    created_at = models.DateTimeField(auto_now_add=True)
    jobs = models.ManyToManyField(Jobs)

    def __str__(self):
        return self.name
