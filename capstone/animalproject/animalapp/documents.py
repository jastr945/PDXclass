from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from django_elasticsearch_dsl import DocType, Index
from elasticsearch import Elasticsearch
# from . import models
from .models import Animal

connections.create_connection(hosts=['localhost'])

es = Elasticsearch(
[
    'http://elastic:changeme@localhost:9200/',
],
)


animal = Index('animals')
# See Elasticsearch Indices API reference for available settings
animal.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@animal.doc_type
class AnimalDocument(DocType):
    class Meta:
        model = Animal # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'species',
            'name',
        ]

# animal = Animal(
#     name="Pofi",
#     species="cat"
# )
# animal.save()

#
# class AnimalIndex(DocType):
#     name = Text()
#     gender = Text()
#     species = Text()
#
#     class Meta:
#         index = 'animal-index'
#
#
# def bulk_indexing():
#     AnimalIndex.init(using=es)
#     pye = AnimalIndex(name='Pyjuszek', gender='male', species='cat')
#     pye.save(using=es)
#
# def search(pet):
#     s = Search().using(es).index('animal-index').query("match", name=pet)
#     response = s.execute().to_dict()
#     return response
