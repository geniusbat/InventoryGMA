from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'InventoryGMA'

    
    def ready(self) -> None:
        post_migrate.connect(AutoCreateInstances,sender=self)
        return super().ready()
    
#Autocreate some categories and locations
def AutoCreateInstances(sender, **kwargs):
    from .models import Category, Location
    #Create categories
    categories = {
        "Herramienta" : {"description":"Herramientas, clavos, tornillos, etc"},
        "Tecnología" : {"description":"Componentes de pc, ratones, cables"},
        "Software" : {"description":"Software"},
        "Cocina" : {"description":"Tanto comida como utensilios de cocina"},
        "Ropa" : {"description":"Ropa y accesorios"},
        "Camping" : {"description":"Cosas de camping como mochilas, kit de primeros auxilios"},
        "Otro" : {"description":"Otros"}
    }
    for category in categories:
        if not Category.objects.filter(name=category).exists():
            instance = Category(name=category, description=categories[category]["description"])
            instance.save()
    
    #Create locations
    locations = {
        "Casa" : {"description":"Está en algún lugar de tu casa"},
        "Trastero" : {"description":"Está en el trastero"},
        "Perdido" : {"description":"No sé donde está"},
        "Huetor" : {"description":"Está en Huetor Tajar"}
    }
    for location in locations:
        if not Location.objects.filter(name=location).exists():
            instance = Location(name=location, description=locations[location]["description"])
            instance.save()
        
