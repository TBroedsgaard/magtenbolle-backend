from django.conf.urls import patterns, include, url
from mtb.api import CustomerResource

customer_resource = CustomerResource()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r"^customers/$", "mtb.views.customers"),
        url(r"^api/", include(customer_resource.urls)),
)
