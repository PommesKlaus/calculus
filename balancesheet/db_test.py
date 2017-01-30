from .models import BsLineItem, Difference
from core.models import Version
from django.db.models import Sum, Case, When, DecimalField
from random import randrange
from decimal import Decimal


def init_db():
    # New Version
    v = Version(year_id=1, name="DUMMY", shortname="XXX")
    v.save()

    # Create 1,000 random data entries for BsLineItems 1 to 13
    difference_list = []
    for i in range(1000):
        difference_list.append(Difference(
            name="Test {0}".format(i),
            bs_line_item_id=randrange(1, 13, 1),
            version=v,
            tax_gaap=Decimal(randrange(-100000, 100000, 10))
        ))
    Difference.objects.bulk_create(difference_list)


def test_python_aggregate():
    v = Version.objects.get(shortname="XXX")

    # Get all BsLineItems (including those without any differences)
    l = list(BsLineItem.objects.all().values())

    # Get all BsLineItems with aggregates (excludes those without any differences)
    d = list(BsLineItem.objects.filter(difference__version_id=v.id).annotate(
        subtotal_difference=Sum('difference__difference'),
        subtotal_pl_permanent=Sum('difference__pl_permanent'),
        subtotal_oci_permanent=Sum('difference__oci_permanent'),
        subtotal_permanent=Sum('difference__permanent'),
        subtotal_pl_temporary=Sum('difference__pl_temporary'),
        subtotal_oci_temporary=Sum('difference__oci_temporary'),
        subtotal_temporary=Sum('difference__temporary'),
        subtotal_pl=Sum('difference__pl'),
        subtotal_oci=Sum('difference__oci'),
        subtotal_pl_true_up=Sum('difference__pl_true_up'),
        subtotal_oci_true_up=Sum('difference__oci_true_up'),
        subtotal_pl_movement=Sum('difference__pl_movement'),
        subtotal_oci_movement=Sum('difference__oci_movement')
    ).values())

    # Combine l and d, setting defaults to Decimal(0.00)

    # Step1: Convert d to dict with id as key
    d_dict = {}
    for elem in d:
        d_dict[elem['id']] = elem

    # Step2: Add additional fields to l
    for elem in l:
        if elem['id'] in d_dict:
            elem['subtotal_difference'] = d_dict[elem['id']]['subtotal_difference']
            elem['subtotal_pl_permanent'] = d_dict[elem['id']]['subtotal_pl_permanent']
            elem['subtotal_oci_permanent'] = d_dict[elem['id']]['subtotal_oci_permanent']
            elem['subtotal_permanent'] = d_dict[elem['id']]['subtotal_permanent']
            elem['subtotal_pl_temporary'] = d_dict[elem['id']]['subtotal_pl_temporary']
            elem['subtotal_oci_temporary'] = d_dict[elem['id']]['subtotal_oci_temporary']
            elem['subtotal_temporary'] = d_dict[elem['id']]['subtotal_temporary']
            elem['subtotal_pl'] = d_dict[elem['id']]['subtotal_pl']
            elem['subtotal_oci'] = d_dict[elem['id']]['subtotal_oci']
            elem['subtotal_pl_true_up'] = d_dict[elem['id']]['subtotal_pl_true_up']
            elem['subtotal_oci_true_up'] = d_dict[elem['id']]['subtotal_oci_true_up']
            elem['subtotal_pl_movement'] = d_dict[elem['id']]['subtotal_pl_movement']
            elem['subtotal_oci_movement'] = d_dict[elem['id']]['subtotal_oci_movement']
        else:
            elem['subtotal_difference'] = Decimal('0.00')
            elem['subtotal_pl_permanent'] = Decimal('0.00')
            elem['subtotal_oci_permanent'] = Decimal('0.00')
            elem['subtotal_permanent'] = Decimal('0.00')
            elem['subtotal_pl_temporary'] = Decimal('0.00')
            elem['subtotal_oci_temporary'] = Decimal('0.00')
            elem['subtotal_temporary'] = Decimal('0.00')
            elem['subtotal_pl'] = Decimal('0.00')
            elem['subtotal_oci'] = Decimal('0.00')
            elem['subtotal_pl_true_up'] = Decimal('0.00')
            elem['subtotal_oci_true_up'] = Decimal('0.00')
            elem['subtotal_pl_movement'] = Decimal('0.00')
            elem['subtotal_oci_movement'] = Decimal('0.00')

    print(l)


def test_sql_aggregate():
    v = Version.objects.get(shortname="XXX")
    l = BsLineItem.objects.annotate(
        subtotal_difference=Sum(Case(When(difference__version_id=v.id, then='difference__difference'), default=0.00,
                                     output_field=DecimalField(decimal_places=2))),
        subtotal_pl_permanent=Sum(Case(When(difference__version_id=v.id, then='difference__pl_permanent'), default=0.00,
                                     output_field=DecimalField(decimal_places=2))),
        subtotal_oci_permanent=Sum(Case(When(difference__version_id=v.id, then='difference__oci_permanent'), default=0.00,
                                     output_field=DecimalField(decimal_places=2))),
        subtotal_permanent=Sum(Case(When(difference__version_id=v.id, then='difference__permanent'), default=0.00,
                                        output_field=DecimalField(decimal_places=2))),
        subtotal_pl_temporary=Sum(Case(When(difference__version_id=v.id, then='difference__pl_temporary'), default=0.00,
                                    output_field=DecimalField(decimal_places=2))),
        subtotal_oci_temporary=Sum(Case(When(difference__version_id=v.id, then='difference__oci_temporary'), default=0.00,
                                       output_field=DecimalField(decimal_places=2))),
        subtotal_temporary=Sum(Case(When(difference__version_id=v.id, then='difference__temporary'), default=0.00,
                                        output_field=DecimalField(decimal_places=2))),
        subtotal_pl=Sum(Case(When(difference__version_id=v.id, then='difference__pl'), default=0.00,
                                        output_field=DecimalField(decimal_places=2))),
        subtotal_oci=Sum(Case(When(difference__version_id=v.id, then='difference__oci'), default=0.00,
                                        output_field=DecimalField(decimal_places=2))),
        subtotal_pl_true_up=Sum(Case(When(difference__version_id=v.id, then='difference__pl_true_up'), default=0.00,
                              output_field=DecimalField(decimal_places=2))),
        subtotal_oci_true_up=Sum(Case(When(difference__version_id=v.id, then='difference__oci_true_up'), default=0.00,
                              output_field=DecimalField(decimal_places=2))),
        subtotal_pl_movement=Sum(Case(When(difference__version_id=v.id, then='difference__pl_movement'), default=0.00,
                              output_field=DecimalField(decimal_places=2))),
        subtotal_oci_movement=Sum(Case(When(difference__version_id=v.id, then='difference__oci_movement'), default=0.00,
                              output_field=DecimalField(decimal_places=2))),
    )
    #print(list(l.values()))


def clear_db():
    # Find Dummy-Version
    v = Version.objects.get(shortname="XXX")

    # Delete 1,000 Dummy-Rows from Difference-Table
    d = Difference.objects.filter(version=v)
    d.delete()

    # Delete Dummy-Version
    v.delete()

    print("OK, Database is now clean.")
