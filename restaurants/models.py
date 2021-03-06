from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL


class TodoQuerySet(models.query.QuerySet):
    def search(self, query): #RestaurantLocation.objects.all().search(query) #RestaurantLocation.objects.filter(something).search()
        if query:
            query = query.strip()
            return self.filter(
                Q(name__icontains=query)|
                Q(timestamp__icontains=query)    
                ).distinct()
        return self


class TodoManager(models.Manager):
    def get_queryset(self):
        return TodoQuerySet(self.model, using=self._db)

    def search(self, query): #RestaurantLocation.objects.search()
        return self.get_queryset().search(query)


class Todo(models.Model):
    owner           = models.ForeignKey(User) # class_instance.model_set.all() # Django Models Unleashed JOINCFE.com
    name            = models.CharField(max_length=120)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(null=True, blank=True)
    #my_date_field   = models.DateField(auto_now=False, auto_now_add=False)

    objects = TodoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}" 
        return reverse('detailt', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name


def todo_pre_save_receiver(sender, instance, *args, **kwargs):
    
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(todo_pre_save_receiver, sender=Todo)





