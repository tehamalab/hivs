from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from django.contrib.gis import geos
from mptt.models import MPTTModel, TreeForeignKey


class AbstractArea(MPTTModel, models.Model):
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        on_delete=models.CASCADE,
        verbose_name=_('parent')
    )
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    code = models.CharField(_('code'), max_length=50, blank=True)
    location_description_auto = models.CharField(
        _('location description'),
        help_text=_('can be generated automatically'),
        max_length=255,
        blank=True
    )
    population = models.PositiveIntegerField(
        _('population'),
        blank=True,
        null=True
    )
    population_male = models.PositiveIntegerField(
        _('male population'),
        blank=True,
        null=True
    )
    population_female = models.PositiveIntegerField(
        _('female population'),
        blank=True,
        null=True
    )
    households = models.PositiveIntegerField(
        _('number of households'),
        blank=True,
        null=True
    )
    population_year = models.PositiveIntegerField(
        _('population year'),
        blank=True,
        null=True
    )
    population_source = models.CharField(
        _('population source'),
        max_length=255,
        blank=True
    )
    geometry = models.MultiPolygonField(
        _('Geometry'),
        geography=True,
        blank=True,
        null=True
    )
    area = models.FloatField(
        _('area'),
        help_text=_('square Meters'),
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField('Created at', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('Last modified'),
        auto_now=True,
        null=True,
        blank=True
    )
    extras = JSONField(_('Extras'), blank=True, default={})

    class Meta:
        abstract = True
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def save(self, *args, **kwargs):
        if self.geometry and isinstance(self.geometry, geos.Polygon):
            self.geometry = geos.MultiPolygon(self.geometry)
        if not self.population and self.population_female\
                and self.population_male:
            self.population =\
                self.population_female + self.population_male
        self.location_description_auto = \
            self.get_location_description_auto()
        super(AbstractArea, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_location_description_auto(self):
        if not self.location_description_auto and self.parent:
            related_names = list(self.parent.get_ancestors(
                ascending=False, include_self=True)
                .values_list('name', flat=True))
            related_names = list(set(related_names))
            if related_names:
                return (', ').join(related_names)
        return self.location_description_auto


class AbstractStreet(models.Model):
    name = models.CharField(_('name'), max_length=255)
    area = models.ForeignKey(
        'hivs_administrative.Area',
        verbose_name=_('administrative area'),
        related_name='streets',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    description = models.TextField(_('description'), blank=True)
    code = models.CharField(_('code'), max_length=50, blank=True)
    location_description_auto = models.CharField(
        _('location description'),
        help_text=_('can be generated automatically'),
        max_length=255,
        blank=True
    )
    population = models.PositiveIntegerField(
        _('population'),
        blank=True,
        null=True
    )
    population_male = models.PositiveIntegerField(
        _('male population'),
        blank=True,
        null=True
    )
    population_female = models.PositiveIntegerField(
        _('female population'),
        blank=True,
        null=True
    )
    households = models.PositiveIntegerField(
        _('number of households'),
        blank=True,
        null=True
    )
    population_year = models.PositiveIntegerField(
        _('population year'),
        blank=True,
        null=True
    )
    population_source = models.CharField(
        _('population source'),
        max_length=255,
        blank=True
    )
    geometry = models.MultiLineStringField(
        _('geometry'),
        geography=True,
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField('created', auto_now_add=True)
    last_modified = models.DateTimeField(
        _('last modified'),
        auto_now=True,
        null=True,
        blank=True
    )
    extras = JSONField(_('extras'), blank=True, default={})

    class Meta:
        abstract = True
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.geometry and isinstance(self.geometry, geos.LineString):
            self.geometry = geos.MultiLineString(self.geometry)
        if not self.population and self.population_female\
                and self.population_male:
            self.population =\
                self.population_female + self.population_male
        self.location_description_auto = \
            self.get_location_description_auto()
        super(AbstractStreet, self).save(*args, **kwargs)

    def get_location_description_auto(self):
        if not self.location_description_auto and self.area:
            related_names = list(self.area.parent.get_ancestors(
                ascending=False, include_self=True)
                .values_list('name', flat=True))
            related_names = list(set(related_names))
            if related_names:
                return (', ').join(related_names)
        return self.location_description_auto
