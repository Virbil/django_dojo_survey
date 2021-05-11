from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        context = {
            "name": request.POST["name_of_surveyor"],
            "dojo_location": request.POST['dojo_location'],
            "fav_coding_language": request.POST['fav_coding_language'],
            "comments": request.POST["comment"]
        }

    return render(request, "results.html", context)


#     http://localhost:8000 - have this display a nice looking HTML form.  
#       The form should be submitted to '/result'

#     http://localhost:8000/result - have this display a html template with 
#       the information that was submitted by POST