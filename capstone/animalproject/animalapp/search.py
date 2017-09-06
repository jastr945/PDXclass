from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class AnimalIndex(DocType):
    name = Text()
    intake_date = Date()
    gender = Text()
    species = Text()

    class Meta:
        index = 'animal-index'


def bulk_indexing():
    AnimalIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Animal.objects.all().iterator()))


def search(species):
    s = Search().filter('term', species=species)
    response = s.execute()
    return response
