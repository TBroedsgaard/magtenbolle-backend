from tastypie.resources import ModelResource
from mtb.models import Customer


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = "customer"
