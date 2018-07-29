from django.http import Http404


def get_single_object(idx, obj_type):
    """
    Return a QuerySet object
    :param idx: Object ID
    :param obj_type: The Queryset Class
    :return: Queryset object
    """
    try:
        return obj_type.objects.get(id=idx)
    except obj_type.DoesNotExist:
        raise Http404
