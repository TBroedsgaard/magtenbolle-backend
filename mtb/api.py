from mtb.models import Customer, Participant, Bike, Registration
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        resource_name = "customer"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class ParticipantResource(ModelResource):
    class Meta:
        queryset = Participant.objects.all()
        resource_name = "participant"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class BikeResource(ModelResource):
    class Meta:
        queryset = Bike.objects.all()
        resource_name = "bike"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class RegistrationResource(ModelResource):
    # Customer: Name of Field (can be anything)
    # fields.ToOneField: same as ForeignKey
    # CustomerResource: The resource it maps to
    # "Customer": The attribute on the Registration model - must match what is
    # in models.py!!
    # null=True: If true, it won't fail on no customers
    Customer = fields.ToOneField(CustomerResource, "Customer", null=True)
    Participants = fields.ToManyField(ParticipantResource, "Participants")

    class Meta:
        queryset = Registration.objects.all()
        resource_name = "registration"
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
