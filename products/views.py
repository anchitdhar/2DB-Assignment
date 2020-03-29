from django.shortcuts import render,redirect
from products.models import Product
# from django.contrib.auth.decorators import login_required
from products.forms import ProductForm

def ProductView(request):
    form = Product.objects.all()
    return render(request, 'posts.html', {'form': form})
    
def ProductAdd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = ProductForm()
    return render(request,'postupload.html',{'form':form})