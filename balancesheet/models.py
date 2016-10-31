from django.db import models
from datetime import datetime

from core.models import Version

# Create your models here.


class BsLineItem(models.Model):
    name = models.CharField(max_length=160, verbose_name='Bezeichnung')
    sorting = models.PositiveSmallIntegerField(verbose_name='Sortierung/Position')

    class Meta:
        ordering = ['sorting']
        verbose_name = 'Bilanzlinie'
        verbose_name_plural = 'Bilanzlinien'

    def __str__(self):
        return self.name


class Difference(models.Model):
    name = models.CharField(max_length=160, default=str(datetime.now()))
    comment = models.TextField(null=True, blank=True, default='')
    bs_line_item = models.ForeignKey('BsLineItem', on_delete=models.PROTECT)
    version = models.ForeignKey(Version, related_name='Difference_version')

    local_gaap = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tax_gaap = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    difference = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    pl_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    oci_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    pl_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    oci_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    pl = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    oci = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field

    py_local_gaap = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_tax_gaap = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_difference = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_pl_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_oci_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_pl_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_oci_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_pl = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    py_oci = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)

    tu_local_gaap = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_tax_gaap = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_difference = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_pl_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_oci_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_permanent = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_pl_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_oci_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_temporary = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_pl = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    tu_oci = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)

    pl_true_up = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    oci_true_up = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    pl_movement = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field
    oci_movement = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)  # Calculated Field

    class Meta:
        # unique_together = ('name', 'version', 'bs_line_item')
        ordering = ['name']
        verbose_name = 'Differenz'
        verbose_name_plural = 'Differenzen'

    def __str__(self):
        return self.name + " (" + str(self.pl_temporary) + ")"

    def save(self, *args, **kwargs):
        self.difference = self.tax_gaap - self.local_gaap
        self.permanent = self.pl_permanent + self.oci_permanent
        self.temporary = self.difference - self.permanent
        self.oci = self.oci_permanent + self.oci_temporary
        self.pl_temporary = self.difference - self.oci - self.pl_permanent
        self.pl = self.pl_temporary + self.pl_permanent
        self.pl_true_up = self.tu_pl - self.py_pl
        self.oci_true_up = self.tu_oci - self.py_oci
        self.pl_movement = self.pl - self.tu_pl
        self.oci_movement = self.oci - self.tu_oci
        super(Difference, self).save(*args, **kwargs)
