from django.shortcuts import render,redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import *
import datetime
import json
import pytz

IST = pytz.timezone('Asia/Kolkata')
weekday = datetime.date.today().weekday()
# weekday returns 0 for Monday and 6 for Sunday
# We have 1 as Monday and 7 as Sunday in database
# So, we do this
weekday = weekday+1

def index(request):
    sub = Subject.objects.all()
    
    # Change this to only for student's subjects
    time_table = Timetable.objects.filter(day_id=weekday).all()
    attendances = Attendance.objects.filter(date=datetime.date.today()).all()
    marked = [a.timetable.id for a in attendances]
    holiday_avl = True
    if len(marked) >0:
        holiday_avl = False
    for t in time_table:
        if t.id in marked:
            t.marked = True
            t.status = Attendance.objects.get(date=datetime.date.today(), timetable_id=t.id).status
        else:
            t.marked = False


    context = { "sub_list": sub, "today": datetime.date.today().strftime("%A, %d %B %Y"), "time_table" : time_table, "holiday_avl": holiday_avl}
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


def holiday(request):
    tt = Timetable.objects.filter(day_id=weekday).all()
    for t in tt:
        Attendance.objects.create(
            date=datetime.date.today(),
            timetable_id=t.id,
            status_id=3 # 3 is for holiday
        )
    return redirect("/")

@csrf_exempt
def mark_attendance_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
    
        Attendance.objects.create(
            date=datetime.date.today(),
            timetable_id=data['tt_id'],
            status_id=data['status']
        )
        return HttpResponse(status=200)
    return HttpResponse(status=400)

def report(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    time_table = Timetable.objects.filter(sid_id=subject_id).all()

    attendances = Attendance.objects.filter(timetable__in=time_table).all()
    total=0
    present=0
    absent=0
    holiday=0
    percentage = 0
    to_75 = 0
    to_60 = 0
    for a in attendances:
        total+=1
        if a.status_id==1:
            present+=1
        elif a.status_id==2:
            absent+=1
        elif a.status_id==3:
            holiday+=1
    if total>0:
        percentage = (present/total)*100
        percentage = round(percentage, 2)
        to_75 = (0.75*total - present)/0.25
        to_60 = (0.60*total - present)/0.40
    context = {"attendances" : attendances,"subject":subject, "time_table":time_table, "to_75": to_75, "to_60": to_60, "total": total, "present": present, "absent": absent, "holiday": holiday, "percentage": percentage}
    return render(request, "report.html", context=context)