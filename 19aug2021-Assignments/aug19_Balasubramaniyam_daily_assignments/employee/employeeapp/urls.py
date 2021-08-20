'''shop/register
shopname textbox
address text
email
phone text
username
password text
confrim text
register button'''
from django.urls import path,include
from .import views

urlpatterns=[
    path("emp/",views.emp,name="front"),
    path("add/",views.myEmployeePage,name="Employee"),
    path("view/",views.view,name="emolyee_details"),
    path("viewemployee/<empcode>",views.Employeedetails,name="employee_individual"),

]
'''project: notesapp 
    app:notes
    1)create a new note title,description,id,
    2)view all notes
    3)view sinle note
    4)delete note
    5)update note'''