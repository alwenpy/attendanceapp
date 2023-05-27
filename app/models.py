from django.db import models
import datetime

class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    roll = models.IntegerField(primary_key=True)
    branch = models.CharField(max_length=50)
    course= models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    student= models.ForeignKey("Student", on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.name}    {self.subject_code}"


class TimeSlot(models.Model):
    id=models.AutoField(primary_key=True)
    start_time = models.TimeField()
    duration = models.DurationField()
    
    def __str__(self):
        return f"{self.start_time}"

class Day(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Timetable(models.Model):
    id=models.AutoField(primary_key=True)
    sid=models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    day = models.ForeignKey(Day,on_delete=models.CASCADE,null=True)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.sid}"
    
class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(default=datetime.date.today)
    roll=models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    timetable=models.ForeignKey(Timetable, on_delete=models.CASCADE,null=True)
    status=models.ForeignKey("Status", on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return f"{self.roll} - {self.timetable} - {self.status}"

class Status(models.Model):
    id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.status
    
    