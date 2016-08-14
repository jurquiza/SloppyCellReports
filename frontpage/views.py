from django.shortcuts import render


# Create your views here.

def main_page(request):
	return render(request, 'frontpage/main_page.html',{})
    
def about(request):
	return render(request, 'frontpage/about.html',{})


