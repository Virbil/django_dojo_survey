from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == "POST":
        request.session['name'] = request.POST["name_of_surveyor"].title()
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['fav_coding_language'] = request.POST['fav_coding_language']
        request.session['comments'] = request.POST["comment"]   
        print(request.session.__dict__)
        
        return redirect('/show-results')
    else:
        return redirect('/')

def show_results(request):
    return render(request, "results.html")