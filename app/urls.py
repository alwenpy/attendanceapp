from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("add-subject", views.add_subject, name="add_subject"),
    path("time-table", views.time_table, name="timetable"),
    path("holiday", views.holiday, name="holiday"),
    path("mark-attendance", views.mark_attendance_ajax, name="mark_attendance_ajax"),
    path("report/<subject_id>", views.report, name="attendance"),
]