from django.http import JsonResponse

from .models import Noticia


def eliminar_noticia(request):
    pk = request.POST.get('pk')
    noticia = Noticia.objects.get(pk=pk)
    noticia.delete()
    response = {}
    return JsonResponse(response)