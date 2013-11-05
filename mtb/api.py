from mtb.models import Customer
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = "customer"
	fields = ["name"]
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
