from django.conf.urls import url

from pizza_app.views import create, view, close, stats, status

urlpatterns = [
    url(r'^create/', create, name='create'),
    # view/<int:pizza_order_id>
    url(r'^view/(?P<pizza_order_id>[0-9]+)/', view, name='view'),
    url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    url(r'^status/(?P<pizza_order_id>[0-9]+)/', status, name='status'),

    url(r'^stats/', stats, name='stats'),
]
