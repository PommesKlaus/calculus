from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    shortname = models.CharField(max_length=5, unique=True, verbose_name='Kürzel')
    type = models.CharField(max_length=50, verbose_name='Gesellschaftstyp')

    class Meta:
        verbose_name = 'Gesellschaft'
        verbose_name_plural = 'Gesellschaften'

    def __str__(self):
        return self.name


class Year(models.Model):
    start_date = models.DateField(verbose_name='Startdatum')
    end_date = models.DateField(verbose_name='Enddatum')
    prior_year = models.ForeignKey('self', blank=True, null=True, verbose_name='Vorjahr')
    company = models.ForeignKey('Company', verbose_name='Gesellschaft', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('company', 'end_date')
        verbose_name = 'Wirtschaftsjahr'
        verbose_name_plural = 'Wirtschaftsjahre'

    def __str__(self):
        return self.end_date.strftime("%d.%m.%Y")


class Version(models.Model):
    year = models.ForeignKey('Year', verbose_name='Jahr', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, verbose_name='Bezeichnung')
    shortname = models.CharField(max_length=5, verbose_name='Kürzel')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    closed = models.BooleanField(default=False, verbose_name='Geschlossen')
    py_version = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='version_py_version',
        verbose_name='Vorjahresversion',
        on_delete=models.PROTECT)  # Was ist die Vergleichsversion im Vorjahr?
    tu_version = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='version_tu_version',
        verbose_name='Matching-Version',
        on_delete=models.PROTECT)  # Welche Version im Vorjahr hat aktualisierte Werte?

    class Meta:
        unique_together = ('year', 'shortname')
        verbose_name = 'Version'
        verbose_name_plural = 'Versionen'

    def __str__(self):
        return self.name
