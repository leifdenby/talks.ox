from datetime import datetime

import factory

from . import models


class EventGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EventGroup


class EventFactory(factory.django.DjangoModelFactory):
    start = datetime(2015, 10, 23, 12, 18)
    end = datetime(2015, 10, 30, 20, 25)

    class Meta:
        model = models.Event


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Person

