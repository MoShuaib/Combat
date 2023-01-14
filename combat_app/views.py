from django.shortcuts import render
from django.http import HttpResponse
from combat_app.models import Promoter, Sanctioning, Medics, Fighter, Gym_Owner, Coach, Event_Calendar
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    return render(request, "index.html")


def fighter(request):
    if request.method == "POST":
        if request.POST.get['roles']:
            fnm = request.POST["fname"]
            lnm = request.POST["lname"]
            profile = request.FILES["profile"]
            em = request.POST["email"]
            cont = request.POST["contact"]
            gen = request.POST["gender"]
            dy = request.POST["date"]
            mon = request.POST["month"]
            yer = request.POST["year"]
            cit = request.POST["city"]
            tow = request.POST["town"]
            cntry = request.POST["country"]
            docs = request.FILES["document"]
            passw = request.POST["password"]
            fight_name = request.POST["fight_name"]
            fight_weight = request.POST["fight_weight"]
            
            wight_units = request.POST["wight_units"]
            fight_height = request.POST["fight_height"]
            height_units = request.POST["height_units"]
            gym_name = request.POST["gym_name"]
            data = Fighter(fname=fnm, lname=lnm, profile=profile, email=em, contact=cont, gender=gen, date=dy, month=mon, year=yer, city=cit, town=tow,
                           country=cntry, document=docs, password=passw, fight_name=fight_name, fight_weight=fight_weight, wight_units=wight_units, fight_height=fight_height,
                           height_units=height_units, gym_name=gym_name)
            data.save()
            return HttpResponse("<h1 style='color:green;'>Data Saved Successfully!</h1>")

    return render(request, "fighter.html")
 
def additional(request):
    return render(request, "additional.html")


def register(request):
    
    if request.method == "POST":
        # if request.POST.get['roles']:
            fnm = request.POST["fname"]
            lnm = request.POST["lname"]
            profile = request.FILES["profile"]
            em = request.POST["email"]
            cont = request.POST["contact"]
            gen = request.POST["gender"]
            dy = request.POST["date"]
            mon = request.POST["month"]
            yer = request.POST["year"]
            cit = request.POST["city"]
            tow = request.POST["town"]
            cntry = request.POST["country"]
            docs = request.FILES["document"]
            passw = request.POST["password"]

            usr = User.objects.create_user(fnm, lnm, em)
            usr.first_name= fnm
            usr.last_name = lnm
            usr.email = em
            usr.save()

            # if request.get["sanctioning"]:
            data = Sanctioning(fname=fnm, lname=lnm, profile=profile, email=em, contact=cont, gender=gen,
                                date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry, document=docs, password=passw)
            data.save()
            return render(request, "register.html", {"status":"{} Account Created Successfuly". format(fnm)})
            

            # if request.get["promoter"]:
            #     data = Promoter(fname=fnm, lname=lnm, email=em, contact=cont, gender=gen,
            #                     date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry)
            #     data.save()

            # if request.get["medics"]:
            #     data = Medics(fname=fnm, lname=lnm, email=em, contact=cont, gender=gen,
            #                   date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry)
            #     data.save()

            # if request.get["gym_owner"]:
            #     data = Gym_Owner(fname=fnm, lname=lnm, email=em, contact=cont, gender=gen,
            #                      date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry)
            #     data.save()

            # if request.get["coach"]:
            #     data = Coach(fname=fnm, lname=lnm, profile=profile, email=em, contact=cont,
            #                  gender=gen, date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry)
            #     data.save()


    return render(request, "register.html")


def profile(request):
    prof = Fighter.objects.all()

    return render(request, "profile.html", {'profile':prof})

def prac(request):
    data_save  = Sanctioning.objects.all()
    print(data_save)
    return render(request, "prac.html", {'all':data_save})


def edit_profile(request):
    return render(request, "edit_profile.html")

def events(request):
    prof = Fighter.objects.all()
    event = Event_Calendar.objects.all()
    return render(request, "events.html", {'eve': event, 'fight':prof})