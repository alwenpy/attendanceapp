from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=50)
    course= models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}    {self.subject_code}"


class TimeSlot(models.Model):
    start_time = models.TimeField()
    duration = models.DurationField()
    
    def __str__(self):
        return f"{self.start_time}"

class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Timetable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    days = models.ManyToManyField(Day)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.subject} - {', '.join(str(day) for day in self.days.all())} ({self.time_slot})"