from django.contrib import admin
from .models import (
    Site,
    STP,
    Beds,
    Income,
    Year,
    SubSite,
)
# Register your models here.


class BedInline(admin.TabularInline):
    model = Beds
    extra = 0


class IncomeInline(admin.TabularInline):
    model = Income
    extra = 0


class SiteInline(admin.TabularInline):
    model = Site
    extra = 0
    fields = ['name', 'nhs_code', 'postcode']


class SubSiteInline(admin.TabularInline):
    model = SubSite
    extra = 0
    fields = ['name', 'nhs_code', 'postcode']


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    inlines = [BedInline, IncomeInline, SubSiteInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'nhs_code', 'stp', 'website')
        }),
        ('Address', {
            'fields': ('street_address_1', 'street_address_2', 'city', 'county', 'postcode')
        })
    )


@admin.register(SubSite)
class SubSiteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'main_location', 'nhs_code', 'site', 'website')
        }),
        ('Address', {
            'fields': ('street_address_1', 'street_address_2', 'city', 'county', 'postcode')
        })
    )


@admin.register(STP)
class STPAdmin(admin.ModelAdmin):
    inlines = [SiteInline]


@admin.register(Beds)
class BedsAdmin(admin.ModelAdmin):
    pass


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    pass


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    pass
