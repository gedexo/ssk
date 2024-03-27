from .models import Category

def main_context(request):
    context = {"all_categories": Category.objects.all()}
    return context