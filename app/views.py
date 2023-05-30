from django.shortcuts import render,redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import *
import datetime
import json


def index(request):
    sub = Subject.objects.all()
    weekday = datetime.date.today().weekday()
    # weekday returns 0 for Monday and 6 for Sunday
    # We have 1 as Monday and 7 as Sunday in database
    # So, we do this
    weekday = weekday+1
    # Change this to only for student's subjects
    time_table = Timetable.objects.filter(day_id=weekday).all()


    context = { "sub_list": sub, "today": datetime.date.today().strftime("%A, %d %B %Y"), "time_table" : time_table}
    return render(request,"index.html" , context=context)


def add_subject(request):
    if request.method == "POST":
        name = request.POST["sub_name"]
        code = request.POST["sub_code"]
        Subject.objects.create(name=name, subject_code=code)
        return redirect("/")
    return render(request, "add-sub.html")
    

@csrf_exempt
def time_table(request):
    if request.method=='POST':
        data = json.loads(request.POST['data'])
        for d in data:
            
            d['day_id'] = int(d['day_id'])
            d['time_slot_id'] = int(d['slot_id'])

            if not(d['subject_id']):
                d['subject_id'] = None
            else:
                d['subject_id'] = int(d['subject_id'])
            
            Timetable.objects.create(
                sid_id = d['subject_id'],
                day_id = d['day_id'],
                time_slot_id = d['slot_id']
            )
        return HttpResponse(status=200)

    sub = Subject.objects.all()
    # Change this to user's subjects
    days = Day.objects.all()
    slots = TimeSlot.objects.all()
    context = {"sub": sub, "days": days, "slots" : slots}
    return render(request, "time-table.html", context=context)