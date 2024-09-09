from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Toko Messi Indah',
        'name' : 'Theodore Kevin Himawan',
        'class': 'PBP F',
        'product_name' : 'Messi Barcelona Jersey',
        'price' : '5000000',
        'description': 'A brand new Barcelona jersey of legendary player Lionel Messi',
        'category': 'Jersey',

    }

    return render(request, "main.html", context)
