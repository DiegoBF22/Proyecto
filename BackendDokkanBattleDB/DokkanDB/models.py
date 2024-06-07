from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Cards(models.Model) :
    CardID = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    CardName = models.CharField(max_length=250)
    CardIcon = models.URLField(max_length=250)
    CardArt = models.URLField(max_length=250)
    CardRarity = models.CharField(max_length=3)
    CardClass = models.CharField(max_length=50)
    CardType = models.CharField(max_length=3)
    CardTypeIcon = models.URLField(max_length=250)
    CardCost = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    CardLeader = models.TextField()
    CardLeaderOf = models.TextField()
    CardSAName = models.CharField(max_length=250)
    CardSA = models.TextField()
    CardPassiveName = models.CharField(max_length=250)
    CardPassive = models.TextField()
    CardReleaseJP = models.DateField()
    CardReleaseGL = models.DateField()
    CardCategories = models.TextField()
    CardActiveName = models.CharField(max_length=250)
    CardActive = models.TextField()
    CardCond = models.TextField()
    CardLinks = models.TextField()
    ObtainedFrom = models.URLField(max_length=200)
    BaseHP = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    BaseATK = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    BaseDEF = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    MaxLevelHP = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    MaxLevelATK = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    MaxLevelDEF = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    HP55 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    ATK55 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    DEF55 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    HP100 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    ATK100 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    DEF100 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])

class Categorias(models.Model) :
    CategoryID = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    CategoryIcon = models.URLField(max_length=250)
    CategoryName = models.CharField(max_length=250)
    CategoryCharacters = models.JSONField()
    
class Banners(models.Model) :
    BannerID = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    BannerIcon = models.URLField(max_length=250)
    BannerName = models.CharField(max_length=250)
    FeaturedCharacters = models.JSONField()
    BannerDetails = models.CharField(max_length=500)
    
class News(models.Model) :
    NewsId = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    NewsImage = models.URLField(max_length=250)
    NewsImage2 = models.URLField(max_length=250)
    NewsName = models.CharField(max_length=250)
    NewsBody = models.TextField()

class Events(models.Model) :
    EventId = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    EventIcon = models.URLField(max_length=250)
    EventName = models.CharField(max_length=250)
    EventType = models.CharField(max_length=250)
    EventWeakness = models.CharField(max_length=250)
    EventReleaseJP = models.DateField()
    EventReleaseGL = models.DateField()
    EventDetails = models.TextField()

class EventType(models.Model) :
    EventTypeId = models.IntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    EventTypeName = models.CharField(max_length=250)
    EventTypeContent = models.JSONField()