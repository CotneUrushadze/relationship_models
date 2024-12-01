from typing import Any
from django.core.management.base import BaseCommand
from django.db.models import (
    Count,
    Max,
    Min,
    Avg,
    Sum,
    Q,
    F
)
from shop.models import Tag, Category, Item



class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
      
    #     total_sum = Item.objects.aggregate(total_sum = Sum('price'))
    #     print(total_sum)
        
    #     avrage_price = Item.objects.aggregate(avrage_price = Avg('price'))
    #     print(avrage_price)
        
    #     min_max_price = Item.objects.aggregate(min_price = Min('price'), max_price = Max('price'))
    #     print(min_max_price)
        
    #     description_count = Item.objects.aggregate(count = Count('description'))
    #     print(description_count)
        
        # categories = Category.objects.annotate(items_count = Count('items'))
        # for category in categories:
        #     print(f"{category.name} : {category.items_count}")
            
        
        # categories = Category.objects.annotate(items_avg_price = Avg('items__price', default = 0) )
        # for category in categories:
        #     print(f"{category.name} : {category.items_avg_price}")
            
            
        # categories = Category.objects.annotate(
        #     min_price = Min('items__price', default=0),
        #     max_price = Max('items__price', default=0)
        # )
            
        # for category in categories:
        #     print(f"{category.name} : Min price : {category.min_price}, Max ptrice: {category.max_price}")
   
   
   
   
   
   
   
   
   
   
        
# #N1        
#         categories = Category.objects.annotate(tags_count=Count('items__tags'))
#         for category in categories:
#             print(f"{category.name} : {category.tags_count}")
            
            
            
# #N2
#         categories = Category.objects.annotate(expensive=Max('items__price'))
#         for category in categories:
#             print(f"{category.name} : {category.expensive}")   
            
            
            
# #N3
#         categories = Category.objects.annotate(cheap=Min('items__price'))
#         for category in categories:
#             print(f"{category.name} : {category.cheap}")
        
        
        
# #N4
#         products = Category.objects.aggregate(cheap=Min('items__price'),
#                                                 avrage=Avg('items__price'),
#                                                 expensive=Max('items__price'),
#                                                 summ=Sum('items__price'))
#         for product in products:
#             print(products)
        
        

        categories = Category.objects.annotate(cheap=Min('items__price'))
        for category in categories:
            print(f"{category.name} : {category.cheap}")