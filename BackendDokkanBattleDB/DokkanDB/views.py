from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DokkanDB.models import Cards, Categorias, Banners, News, Events, EventType

# Create your views here.

@csrf_exempt

# Método que devuelve todas las cartas
# Method that returns every card
def devolverCartas(request):
    if request.method != "GET":
        return JsonResponse({"error": "Incorrect method, must be GET"}, status=405)
    
    cards = Cards.objects.all()
    cardsList = []
    for fila in cards:
        diccionario = {}
        diccionario['cardId'] = fila.CardID
        diccionario['cardName'] = fila.CardName
        diccionario['cardIcon'] = fila.CardIcon
        diccionario['cardRarity'] = fila.CardRarity
        diccionario['cardClass'] = fila.CardClass
        diccionario['cardType'] = fila.CardType
        diccionario['cardTypeIcon'] = fila.CardTypeIcon
        diccionario['cardCost'] = fila.CardCost
        diccionario['leader'] = fila.CardLeader
        diccionario['leaderOf'] = fila.CardLeaderOf
        diccionario['nameSA'] = fila.CardSAName
        diccionario['sA'] = fila.CardSA
        diccionario['passiveName'] = fila.CardPassiveName
        diccionario['passive'] = fila.CardPassive
        diccionario['releaseJP'] = fila.CardReleaseJP
        diccionario['releaseGB'] = fila.CardReleaseGL
        diccionario['categories'] = fila.CardCategories
        diccionario['activeName'] = fila.CardActiveName
        diccionario['active'] = fila.CardActive
        diccionario['activeConditions'] = fila.CardCond
        diccionario['links'] = fila.CardLinks
        diccionario['obtainedFrom'] = fila.ObtainedFrom
        diccionario['baseHP'] = fila.BaseHP
        diccionario['baseATK'] = fila.BaseATK
        diccionario['baseDEF'] = fila.BaseDEF
        diccionario['maxHP'] = fila.MaxLevelHP
        diccionario['maxATK'] = fila.MaxLevelATK
        diccionario['maxDEF'] = fila.MaxLevelDEF
        diccionario['hp55'] = fila.HP55
        diccionario['atk55'] = fila.ATK55
        diccionario['def55'] = fila.DEF55
        diccionario['hp100'] = fila.HP100
        diccionario['atk100'] = fila.ATK100
        diccionario['def100'] = fila.DEF100
        cardsList.append(diccionario)
    
    return JsonResponse(cardsList, safe=False, json_dumps_params={'ensure_ascii': False})

# Método que devuelve una carta específica
# Method that returns a specific card
def devolverCartaPorId(request, idCard):
    try:
        card = Cards.objects.get(CardID=idCard)
        diccionario = {
            'cardId': card.CardID,
            'cardName': card.CardName,
            'cardIcon': card.CardIcon,
            'cardArt': card.CardArt,
            'cardClass': card.CardClass,
            'cardType': card.CardType,
            'cardTypeIcon': card.CardTypeIcon,
            'cardCost': card.CardCost,
            'leader': card.CardLeader,
            'nameSA': card.CardSAName,
            'sA': card.CardSA,
            'passiveName': card.CardPassiveName,
            'passive': card.CardPassive,
            'releaseJP': card.CardReleaseJP,
            'releaseGB': card.CardReleaseGL,
            'categories': card.CardCategories,
            'active': card.CardActive,
            'activeConditions': card.CardCond,
            'links': card.CardLinks,
            'obtainedFrom': card.ObtainedFrom,
            'baseHP': card.BaseHP,
            'baseATK': card.BaseATK,
            'baseDEF': card.BaseDEF,
            'maxHP': card.MaxLevelHP,
            'maxATK': card.MaxLevelATK,
            'maxDEF': card.MaxLevelDEF,
            'hp55': card.HP55,
            'atk55': card.ATK55,
            'def55': card.DEF55,
            'hp100': card.HP100,
            'atk100': card.ATK100,
            'def100': card.DEF100,
        }
    except Cards.DoesNotExist:
        return JsonResponse({'error': 'That card does not exist'}, status=404)
    return JsonResponse(diccionario, safe=False, json_dumps_params={'ensure_ascii': False})


# Método que devuelve todas las categorías
# Method that returns every category
def devolverCategorias(request):
    if request.method != "GET":
        return JsonResponse({"error":"Incorrect method, must be GET"}, status=405)
    categories = Categorias.objects.all()
    categoriesList = []
    for fila in categories:
        diccionario = {}
        diccionario['categoryId'] = fila.CategoryID
        diccionario['categoryIcon'] = fila.CategoryIcon
        diccionario['categoryName'] = fila.CategoryName
        diccionario['categoryCharacters'] = fila.CategoryCharacters
        categoriesList.append(diccionario)
        
    return JsonResponse(categoriesList, safe = False, json_dumps_params={'ensure_ascii': False} )

# Método que devuelve una categoría específica
# Method that returns a specific category
def devolverCategoriasPorId(request, idCategory):
    try:
            category = Categorias.objects.get(CategoryID=idCategory)
            diccionario = {
                'categoryId': category.CategoryID,
                'categoryIcon': category.CategoryIcon,
                'categoryName': category.CategoryName,
                'categoryCharacters': category.CategoryCharacters
            }
    except Cards.DoesNotExist:
        return JsonResponse({'error': 'That category does not exist'}, status=404)
    return JsonResponse(diccionario, safe=False, json_dumps_params={'ensure_ascii': False})
    
# Método que devuelve todos los banners
# Method that returns every banner
def devolverBanners(request):
    if request.method != "GET":
        return JsonResponse({"error":"Incorrect method, must be GET"}, status=405)
    banners = Banners.objects.all()
    bannersList = []
    for fila in banners:
        diccionario = {}
        diccionario['bannerID'] = fila.BannerID
        diccionario['bannerIcon'] = fila.BannerIcon
        diccionario['bannerName'] = fila.BannerName
        diccionario['bannerCharacters'] = fila.FeaturedCharacters
        diccionario['bannerDetails'] = fila.BannerDetails
        bannersList.append(diccionario)
        
    return JsonResponse(bannersList, safe = False, json_dumps_params={'ensure_ascii': False} )
    
# Método que devuelve un banner específico
# Method that returns a specific banner
def devolverBannerPorId(request, idBanner):
    try:
            banner = Banners.objects.get(BannerID=idBanner)
            diccionario = {
                'bannerID': banner.BannerID,
                'bannerIcon': banner.BannerIcon,
                'bannerName': banner.BannerName,
                'bannerCharacters': banner.FeaturedCharacters,
                'bannerDetails': banner.BannerDetails
            }
    except Cards.DoesNotExist:
        return JsonResponse({'error': 'That banner does not exist'}, status=404)
    return JsonResponse(diccionario, safe=False, json_dumps_params={'ensure_ascii': False})
    
# Método que devuelve todas las noticias
# Method that returns every news
def devolverNews(request):
    if request.method != "GET":
        return JsonResponse({"error":"Incorrect method, must be GET"}, status=405)
    news = News.objects.all()
    newsList = []
    for fila in news:
        diccionario = {}
        diccionario['newsID'] = fila.NewsId
        diccionario['newsImage'] = fila.NewsImage
        diccionario['newsImage2'] = fila.NewsImage2
        diccionario['newsName'] = fila.NewsName
        diccionario['newsBody'] = fila.NewsBody
        newsList.append(diccionario)
        
    return JsonResponse(newsList, safe = False, json_dumps_params={'ensure_ascii': False} )

# Método que devuelve una noticia específica
# Method that returns a specific news
def devolverNewsPorId(request, idNews):
    try:
            news = News.objects.get(NewsId=idNews)
            diccionario = {
                'newsID': news.NewsId,
                'newsImage': news.NewsImage,
                'newsImage2': news.NewsImage2,
                'newsName': news.NewsName,
                'newsBody': news.NewsBody
            }
    except Cards.DoesNotExist:
        return JsonResponse({'error': 'That news does not exist'}, status=404)
    return JsonResponse(diccionario, safe=False, json_dumps_params={'ensure_ascii': False})
    
# Método que devuelve todos los eventos
# Method that returns every event
def devolverEvents(request):
    if request.method != "GET":
        return JsonResponse({"error":"Incorrect method, must be GET"}, status=405)
    events = Events.objects.all()
    eventsList = []
    for fila in events:
        diccionario = {}
        diccionario['eventId'] = fila.EventId
        diccionario['eventIcon'] = fila.EventIcon
        diccionario['eventName'] = fila.EventName
        diccionario['eventType'] = fila.EventType
        diccionario['eventWeakness'] = fila.EventWeakness
        diccionario['eventReleaseJP'] = fila.EventReleaseJP
        diccionario['eventReleaseGL'] = fila.EventReleaseGL
        diccionario['eventDetails'] = fila.EventDetails
        eventsList.append(diccionario)
        
    return JsonResponse(eventsList, safe = False, json_dumps_params={'ensure_ascii': False} )

# Método que devuelve un evento específico
# Method that returns a specific event
def devolverEventPorId(request, idEvent):
    try:
            event = Events.objects.get(EventId=idEvent)
            diccionario = {
                'eventId': event.EventId,
                'eventIcon': event.EventIcon,
                'eventName': event.EventName,
                'eventType': event.EventType,
                'eventWeakness': event.EventWeakness,
                'eventReleaseJP': event.EventReleaseJP,
                'eventReleaseGL': event.EventReleaseGL,
                'eventDetails': event.EventDetails
            }
    except Cards.DoesNotExist:
        return JsonResponse({'error': 'That event does not exist'}, status=404)
    return JsonResponse(diccionario, safe=False, json_dumps_params={'ensure_ascii': False})

# Método que devuelve todos los tipos de eventos
# Method that returns every event type
def devolverEventType(request):
    if request.method != "GET":
        return JsonResponse({"error":"Incorrect method, must be GET"}, status=405)
    eventType = EventType.objects.all()
    eventTypeList = []
    for fila in eventType:
        diccionario = {}
        diccionario['eventTypeId'] = fila.EventTypeId
        diccionario['eventTypeName'] = fila.EventTypeName
        diccionario['eventTypeContent'] = fila.EventTypeContent
        eventTypeList.append(diccionario)
        
    return JsonResponse(eventTypeList, safe = False, json_dumps_params={'ensure_ascii': False} )
    
# Método que devuelve un tipo de evento específico
# Method that returns a specific event type
def devolverEventTypePorId(request, idEventType):
    try:
        eventType = EventType.objects.get(EventTypeId=idEventType)  # Cambio aquí
        diccionario = {
            'eventTypeId': eventType.EventTypeId,
            'eventTypeName': eventType.EventTypeName,
            'eventTypeContent': eventType.EventTypeContent
        }
    except EventType.DoesNotExist:  # Cambio aquí
        return JsonResponse({'error': 'That event type does not exist'}, status=404)
    return JsonResponse(diccionario, safe=False, json_dumps_params={'ensure_ascii': False})