from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'App Name' : 'Toko Messi Indah',
        'Name' : 'Theodore Kevin Himawan',
        'Class': 'PBP F',
        'Product Name' : 'Messi Barcelona Jersey',
        'Price' : '5000000',
        'Description': 'A brand new Barcelona jersey of legendary player Lionel Messi',
        'Category': 'Jersey',

    }

    return render(request, "main.html", context)
