from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import *
from datetime import datetime

# Create your views here.
def post_list(request):
    return render_to_response("producto_list.html", {
        'time':datetime.now(),
        }, context_instance=RequestContext(request))

def post_list(request):
		productos=Productos.objects.filter(nombre__contains='').order_by()
		return render(request, 'pagina/producto_list.html', {'productos':productos})

def post_detail(request, pk):

        producto = get_object_or_404(Productos, pk=pk)
        return render(request, 'pagina/producto_detail.html', {'producto': producto})
        