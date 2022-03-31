from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
#fonction qui permet d'ajouter et afficher les etudiants
def addView(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['nom']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(nom = nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
        
    return render(request, 'student/addView.html', {'form':fm, 'stud':stud})

#fonction qui permet de modifier

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
            pi = User.objects.get(pk=id)
            fm = StudentRegistration(instance=pi)
    return render(request, 'student/updateStudent.html', {'form':fm})

#fonction qui permet de supprimer

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
