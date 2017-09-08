from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch import Elasticsearch
from . import models
import datetime

connections.create_connection()

es = Elasticsearch(
[
    'http://elastic:changeme@localhost:9200/',
],
)


class AnimalIndex(DocType):
    name = Text()
    gender = Text()
    species = Text()

    class Meta:
        index = 'animal-index'


def bulk_indexing():
    AnimalIndex.init(using=es)
    pye = AnimalIndex(name='Pyjuszek', gender='male', species='cat')
    pye.save(using=es)

def search(pet):
    s = Search().using(es).index('animal-index').query("match", name=pet)
    response = s.execute().to_dict()
    return response
