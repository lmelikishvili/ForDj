from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    context = {}
    list_of_values = [
        "Levani",
        "Melikishvili",
        33
    ]
    context['list_content'] = list_of_values

    return render(request, 'personal/home.html', context)
