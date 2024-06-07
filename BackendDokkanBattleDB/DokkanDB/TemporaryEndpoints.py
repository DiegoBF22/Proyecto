from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def cartas(request):
  return JsonResponse([{
        "CardId": 12879,
        "CardName": "Pressed-for-Time Showdown Super Saiyan 3 Goku (Angel)Pressed-for-Time Showdown Super Saiyan 3 Goku (Angel)",
        "CardIcon":"https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/ff/Card_1028320_thumb_apng.png/revision/latest?cb=20240215090620",
        "CardArt": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/70/Card_1028790_artwork.png/revision/latest?cb=20240425030801",
        "CardType": "AGL",
        "CardCost": 58,
        "CardLeader": '"Majin Buu Saga", "Otherworld Warriors" or "Accelerated Battle" Category Ki +3 and HP, ATK & DEF +170%; plus an additional HP, ATK & DEF +30% for characters who also belong to the "Kamehameha" or "Time Limit" Category',
        "CardSAName": "Instant Transmission Meteor Crush",
        "CardSA": "Greatly raises ATK & DEF for 1 turn and causes immense damage with a high chance of stunning the enemy",
        "CardPassiveName": "Buying Time at All Costs",
        "CardPassive": "Activates the Entrance Animation (once only), chance of performing a critical hit +50% for 5 turns from the character's entry turn and reduces damage received by 90% upon the character's entry and with each turn passed, damage reduction rate -15% (no more than -90%) when there is another 'Majin Buu Saga' Category ally on the team upon the character's entry; Ki +2 and ATK & DEF +150%; plus an additional ATK & DEF +150% when performing a Super Attack; reduces damage received by 5% with each Super Attack performed (up to 30%); medium chance of performing a critical hit; launches an additional attack that has a great chance of becoming a Super Attack; when there is another 'Majin Buu Saga' Category ally attacking in the same turn, plus an additional DEF +100% and guards all attacks as the 1st attacker in a turn and an additional ATK +100% and launches an additional Super Attack as the 2nd or 3rd attacker in a turn; high chance of nullifying Ki Blast Super Attacks directed at the character and countering with tremendous power",
        "CardReleaseJP": "26-04-2024",
        "CardReleaseGL": "26-04-2024",
        "CardCategories": ["Resurrected Warriors", "Majin Buu Saga", "Super Saiyan 3", "Pure Saiyans", "Goku's Family", "Kamehameha", "Otherworld Warriors", "Turtle School", "Time limit", "Mastered Evolution", "Bond of Friendship", "Accelerated Battle", "Power Beyond Super Saiyan", "Bond of Parent and Child", "Earth-Bred Fighters"],
        "CardActiveName": "Full Power Kamehameha",
        "CardActive": "Massively raises ATK temporarily, causes ultimate damage to enemy and, within the turn activated, all attacks become critical hits",
        "CardCond": 'Can be activated when there is another "Majin Buu Saga" Category ally attacking in the same turn starting from the 4th turn from the start of battle (once only)',
        "CardLinks": ["Golden Warrior", "Super Saiyan", "Over in a Flash", "Limit-Breaking Form", "Kamehameha", "Fierce Battle"],
        "ObtainedFrom": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/be/Card_1028780_thumb.png/revision/latest?cb=20240427170415",
        "BaseHP": 4045,
        "BaseATK": 3242,
        "BaseDEF": 2371,
        "MaxLevelHP": 13350,
        "MaxLevelATK": 10700,
        "MaxLevelDEF": 7825,
        "55HP": 15350,
        "55ATK": 12700,
        "55DEF": 9825,
        "100HP": 17950,
        "100ATK": 15700,
        "100DEF": 13225
    },
    {
        "CardId": 12099,
        "CardName": "Peerless Super Power Super Saiyan 4 Gogeta",
        "CardIcon":"https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/94/Card_1020990_thumb.png/revision/latest?cb=20210131044903",
        "CardArt": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/23/Card_1020990_artwork.png/revision/latest?cb=20201029030722",
        "CardType": "INT",
        "CardCost": 58,
        "CardLeader": '"Giant Ape Power" Category Ki +3 and HP, ATK & DEF +170%; or "Shadow Dragon Saga" Category Ki +3 and HP, ATK & DEF +150%',
        "CardSAName": "Big Bang Kamehameha",
        "CardSA": "Greatly raises ATK & DEF for 1 turn and causes immense damage to enemy",
        "CardPassiveName": "Power to Annihilate Evil",
        "CardPassive": "ATK & DEF +200%; Ki +4 plus an additional ATK & DEF +40% and attacks effective against all Types for 8 turns from start of turn; high chance of attacks being effective against all Types starting from the 9th turn from the start of battle; high chance of nullifying enemy's Super Attack and countering with tremendous power",
        "CardReleaseJP": "30-10-2020",
        "CardReleaseGL": "01-02-2021",
        "CardCategories": ["Fusion", "Shadow Dragon Saga", "Kamehameha", "Final Trump Card", "Giant Ape Power", "GT Heroes", "Time Limit", "Accelerated Battle", "Battle of Fate", "Power Beyond Super Saiyan", "Fused Fighters"],
        "CardActiveName": "Plus Energy Emission",
        "CardActive": "ATK & DEF +40% and all enemies' ATK & DEF -40% for 1 turn",
        "CardCond": 'Can be activated after the character receives attack 4 or more times in battle (once only)',
        "CardLinks": ["Super Saiyan", "Kamehameha", "Shocking Speed", "Over in a Flash", "GT", "Fused Fighter", "Fierce Battle"],
        "ObtainedFrom": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a1/Card_1020980_thumb.png/revision/latest?cb=20210131044905",
        "BaseHP": 3705,
        "BaseATK": 3834,
        "BaseDEF": 1492,
        "MaxLevelHP": 12350,
        "MaxLevelATK": 12780,
        "MaxLevelDEF": 4975,
        "55HP": 14350,
        "55ATK": 14780,
        "55DEF": 6975,
        "100HP": 17350,
        "100ATK": 17780,
        "100DEF": 9975
      },
    {
        "CardId": 12832,
        "CardName": "New Power Beyond Ultimate Gohan (Beast)",
        "CardIcon":"https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/ff/Card_1028320_thumb_apng.png/revision/latest?cb=20240215090620",
        "CardArt": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f0/Card_1028320_artwork_apng.webp/revision/latest?cb=20240215105558",
        "CardType": "STR",
        "CardCost": 77,
        "CardLeader": '"Super Heroes", "Bond of Master and Disciple" or "Miraculous Awakening" Category Ki +3 and HP, ATK & DEF +170%; plus an additional HP, ATK & DEF +30% for characters who also belong to the "Entrusted Will" or "Movie Heroes" Category',
        "CardSAName": "Vicious Demon Flash",
        "CardSA": "Greatly raises ATK and raises DEF for 1 turn and causes colossal damage to enemy",
        "CardPassiveName": "Fearsome Beast Awoken",
        "CardPassive": "Activates the Entrance Animation upon entry (once only); Ki +8 and chance of performing a critical hit +40% and reduces damage received by 40% for 5 turns from the character's entry turn; Ki +3, ATK & DEF +250% and guards all attacks; plus an additional ATK +50% when attacking; chance of performing a critical hit +20% when Ki is 24; plus an additional DEF +80% and reduces damage received by 20% if Ki is 24 when receiving an attack; Ki +1 per Ki Sphere obtained; launches an additional Super Attack and all allies' Ki +3 (self excluded) within the same turn after receiving an attack; Ki +1 (up to 5) and, within the same turn, ATK and chance of performing a critical hit +20%, with each attack received; plus an additional chance of performing a critical hit +20%, an additional damage reduction of 20% and all allies' Ki +2 starting from the turn in which the character performs the 5th attack or receives the 8th attack in battle",
        "CardReleaseJP": "16-02-2024",
        "CardReleaseGL": "00-00-0000",
        "CardCategories": ["Hybrid Saiyans", "Full Power", "Movie Heroes", "Goku's Family", "Siblings Bond", "Bond of Master and Disciple", "Exploding Rage", "Connected Hope", "Miraculous Awakening", "Entrusted Will", "Battle of Fate", "Bond of Parent and Child", "Earth-Bred Fighters", "Super Heroes"],
        "CardActiveName": "Gohan's Confidence",
        "CardActive": "Ki +24, DEF +158%, character intercepts all enemies' attacks and performs a critical hit for 1 turn",
        "CardCond": 'Can be activated upon entering next attacking turn after receiving an attack (once only)',
        "CardLinks": ["All in the Family", "Saiyan Warrior Race", "Infighter", "Shocking Speed", "Prepared for Battle", "Fierce Battle", "Legendary Power"],
        "ObtainedFrom": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/54/Card_1028310_thumb.png/revision/latest?cb=20240215133854",
        "BaseHP": 4992,
        "BaseATK": 4628,
        "BaseDEF": 3119,
        "MaxLevelHP": 16475,
        "MaxLevelATK": 15275,
        "MaxLevelDEF": 10294,
        "55HP": 18475,
        "55ATK": 14780,
        "55DEF": 12294,
        "100HP": 21475,
        "100ATK": 20675,
        "100DEF": 14894
      }], safe=False)

def categorias(request):
  return JsonResponse([{
        "CategoryID": 1,
        "CategoryIcon": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/3c/Power_Beyond_Super_Saiyan_Category.png/revision/latest/scale-to-width-down/200?cb=20230817034727",
        "CategoryName": "Power Beyond Super Saiyan",
        "CategoryCharacters": [12879, 12099]
        
      },
    {
        "CategoryID": 2,
        "CategoryIcon": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5d/Majin_Buu_Saga_Category.png/revision/latest/scale-to-width-down/200?cb=20230817034541",
        "CategoryName": "Majin Buu Saga",
        "CategoryCharacters": [12879]
        
      },
    {
        "CategoryID": 3,
        "CategoryIcon": "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0a/Goku%27s_Family_Category.png/revision/latest/scale-to-width-down/200?cb=20230817034423",
        "CategoryName": "Goku's Family",
        "CategoryCharacters": [12879, 12832]
        
      }], safe=False)
  
def Banners(request):
  return JsonResponse([{
        "BannerID": 1,
        "BannerIcon": "https://drive.google.com/file/d/1-ID1R6hmm9zdrUHqTKs4DA5bqqQooUjB/view?usp=drive_link",
        "BannerName": "Legendary Summon",
        "FeaturedCharacters": [12879, 12099]
      },
    {
        "BannerID": 2,
        "BannerIcon": "https://drive.google.com/file/d/1R8frsDuxHj70ePg37uZNkz1nwXWjTI45/view?usp=drive_link",
        "BannerName": "Dokkan Festival (A)",
        "FeaturedCharacters": [12879, 12099]
      },
    {
        "BannerID": 3,
        "BannerIcon": "https://drive.google.com/file/d/1OBAsvyPLxLZb45w8ecEjZHXBruRnTpdE/view?usp=drive_link",
        "BannerName": "Dokkan Festival (B)",
        "FeaturedCharacters": [12879, 12099]
      },], safe=False)
  
def News(request):
  return JsonResponse([{
        "NewsId": 1,
        "NewsImage": "https://drive.google.com/file/d/1HUUoiMtEG3o4xAYOegJrHe-ObT6cKwlJ/view?usp=drive_link",
        "NewsImage2": "https://drive.google.com/file/d/13oiUAoglGHtsGXSvvWW8FKp9p46JMXDh/view?usp=drive_link",
        "NewsName": "Incredible Surprise! Dokkan Special Missions Part 2!",
        "NewsBody": (
            "Incredible Surprise! Dokkan Special Missions Part 2 is here!\n"
            "Get rewards including Dragon Stones and '30' Special Summon Tickets!\n\n"
            "Start Date: 5/14/2024 2:00:00 AM CEST\n\n"
            "News 1\n"
            "Event Period\n"
            "Fri, 4/26 2:00 AM CEST ~ Fri, 5/31 1:59 AM CEST\n\n"
            "Incredible Surprise! Dokkan Special Missions are here!\n\n"
            "Missions from Part 2 are available starting from Tue, 5/14 CEST!\n\n"
            "Complete the Event Missions to get Dragon Stones, Potential Orbs and other rewards! You can also recruit [Mysterious Ritual] Elder Kai!\n\n"
            "A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2! The Summon Tickets can be used to perform a summon in the 'Incredible Surprise! '30' Special Summon'!\n\n"
            "In addition, the Daily Mission that allows you to recruit [Light Doze] Elder Kai (Dozing) is still available!\n\n"
            "Complete missions to obtain all the awesome rewards!\n"
            "Mission Details\n\n"
            "News 1\n"
            "* Event Missions can only be completed once.\n\n"
            "* Please go to the 'Daily Missions' and 'Event Missions' pages for more information.\n\n"
            "* Daily Missions will reset daily at 2:00 AM CEST. Please claim the rewards of the Daily Missions by 1:59 AM CEST the next day.\n\n"
            "* Daily Missions are excluded from the completion conditions of the missions 'Complete 10 or more Part 1 missions!', 'Complete all the Part 1 missions!', 'Complete 10 or more Part 2 missions!' and 'Complete all the 'Incredible Surprise! Dokkan Special Missions'!'.\n\n"
            "* 30 '30' Special Summon Tickets are required to perform a summon in the 'Incredible Surprise! '30' Special Summon'. A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2, and another 10 '30' Special Summon Tickets can be obtained upon the first login between Fri, 4/26 5:00 AM CEST and Fri, 5/31 1:59 AM CEST.\n\n"
            "* The system time is in accordance with Greenwich Mean Time.\n\n"
            "* Please note that the event content and dates are subject to change without prior warning.\n\n"
            "We hope you continue to enjoy playing Dragon Ball Z Dokkan Battle!"
        )
      },
    {
        "NewsId": 2,
        "NewsImage": "https://drive.google.com/file/d/1HUUoiMtEG3o4xAYOegJrHe-ObT6cKwlJ/view?usp=drive_link",
        "NewsImage2": "https://drive.google.com/file/d/13oiUAoglGHtsGXSvvWW8FKp9p46JMXDh/view?usp=drive_link",
        "NewsName": "Incredible Surprise! Dokkan Special Missions Part 2!",
        "NewsBody": (
            "Incredible Surprise! Dokkan Special Missions Part 2 is here!\n"
            "Get rewards including Dragon Stones and '30' Special Summon Tickets!\n\n"
            "Start Date: 5/14/2024 2:00:00 AM CEST\n\n"
            "News 1\n"
            "Event Period\n"
            "Fri, 4/26 2:00 AM CEST ~ Fri, 5/31 1:59 AM CEST\n\n"
            "Incredible Surprise! Dokkan Special Missions are here!\n\n"
            "Missions from Part 2 are available starting from Tue, 5/14 CEST!\n\n"
            "Complete the Event Missions to get Dragon Stones, Potential Orbs and other rewards! You can also recruit [Mysterious Ritual] Elder Kai!\n\n"
            "A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2! The Summon Tickets can be used to perform a summon in the 'Incredible Surprise! '30' Special Summon'!\n\n"
            "In addition, the Daily Mission that allows you to recruit [Light Doze] Elder Kai (Dozing) is still available!\n\n"
            "Complete missions to obtain all the awesome rewards!\n"
            "Mission Details\n\n"
            "News 1\n"
            "* Event Missions can only be completed once.\n\n"
            "* Please go to the 'Daily Missions' and 'Event Missions' pages for more information.\n\n"
            "* Daily Missions will reset daily at 2:00 AM CEST. Please claim the rewards of the Daily Missions by 1:59 AM CEST the next day.\n\n"
            "* Daily Missions are excluded from the completion conditions of the missions 'Complete 10 or more Part 1 missions!', 'Complete all the Part 1 missions!', 'Complete 10 or more Part 2 missions!' and 'Complete all the 'Incredible Surprise! Dokkan Special Missions'!'.\n\n"
            "* 30 '30' Special Summon Tickets are required to perform a summon in the 'Incredible Surprise! '30' Special Summon'. A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2, and another 10 '30' Special Summon Tickets can be obtained upon the first login between Fri, 4/26 5:00 AM CEST and Fri, 5/31 1:59 AM CEST.\n\n"
            "* The system time is in accordance with Greenwich Mean Time.\n\n"
            "* Please note that the event content and dates are subject to change without prior warning.\n\n"
            "We hope you continue to enjoy playing Dragon Ball Z Dokkan Battle!"
        )
      },
    {
        "NewsId": 3,
        "NewsImage": "https://drive.google.com/file/d/1HUUoiMtEG3o4xAYOegJrHe-ObT6cKwlJ/view?usp=drive_link",
        "NewsImage2": "https://drive.google.com/file/d/13oiUAoglGHtsGXSvvWW8FKp9p46JMXDh/view?usp=drive_link",
        "NewsName": "Incredible Surprise! Dokkan Special Missions Part 2!",
        "NewsBody": (
            "Incredible Surprise! Dokkan Special Missions Part 2 is here!\n"
            "Get rewards including Dragon Stones and '30' Special Summon Tickets!\n\n"
            "Start Date: 5/14/2024 2:00:00 AM CEST\n\n"
            "News 1\n"
            "Event Period\n"
            "Fri, 4/26 2:00 AM CEST ~ Fri, 5/31 1:59 AM CEST\n\n"
            "Incredible Surprise! Dokkan Special Missions are here!\n\n"
            "Missions from Part 2 are available starting from Tue, 5/14 CEST!\n\n"
            "Complete the Event Missions to get Dragon Stones, Potential Orbs and other rewards! You can also recruit [Mysterious Ritual] Elder Kai!\n\n"
            "A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2! The Summon Tickets can be used to perform a summon in the 'Incredible Surprise! '30' Special Summon'!\n\n"
            "In addition, the Daily Mission that allows you to recruit [Light Doze] Elder Kai (Dozing) is still available!\n\n"
            "Complete missions to obtain all the awesome rewards!\n"
            "Mission Details\n\n"
            "News 1\n"
            "* Event Missions can only be completed once.\n\n"
            "* Please go to the 'Daily Missions' and 'Event Missions' pages for more information.\n\n"
            "* Daily Missions will reset daily at 2:00 AM CEST. Please claim the rewards of the Daily Missions by 1:59 AM CEST the next day.\n\n"
            "* Daily Missions are excluded from the completion conditions of the missions 'Complete 10 or more Part 1 missions!', 'Complete all the Part 1 missions!', 'Complete 10 or more Part 2 missions!' and 'Complete all the 'Incredible Surprise! Dokkan Special Missions'!'.\n\n"
            "* 30 '30' Special Summon Tickets are required to perform a summon in the 'Incredible Surprise! '30' Special Summon'. A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2, and another 10 '30' Special Summon Tickets can be obtained upon the first login between Fri, 4/26 5:00 AM CEST and Fri, 5/31 1:59 AM CEST.\n\n"
            "* The system time is in accordance with Greenwich Mean Time.\n\n"
            "* Please note that the event content and dates are subject to change without prior warning.\n\n"
            "We hope you continue to enjoy playing Dragon Ball Z Dokkan Battle!"
        )
      },
    {
        "NewsId": 4,
        "NewsImage": "https://drive.google.com/file/d/1HUUoiMtEG3o4xAYOegJrHe-ObT6cKwlJ/view?usp=drive_link",
        "NewsImage2": "https://drive.google.com/file/d/13oiUAoglGHtsGXSvvWW8FKp9p46JMXDh/view?usp=drive_link",
        "NewsName": "Incredible Surprise! Dokkan Special Missions Part 2!",
        "NewsBody": (
            "Incredible Surprise! Dokkan Special Missions Part 2 is here!\n"
            "Get rewards including Dragon Stones and '30' Special Summon Tickets!\n\n"
            "Start Date: 5/14/2024 2:00:00 AM CEST\n\n"
            "News 1\n"
            "Event Period\n"
            "Fri, 4/26 2:00 AM CEST ~ Fri, 5/31 1:59 AM CEST\n\n"
            "Incredible Surprise! Dokkan Special Missions are here!\n\n"
            "Missions from Part 2 are available starting from Tue, 5/14 CEST!\n\n"
            "Complete the Event Missions to get Dragon Stones, Potential Orbs and other rewards! You can also recruit [Mysterious Ritual] Elder Kai!\n\n"
            "A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2! The Summon Tickets can be used to perform a summon in the 'Incredible Surprise! '30' Special Summon'!\n\n"
            "In addition, the Daily Mission that allows you to recruit [Light Doze] Elder Kai (Dozing) is still available!\n\n"
            "Complete missions to obtain all the awesome rewards!\n"
            "Mission Details\n\n"
            "News 1\n"
            "* Event Missions can only be completed once.\n\n"
            "* Please go to the 'Daily Missions' and 'Event Missions' pages for more information.\n\n"
            "* Daily Missions will reset daily at 2:00 AM CEST. Please claim the rewards of the Daily Missions by 1:59 AM CEST the next day.\n\n"
            "* Daily Missions are excluded from the completion conditions of the missions 'Complete 10 or more Part 1 missions!', 'Complete all the Part 1 missions!', 'Complete 10 or more Part 2 missions!' and 'Complete all the 'Incredible Surprise! Dokkan Special Missions'!'.\n\n"
            "* 30 '30' Special Summon Tickets are required to perform a summon in the 'Incredible Surprise! '30' Special Summon'. A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2, and another 10 '30' Special Summon Tickets can be obtained upon the first login between Fri, 4/26 5:00 AM CEST and Fri, 5/31 1:59 AM CEST.\n\n"
            "* The system time is in accordance with Greenwich Mean Time.\n\n"
            "* Please note that the event content and dates are subject to change without prior warning.\n\n"
            "We hope you continue to enjoy playing Dragon Ball Z Dokkan Battle!"
        )
      },
    {
        "NewsId": 5,
        "NewsImage": "https://drive.google.com/file/d/1HUUoiMtEG3o4xAYOegJrHe-ObT6cKwlJ/view?usp=drive_link",
        "NewsImage2": "https://drive.google.com/file/d/13oiUAoglGHtsGXSvvWW8FKp9p46JMXDh/view?usp=drive_link",
        "NewsName": "Incredible Surprise! Dokkan Special Missions Part 2!",
        "NewsBody": (
            "Incredible Surprise! Dokkan Special Missions Part 2 is here!\n"
            "Get rewards including Dragon Stones and '30' Special Summon Tickets!\n\n"
            "Start Date: 5/14/2024 2:00:00 AM CEST\n\n"
            "News 1\n"
            "Event Period\n"
            "Fri, 4/26 2:00 AM CEST ~ Fri, 5/31 1:59 AM CEST\n\n"
            "Incredible Surprise! Dokkan Special Missions are here!\n\n"
            "Missions from Part 2 are available starting from Tue, 5/14 CEST!\n\n"
            "Complete the Event Missions to get Dragon Stones, Potential Orbs and other rewards! You can also recruit [Mysterious Ritual] Elder Kai!\n\n"
            "A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2! The Summon Tickets can be used to perform a summon in the 'Incredible Surprise! '30' Special Summon'!\n\n"
            "In addition, the Daily Mission that allows you to recruit [Light Doze] Elder Kai (Dozing) is still available!\n\n"
            "Complete missions to obtain all the awesome rewards!\n"
            "Mission Details\n\n"
            "News 1\n"
            "* Event Missions can only be completed once.\n\n"
            "* Please go to the 'Daily Missions' and 'Event Missions' pages for more information.\n\n"
            "* Daily Missions will reset daily at 2:00 AM CEST. Please claim the rewards of the Daily Missions by 1:59 AM CEST the next day.\n\n"
            "* Daily Missions are excluded from the completion conditions of the missions 'Complete 10 or more Part 1 missions!', 'Complete all the Part 1 missions!', 'Complete 10 or more Part 2 missions!' and 'Complete all the 'Incredible Surprise! Dokkan Special Missions'!'.\n\n"
            "* 30 '30' Special Summon Tickets are required to perform a summon in the 'Incredible Surprise! '30' Special Summon'. A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2, and another 10 '30' Special Summon Tickets can be obtained upon the first login between Fri, 4/26 5:00 AM CEST and Fri, 5/31 1:59 AM CEST.\n\n"
            "* The system time is in accordance with Greenwich Mean Time.\n\n"
            "* Please note that the event content and dates are subject to change without prior warning.\n\n"
            "We hope you continue to enjoy playing Dragon Ball Z Dokkan Battle!"
        )
      },
    {
        "NewsId": 6,
        "NewsImage": "https://drive.google.com/file/d/1HUUoiMtEG3o4xAYOegJrHe-ObT6cKwlJ/view?usp=drive_link",
        "NewsImage2": "https://drive.google.com/file/d/13oiUAoglGHtsGXSvvWW8FKp9p46JMXDh/view?usp=drive_link",
        "NewsName": "Incredible Surprise! Dokkan Special Missions Part 2!",
        "NewsBody": (
            "Incredible Surprise! Dokkan Special Missions Part 2 is here!\n"
            "Get rewards including Dragon Stones and '30' Special Summon Tickets!\n\n"
            "Start Date: 5/14/2024 2:00:00 AM CEST\n\n"
            "News 1\n"
            "Event Period\n"
            "Fri, 4/26 2:00 AM CEST ~ Fri, 5/31 1:59 AM CEST\n\n"
            "Incredible Surprise! Dokkan Special Missions are here!\n\n"
            "Missions from Part 2 are available starting from Tue, 5/14 CEST!\n\n"
            "Complete the Event Missions to get Dragon Stones, Potential Orbs and other rewards! You can also recruit [Mysterious Ritual] Elder Kai!\n\n"
            "A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2! The Summon Tickets can be used to perform a summon in the 'Incredible Surprise! '30' Special Summon'!\n\n"
            "In addition, the Daily Mission that allows you to recruit [Light Doze] Elder Kai (Dozing) is still available!\n\n"
            "Complete missions to obtain all the awesome rewards!\n"
            "Mission Details\n\n"
            "News 1\n"
            "* Event Missions can only be completed once.\n\n"
            "* Please go to the 'Daily Missions' and 'Event Missions' pages for more information.\n\n"
            "* Daily Missions will reset daily at 2:00 AM CEST. Please claim the rewards of the Daily Missions by 1:59 AM CEST the next day.\n\n"
            "* Daily Missions are excluded from the completion conditions of the missions 'Complete 10 or more Part 1 missions!', 'Complete all the Part 1 missions!', 'Complete 10 or more Part 2 missions!' and 'Complete all the 'Incredible Surprise! Dokkan Special Missions'!'.\n\n"
            "* 30 '30' Special Summon Tickets are required to perform a summon in the 'Incredible Surprise! '30' Special Summon'. A total of 20 '30' Special Summon Tickets can be obtained by completing certain missions from Part 1 and Part 2, and another 10 '30' Special Summon Tickets can be obtained upon the first login between Fri, 4/26 5:00 AM CEST and Fri, 5/31 1:59 AM CEST.\n\n"
            "* The system time is in accordance with Greenwich Mean Time.\n\n"
            "* Please note that the event content and dates are subject to change without prior warning.\n\n"
            "We hope you continue to enjoy playing Dragon Ball Z Dokkan Battle!"
        )
      },], safe=False)
  
def Events(request):
    return JsonResponse([{
        "EventId": 1,
        "EventName":"Extreme Z-Battle: Power Beyond the Extremes Gohan (Teen)",
        "EventType": "EXTREME Z BATTLE",
        "EventIcon": "https://drive.google.com/file/d/15le5GyIhPiY0IcjVaPNHcggQJ1ENw-ES/view?usp=drive_link",
        "EventReleaseJP": "08-05-2024",
        "EventReleaseGL": "08-05-2024",
        "EventWeakness": "Majin Buu Saga",
        "EventDetails": (
            "Challenge Gohan! Seal the victory to collect Awakening Medals!\n\n"
            "Event restrictions\n"
            "You are unable to use Dragon Stones to revive or continue if you are KO'd in the event.\n"
            "The stages cost 0 stamina until you beat them, after that they cost stamina to replay.\n"
            "You can replay stages with Keys of the Past. You will also need them when you haven't completed a stage.\n"
            "You cannot bring any Support Items or Memories.\n"
            "Characters with the same second name cannot be included on the same team.\n\n"
            "The damage threshold of 2 million for SSR icon characters starting from Level 10 means that Card 1002360 thumb will no longer be able to instantly defeat the boss with his lethal Passive Skill should it activate. Characters from the 'Worldwide Chaos' Category take less damage, mitigate Gohan's damage reduction and cause increased damage. However, they won't be able to bypass Gohan's damage reduction against specific Types.\n"
            "Note: allies that are not part of the effective Category, and are also not of the effective Type, will have to face both damage reductions.\n\n"
            "By replaying certain levels (checkpoints), you can get additional rewards:\n"
            "Level 5, 3 STA: TEQ Gohan (Teen) Bronze x1\n"
            "Level 10, 5 STA: TEQ Gohan (Teen) Bronze x2\n"
            "Level 15, 5 STA: TEQ Gohan (Teen) Silver x2\n"
            "Level 20, 7 STA: TEQ Gohan (Teen) Silver x4\n"
            "Level 25, 10 STA: TEQ Gohan (Teen) Gold x4\n"
            "Level 30, 15 STA: TEQ Gohan (Teen) Rainbow x4"
        ),
    },
    {
        "EventId": 2,
        "EventName":"Extreme Z-Battle: Power Beyond the Extremes Gohan (Teen)",
        "EventType": "EXTREME Z BATTLE",
        "EventIcon": "https://drive.google.com/file/d/15le5GyIhPiY0IcjVaPNHcggQJ1ENw-ES/view?usp=drive_link",
        "EventReleaseJP": "08-05-2024",
        "EventReleaseGL": "08-05-2024",
        "EventWeakness": "Majin Buu Saga",
        "EventDetails": (
            "Challenge Gohan! Seal the victory to collect Awakening Medals!\n\n"
            "Event restrictions\n"
            "You are unable to use Dragon Stones to revive or continue if you are KO'd in the event.\n"
            "The stages cost 0 stamina until you beat them, after that they cost stamina to replay.\n"
            "You can replay stages with Keys of the Past. You will also need them when you haven't completed a stage.\n"
            "You cannot bring any Support Items or Memories.\n"
            "Characters with the same second name cannot be included on the same team.\n\n"
            "The damage threshold of 2 million for SSR icon characters starting from Level 10 means that Card 1002360 thumb will no longer be able to instantly defeat the boss with his lethal Passive Skill should it activate. Characters from the 'Worldwide Chaos' Category take less damage, mitigate Gohan's damage reduction and cause increased damage. However, they won't be able to bypass Gohan's damage reduction against specific Types.\n"
            "Note: allies that are not part of the effective Category, and are also not of the effective Type, will have to face both damage reductions.\n\n"
            "By replaying certain levels (checkpoints), you can get additional rewards:\n"
            "Level 5, 3 STA: TEQ Gohan (Teen) Bronze x1\n"
            "Level 10, 5 STA: TEQ Gohan (Teen) Bronze x2\n"
            "Level 15, 5 STA: TEQ Gohan (Teen) Silver x2\n"
            "Level 20, 7 STA: TEQ Gohan (Teen) Silver x4\n"
            "Level 25, 10 STA: TEQ Gohan (Teen) Gold x4\n"
            "Level 30, 15 STA: TEQ Gohan (Teen) Rainbow x4"
        ),
    },
    {
        "EventId": 3,
        "EventName":"Extreme Z-Battle: Power Beyond the Extremes Gohan (Teen)",
        "EventType": "EXTREME Z BATTLE",
        "EventIcon": "https://drive.google.com/file/d/15le5GyIhPiY0IcjVaPNHcggQJ1ENw-ES/view?usp=drive_link",
        "EventReleaseJP": "08-05-2024",
        "EventReleaseGL": "08-05-2024",
        "EventWeakness": "Majin Buu Saga",
        "EventDetails": (
            "Challenge Gohan! Seal the victory to collect Awakening Medals!\n\n"
            "Event restrictions\n"
            "You are unable to use Dragon Stones to revive or continue if you are KO'd in the event.\n"
            "The stages cost 0 stamina until you beat them, after that they cost stamina to replay.\n"
            "You can replay stages with Keys of the Past. You will also need them when you haven't completed a stage.\n"
            "You cannot bring any Support Items or Memories.\n"
            "Characters with the same second name cannot be included on the same team.\n\n"
            "The damage threshold of 2 million for SSR icon characters starting from Level 10 means that Card 1002360 thumb will no longer be able to instantly defeat the boss with his lethal Passive Skill should it activate. Characters from the 'Worldwide Chaos' Category take less damage, mitigate Gohan's damage reduction and cause increased damage. However, they won't be able to bypass Gohan's damage reduction against specific Types.\n"
            "Note: allies that are not part of the effective Category, and are also not of the effective Type, will have to face both damage reductions.\n\n"
            "By replaying certain levels (checkpoints), you can get additional rewards:\n"
            "Level 5, 3 STA: TEQ Gohan (Teen) Bronze x1\n"
            "Level 10, 5 STA: TEQ Gohan (Teen) Bronze x2\n"
            "Level 15, 5 STA: TEQ Gohan (Teen) Silver x2\n"
            "Level 20, 7 STA: TEQ Gohan (Teen) Silver x4\n"
            "Level 25, 10 STA: TEQ Gohan (Teen) Gold x4\n"
            "Level 30, 15 STA: TEQ Gohan (Teen) Rainbow x4"
        ),
    },
    {
        "EventId": 4,
        "EventName":"Extreme Z-Battle: Power Beyond the Extremes Gohan (Teen)",
        "EventType": "EXTREME Z BATTLE",
        "EventIcon": "https://drive.google.com/file/d/15le5GyIhPiY0IcjVaPNHcggQJ1ENw-ES/view?usp=drive_link",
        "EventReleaseJP": "08-05-2024",
        "EventReleaseGL": "08-05-2024",
        "EventWeakness": "Majin Buu Saga",
        "EventDetails": (
            "Challenge Gohan! Seal the victory to collect Awakening Medals!\n\n"
            "Event restrictions\n"
            "You are unable to use Dragon Stones to revive or continue if you are KO'd in the event.\n"
            "The stages cost 0 stamina until you beat them, after that they cost stamina to replay.\n"
            "You can replay stages with Keys of the Past. You will also need them when you haven't completed a stage.\n"
            "You cannot bring any Support Items or Memories.\n"
            "Characters with the same second name cannot be included on the same team.\n\n"
            "The damage threshold of 2 million for SSR icon characters starting from Level 10 means that Card 1002360 thumb will no longer be able to instantly defeat the boss with his lethal Passive Skill should it activate. Characters from the 'Worldwide Chaos' Category take less damage, mitigate Gohan's damage reduction and cause increased damage. However, they won't be able to bypass Gohan's damage reduction against specific Types.\n"
            "Note: allies that are not part of the effective Category, and are also not of the effective Type, will have to face both damage reductions.\n\n"
            "By replaying certain levels (checkpoints), you can get additional rewards:\n"
            "Level 5, 3 STA: TEQ Gohan (Teen) Bronze x1\n"
            "Level 10, 5 STA: TEQ Gohan (Teen) Bronze x2\n"
            "Level 15, 5 STA: TEQ Gohan (Teen) Silver x2\n"
            "Level 20, 7 STA: TEQ Gohan (Teen) Silver x4\n"
            "Level 25, 10 STA: TEQ Gohan (Teen) Gold x4\n"
            "Level 30, 15 STA: TEQ Gohan (Teen) Rainbow x4"
        ),
    },
    {
        "EventId": 5,
        "EventName":"Extreme Z-Battle: Power Beyond the Extremes Gohan (Teen)",
        "EventType": "EXTREME Z BATTLE",
        "EventIcon": "https://drive.google.com/file/d/15le5GyIhPiY0IcjVaPNHcggQJ1ENw-ES/view?usp=drive_link",
        "EventReleaseJP": "08-05-2024",
        "EventReleaseGL": "08-05-2024",
        "EventWeakness": "Majin Buu Saga",
        "EventDetails": (
            "Challenge Gohan! Seal the victory to collect Awakening Medals!\n\n"
            "Event restrictions\n"
            "You are unable to use Dragon Stones to revive or continue if you are KO'd in the event.\n"
            "The stages cost 0 stamina until you beat them, after that they cost stamina to replay.\n"
            "You can replay stages with Keys of the Past. You will also need them when you haven't completed a stage.\n"
            "You cannot bring any Support Items or Memories.\n"
            "Characters with the same second name cannot be included on the same team.\n\n"
            "The damage threshold of 2 million for SSR icon characters starting from Level 10 means that Card 1002360 thumb will no longer be able to instantly defeat the boss with his lethal Passive Skill should it activate. Characters from the 'Worldwide Chaos' Category take less damage, mitigate Gohan's damage reduction and cause increased damage. However, they won't be able to bypass Gohan's damage reduction against specific Types.\n"
            "Note: allies that are not part of the effective Category, and are also not of the effective Type, will have to face both damage reductions.\n\n"
            "By replaying certain levels (checkpoints), you can get additional rewards:\n"
            "Level 5, 3 STA: TEQ Gohan (Teen) Bronze x1\n"
            "Level 10, 5 STA: TEQ Gohan (Teen) Bronze x2\n"
            "Level 15, 5 STA: TEQ Gohan (Teen) Silver x2\n"
            "Level 20, 7 STA: TEQ Gohan (Teen) Silver x4\n"
            "Level 25, 10 STA: TEQ Gohan (Teen) Gold x4\n"
            "Level 30, 15 STA: TEQ Gohan (Teen) Rainbow x4"
        ),
    },
    {
        "EventId": 6,
        "EventName":"Extreme Z-Battle: Power Beyond the Extremes Gohan (Teen)",
        "EventType": "EXTREME Z BATTLE",
        "EventIcon": "https://drive.google.com/file/d/15le5GyIhPiY0IcjVaPNHcggQJ1ENw-ES/view?usp=drive_link",
        "EventReleaseJP": "08-05-2024",
        "EventReleaseGL": "08-05-2024",
        "EventWeakness": "Majin Buu Saga",
        "EventDetails": (
            "Challenge Gohan! Seal the victory to collect Awakening Medals!\n\n"
            "Event restrictions\n"
            "You are unable to use Dragon Stones to revive or continue if you are KO'd in the event.\n"
            "The stages cost 0 stamina until you beat them, after that they cost stamina to replay.\n"
            "You can replay stages with Keys of the Past. You will also need them when you haven't completed a stage.\n"
            "You cannot bring any Support Items or Memories.\n"
            "Characters with the same second name cannot be included on the same team.\n\n"
            "The damage threshold of 2 million for SSR icon characters starting from Level 10 means that Card 1002360 thumb will no longer be able to instantly defeat the boss with his lethal Passive Skill should it activate. Characters from the 'Worldwide Chaos' Category take less damage, mitigate Gohan's damage reduction and cause increased damage. However, they won't be able to bypass Gohan's damage reduction against specific Types.\n"
            "Note: allies that are not part of the effective Category, and are also not of the effective Type, will have to face both damage reductions.\n\n"
            "By replaying certain levels (checkpoints), you can get additional rewards:\n"
            "Level 5, 3 STA: TEQ Gohan (Teen) Bronze x1\n"
            "Level 10, 5 STA: TEQ Gohan (Teen) Bronze x2\n"
            "Level 15, 5 STA: TEQ Gohan (Teen) Silver x2\n"
            "Level 20, 7 STA: TEQ Gohan (Teen) Silver x4\n"
            "Level 25, 10 STA: TEQ Gohan (Teen) Gold x4\n"
            "Level 30, 15 STA: TEQ Gohan (Teen) Rainbow x4"
        ),
    },])  

def EventType(request):
  return JsonResponse([{
        "EventTypeId": 1,
        "EventTypeName": "STORY",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 2,
        "EvenTypeName": "QUEST",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 3,
        "EvenTypeName": "DB STORIES",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 4,
        "EvenTypeName": "GROWTH",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 5,
        "EvenTypeName": "EXTREME Z BATTLE",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 6,
        "EvenTypeName": "LIMITED",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 7,
        "EvenTypeName": "CHALLENGE",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 8,
        "EvenTypeName": "ULTIMATE CLASH",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 9,
        "EvenTypeName": "BURST MODE",
        "EventTypeContent": [12879, 12099]
      },
    {
        "EventTypeId": 10,
        "EvenTypeName": "PETTAN BATTLE",
        "EventTypeContent": [12879, 12099]
      },], safe=False)
