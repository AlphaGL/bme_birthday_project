from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentBirthdayForm

def birthday_form(request):
    if request.method == 'POST':
        form = StudentBirthdayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '🎉 Thank you for submitting! We celebrate you in advance! 🎊❤')
            return redirect('birthday_success')
    else:
        form = StudentBirthdayForm()
    
    return render(request, 'birthdays/form.html', {'form': form})

def birthday_success(request):
    return render(request, 'birthdays/success.html')

@login_required
def admin_dashboard(request):
    students = Student.objects.all()
    
    # Filter by month
    month_filter = request.GET.get('month')
    if month_filter:
        students = students.filter(birth_month=month_filter)
    
    # Search
    search = request.GET.get('search')
    if search:
        students = students.filter(full_name__icontains=search)
    
    # Pagination
    paginator = Paginator(students, 12)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    
    context = {
        'students': students,
        'total_students': Student.objects.count(),
        'month_filter': month_filter,
        'search': search
    }
    return render(request, 'birthdays/admin_dashboard.html', context)

@login_required
def admin_create(request):
    if request.method == 'POST':
        form = StudentBirthdayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('admin_dashboard')
    else:
        form = StudentBirthdayForm()
    
    return render(request, 'birthdays/admin_form.html', {'form': form, 'action': 'Create'})

@login_required
def admin_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentBirthdayForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = StudentBirthdayForm(instance=student)
    
    return render(request, 'birthdays/admin_form.html', {
        'form': form,
        'action': 'Update',
        'student': student
    })

@login_required
def admin_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('admin_dashboard')
    
    return render(request, 'birthdays/admin_confirm_delete.html', {'student': student})