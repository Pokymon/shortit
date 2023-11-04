from django.shortcuts import render, redirect, Http404
from .models import ShortenedURL
from .forms import URLForm
from .utils import generate_short_id

def shorten_url(request):
    short_url = None
    error = None
    form = URLForm(request.POST or None)
    
    if form.is_valid():
        url = form.cleaned_data['url']
        short_id = generate_short_id()
        shortened_url_obj, created = ShortenedURL.objects.get_or_create(
            original_url=url, defaults={'short_id': short_id}
        )
        short_url = request.build_absolute_uri(shortened_url_obj.get_absolute_url())
    else:
        error = "Invalid URL. Please enter a valid URL and try again."
    
    return render(request, 'index.html', {'form': form, 'short_url': short_url, 'error': error})

def redirect_view(request, short_id):
    try:
        shortened_url_obj = ShortenedURL.objects.get(short_id=short_id)
        return redirect(shortened_url_obj.original_url)
    except ShortenedURL.DoesNotExist:
        raise Http404("Shortened URL not found")
