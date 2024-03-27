from django.shortcuts import render

from django.http import JsonResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView

from .models import Product,Category,Testimonial,Updates,ClientLogo,Organization
from .forms import ContactForm,ProductEnquiryForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'web/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["testimonials"] = Testimonial.objects.all()
        context["updates"] = Updates.objects.all()[:3]
        context["clients"] = ClientLogo.objects.all()  
        context["organizations"] = Organization.objects.all()
        context["is_index"] = True
        return context
    
    
class AboutView(TemplateView):
    template_name = 'web/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] =  ClientLogo.objects.all()
        context["categories"] = Category.objects.all() 
        
        return context
    
    
class ContactView(FormView):
    form_class = ContactForm
    template_name = "web/contact.html"

    def form_valid(self, form):
        form.save()

        response_data = { "status": "true","title": "Thankyou for your quirey submitted","message": "our team will revert to you at the earliest ",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)
    

class UpdatesView(ListView):
    model = Updates
    template_name = 'web/updates.html'
    
class UpadateDetailView(DetailView):
    model = Updates
    template_name = 'web/update_detail.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        current_update = self.get_object()
        context["updates"] = Updates.objects.exclude(pk=current_update.pk).order_by("-id")
        return context
    
    
    
class ProductListView(ListView,FormView):
    model = Product
    form_class = ProductEnquiryForm
    template_name = "web/product.html"
    paginate_by=20
    
    def get_queryset(self):
        category = self.request.GET.get("category")
        products = super().get_queryset()  # Retrieve the base queryset
        
        if category:
            products = products.filter(category__id=category)
            
        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all() 
        return context
    
    
    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Successfully submitted","message": "our team will revert to you at the earliest ",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)
    
    
