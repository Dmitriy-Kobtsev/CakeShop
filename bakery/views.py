from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bakery.forms import ProductDescriptionForm, CategoryForm, ProductForm
from bakery.models import Products, Category
from cart.forms import CartAddProductForm


class ProductView(ListView):
    model = Products
    template_name = 'bakery/index.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductView, self).get_context_data(**kwargs)
    #     context['category'] = Category.objects.all()
    #     return context


class ProductFilterView(ListView):
    model = Products
    template_name = 'bakery/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductFilterView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        print(self.category)
        return Products.objects.filter(product_category=self.category)


class ProductDetailView(DetailView):
    model = Products
    template_name = 'bakery/product_info.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('bakery:index')


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('bakery:index')

    def form_valid(self, form):
        context_data = self.get_context_data()

        if form.is_valid():
            self.object = form.save()
            return super(ProductUpdateView, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('bakery:index')



class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('bakery:index')