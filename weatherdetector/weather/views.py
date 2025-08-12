from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Handle form submission if needed
        city = request.POST['city']
    return render(request, 'index.html')  # Render the index template