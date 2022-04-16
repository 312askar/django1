from .models import RegulatTour

def minus_place_count(pk, count):
    try:
        regular = RegulatTour.objects.get(id=pk)
        regular.places_count -= count
        regular.save()
        return True
    except RegulatTour.DoesNotExist:
        return False
