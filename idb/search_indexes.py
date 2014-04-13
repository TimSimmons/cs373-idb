from haystack import indexes
from idb.models import Player


class PlayerIndex(indexes.SearchIndex, indexes.Indexable):
    text     = indexes.CharField(document=True, use_template=True)
    name     = indexes.CharField(model_attr='name')
    number   = indexes.IntegerField(model_attr='number')
    position = indexes.CharField(model_attr='position')
    bats     = indexes.CharField(model_attr='bats')
    throws   = indexes.CharField(model_attr='throws')
    height   = indexes.IntegerField(model_attr='height')
    weight   = indexes.IntegerField(model_attr='weight')
    school   = indexes.CharField(model_attr='school')
    social   = indexes.CharField(model_attr='social')
    link     = indexes.CharField(model_attr='gen_link')

    def get_model(self):
        return Player

class PlayerIndex(indexes.SearchIndex, indexes.Indexable):
    text     = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Team
