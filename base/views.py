from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctors, Patients, Appointments
from .forms import DoctorsModelForm, PatientsModelForm, AppointmentsModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
''' Appointments CRUD operations '''
@login_required(login_url='signin')
def create_appoint(request):
    form = AppointmentsModelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('display_appoint')
    return render(request, 'create_appoint.html', {'form':form})

@login_required(login_url='signin')
def display_appoint(request):
    # restricting the access of other user's details by only accessing the active/current user's details
    data = Appointments.objects.filter(user = request.user)
    return render(request, 'display_appoint.html', {'data':data})

@login_required(login_url='signin')
def update_appoint(request, aid):
    record = get_object_or_404(Appointments, id = aid)
    form = AppointmentsModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('display_appoint')
    return render(request, 'update_appoint.html', {'form':form})

@login_required(login_url='signin')
def delete_appoint(request, aid):
    record = get_object_or_404(Appointments, id = aid)
    if request.method == 'POST':
        record.delete()
        return redirect('display_appoint')
    return render(request, 'delete_appoint.html')

#doctors model crud operation 

@login_required(login_url="signin")
def create(request):
    form = DoctorsModelForm(request.POST, request.FILES)
    if form.is_valid():
        record = form.save(commit=False)
        record.user = request.user
        record.save
        return redirect('read')
    return render(request, 'create.html',{'form':form})

@login_required(login_url='signin')
def read(request):
    data = doctors.object.filter(is_deleted=False)
    return render(request, 'read.html',{'data':data})

@login_required(login_url='signin')
def update(request,did):
    record = get_object_or_404(Doctors, id=did)
    form = DoctorsModelForm(request.POST, request.FILES, instance=record)
















''' Patient's CRUD Operations '''
# create operation
@login_required(login_url='signin')
def create_patients(request):
    # creating an object for the PatientsModelForm to collect the details submitted from the form. If form is submitted, details will be stored else empty form will be stored.
    form = PatientsModelForm(request.POST, request.FILES)

    # is_valid is an inbuilt function which will check whether all the values are validated or not.
    if form.is_valid():
        # will insert all the validated data as a record into the connected Model
        form.save()
        # once after submitting the form, the control will be re-directed towardws the display page using redirect() --> redirect('url_name')
        return redirect('display_pat')
    # if the form is not submitted, then we have to display the form for the user in the browser, hence we have to pass the empty form as a context
    return render(request, 'create_patients.html', {'form':form})

# read operation
@login_required(login_url='signin')
def display_patients(request):
    records = Patients.objects.all()
    return render(request, 'display_patients.html', {'data':records})

# update operation
@login_required(login_url='signin')
def update_patients(request, pid):
    # fetch the particular record to update in the Model
    record = get_object_or_404(Patients, id = pid)
    # collect the data from the form and display the default value as of the fetched record --> instance = record
    form = PatientsModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('display_pat')
    return render(request, 'update_patients.html', {'form':form})

# delete operation
@login_required(login_url='signin')
def delete_patients(request, pid):
    # fetch the particular record to delete from the model
    record = get_object_or_404(Patients, id = pid)
    if request.method == "POST":
        # delete the record
        record.delete()
        return redirect('display_pat')
    return render(request, 'delete_patients.html', {'data':record})































''' Doctor's Model CRUD Operations '''
@login_required(login_url='signin')
def create(request):
    form = DoctorsModelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=True)
        return redirect('read')
    return render(request, 'create.html', {'form':form})

@login_required(login_url='signin')
def read(request):
    data = Doctors.objects.all()
    return render(request, 'read.html', {'data':data})

@login_required(login_url='signin')
def update(request, did):
    record = get_object_or_404(Doctors, id = did)
    form = DoctorsModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'update.html', {'form':form})

@login_required(login_url='signin')
def delete(request, did):
    record = get_object_or_404(Doctors, id = did)
    if request.method == 'POST':
        record.delete()
        return redirect('read')
    return render(request, 'delete.html', {'data':record})
