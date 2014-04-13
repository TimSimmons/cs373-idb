from haystack import indexes
from idb.models import Player, Team, Year


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

class TeamIndex(indexes.SearchIndex, indexes.Indexable):
    text     = indexes.CharField(document=True, use_template=True)
    name     = indexes.CharField(model_attr='name')
    abbr     = indexes.CharField(model_attr='abbr')
    city     = indexes.CharField(model_attr='city')
    state    = indexes.CharField(model_attr='state')
    park     = indexes.CharField(model_attr='park')
    div      = indexes.CharField(model_attr='div')
    mgr      = indexes.CharField(model_attr='mgr')
    social   = indexes.CharField(model_attr='social')
    
    def get_model(self):
        return Team
    
    
class YearIndex(indexes.SearchIndex, indexes.Indexable):
    text     = indexes.CharField(document=True, use_template=True)
    year     = indexes.CharField(model_attr='year')
    champion = indexes.CharField(model_attr='champion')
    AL_MVP   = indexes.CharField(model_attr='AL_MVP')
    NL_MVP   = indexes.CharField(model_attr='NL_MVP')
    NL_CY    = indexes.CharField(model_attr='NL_CY')
    AL_CY    = indexes.CharField(model_attr='AL_CY')

    def get_model(self):
        return Year