from rest_framework import serializers
from DokkanDB.models import Cards, Categorias, Banners, News, Events, EventType

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cards
        fields=('CardId', 'CardName', 'CardIcon', 'CardArt', 'CardType', 'CardCost', 'CardLeader', 'CardSAName', 'CardSA', 'CardPassiveName', 'CardPassive', 'CardReleaseJP', 'CardReleaseGL', 'CardCategories', 'CardActiveName', 'CardActive', 'CardCond', 'CardLinks', 'ObtainedFrom', 'BaseHP', 'BaseATK', 'BaseDEF', 'MaxLevelHP', 'MaxLevelATK', 'MaxLevelDEF', '55HP', '55ATK', '55DEF', '100HP', '100ATK', '100DEF')

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorias
        fields=('CategoryID', 'CategoryIcon', 'CategoryName', 'CategoryCharacters')
        
class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banners
        fields=('BannerID', 'BannerIcon', 'BannerName', 'FeaturedCharacters')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=('NewsId', 'NewsImage', 'NewsImage2', 'NewsName', 'NewsBody')
        
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=('EventId', 'EventName', 'EventType', 'EventIcon', 'EventReleaseJP', 'EventReleaseGL', 'EventWeakness', 'EventDetails')
        
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventType
        fields=('EventTypeId', 'EventTypeName', 'EventTypeContent')
                