import pytest

from tests.models import TestDoubleMonitorFieldModel


@pytest.mark.django_db
def test_recursion_errors_from_queryset_only_method_on_double_monitor_field():
    TestDoubleMonitorFieldModel.objects.create()
    # include list() to force evaluation of the queryset

    # Any field passed to only() is failing
    list(TestDoubleMonitorFieldModel.objects.only('monitored_field1'))


@pytest.mark.django_db
def test_recursion_errors_from_queryset_defer_method_on_double_monitor_field():
    TestDoubleMonitorFieldModel.objects.create()
    # include list() to force evaluation of the queryset

    # Only monitored fields passed to defer() are failing
    list(TestDoubleMonitorFieldModel.objects.defer('monitored_field2'))
