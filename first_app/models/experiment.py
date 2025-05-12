from django.db import models

class MyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        app_label = 'first_app'


class Experiment(MyBaseModel):

    field_1=models.CharField(max_length=100)
    field_2=models.CharField(max_length=100)
    field_3=models.CharField(max_length=100)



    class Meta:
        verbose_name='My Experiment'
        verbose_name_plural='My Experiments'
        managed = False


class Experiment2(MyBaseModel):
    class Meta:
        get_latest_by = 'created_at'
        # get_latest_by = 'updated_at'


class PublishedQuerySet(models.QuerySet):
    def published(self):
        self.filter(status=1)

    def recent(self):
        return self.order_by('-created_at')[:5]


class ArticleManager(models.Manager):
    def get_queryset(self):
        return PublishedQuerySet(self.model, using=self._db)

    def published(self):
       # return self.get_queryset().filter(status=1)
        return self.get_queryset().published()
        #return self.get_queryset()



class Article(MyBaseModel):
    STATUS_CHOICES=((-1, 'Draft'), (0, 'Not Published'), (1, 'Published'))


    title=models.CharField(max_length=50)
    content=models.TextField()
    status=models.IntegerField(choices=STATUS_CHOICES, default=0)


    objects=ArticleManager()

    def __repr__(self):
        return f'{self.title} {self.status}'
