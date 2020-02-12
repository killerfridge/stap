from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    stp = models.ForeignKey('STP', on_delete=models.CASCADE, verbose_name='STP')
    nhs_code = models.CharField(max_length=6, verbose_name='NHS Code')
    street_address_1 = models.CharField(max_length=40, blank=True)
    street_address_2 = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=20, blank=True)
    county = models.CharField(max_length=20, blank=True)
    postcode = models.CharField(max_length=10, blank=True)

    website = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('main:site_detail', args=[self.pk])


class STP(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'STP/Health Board'
        verbose_name_plural = 'STPs/Health Boards'

    def get_absolute_url(self):
        return reverse('main:stp_detail', args=[self.pk])


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return f'{self.year}'

    class Meta:
        ordering = ['year']


class Beds(models.Model):
    general = models.IntegerField()
    critical = models.IntegerField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Beds'
        ordering = ['-year']

    def __str__(self):
        return f'{self.site} Beds: {self.year}'


class Income(models.Model):
    income = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Income Statements'
        ordering = ['-year']

    def __str__(self):
        return f'{self.site} Income: {self.year}'


# TODO CQC model
