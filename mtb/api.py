from mtb.models import ContactPerson, Customer, Bike, Checkin, Payment, Dummy, Dimmy
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields


class DummyResource(ModelResource):
    class Meta:
        queryset = Dummy.objects.all()
        resource_name = "dummy"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class DimmyResource(ModelResource):
    Dummy = fields.ToOneField(DummyResource, "Dummy", full=True)

    class Meta:
        queryset = Dimmy.objects.all()
        resource_name = "dimmy"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class ContactPersonResource(ModelResource):
    class Meta:
        queryset = ContactPerson.objects.all()
        resource_name = "contactperson"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = "customer"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class BikeResource(ModelResource):
    class Meta:
        queryset = Bike.objects.all()
        resource_name = "bike"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class PaymentResource(ModelResource):
    class Meta:
        queryset = Payment.objects.all()
        resource_name = "payment"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class CheckinResource(ModelResource):
    # ContactPerson: Name of Field (can be anything)
    # fields.ToOneField: same as ForeignKey
    # ContactPersonResource: The resource it maps to
    # "ContactPerson": The attribute on the Registration model - must match
    # what is in models.py!!
    # null=True: If true, it won't fail on no customers
    ContactPerson = fields.ToOneField(ContactPersonResource, "ContactPerson",
                                      full=True)
    Customers = fields.ToManyField(CustomerResource, "Customers", null=True,
                                   full=True)
    Bikes = fields.ToManyField(BikeResource, "Bikes", null=True, full=True)
    Payment = fields.ToOneField(PaymentResource, "Payment", full=True)

    class Meta:
        queryset = Checkin.objects.all()
        resource_name = "checkin"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
