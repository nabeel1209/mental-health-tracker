from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275166',
        'name': 'Nabeel Muhammad',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
