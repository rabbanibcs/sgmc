from department.models import Department
from gallery.models import Carousel


def extras(request):
    departments = Department.objects.exclude(name='Other').order_by('name')
    carousel = Carousel.objects.all()

    return {'departments':departments,'carousels':carousel }