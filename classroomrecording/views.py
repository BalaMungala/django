from django.shortcuts import render
import datetime
from classroomrecording.models import Employee


# Create your views here.


def employee_info_view(request):
	employees=Employee.objects.all()
	return render(request,'testapp/classrecording.html',context={'employees':employees})

def add_movieform_submission(request):
	employee=Employee(1,23,234,23)
	employee.save()
	return render(request,'testapp/classrecording.html')
	
	
