#from first_app.models import *
#did not react to the first_app import
from django.db.models import Count, Value, CharField

from first_app.models import Article, Department, Position


def examples():
    articles=Article.objects.filter(status__lte=1)
    #articles=Article.objects.filter(status__gte=-1)
    print(articles)

    non_draft_articles=Article.objects.exclude(status=-1)

    active_position=Department.objects.annotate(num_positions=Count('position'))
    #active_position=active_position.annotate(position = Value('position', output_field=CharField()))



    departments=list(active_position)
    # acticles_ordered=list(Article.objects.order_by('title'))
    #unique_positions=Position.objects.distinct('title')
    first_art=Article.objects.first()
    last_art=Article.objects.last()
    #pub = Article.objects.published().exists()

    for a in Article.objects.iterator():
        print(a)

    positions = list(Position.objects.all())
    for p in positions:
        print(p.department.name)

    positions = list(Position.objects.select_related('department'))

    return




if __name__=="__main__":
    examples()