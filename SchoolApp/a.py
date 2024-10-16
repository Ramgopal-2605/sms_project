import datetime
from tokenize import Token
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.db.models import Avg
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def admin_registration(request):
    if request.method == 'POST':
        admin_name = request.POST.get('admin_name')
        admin_id = request.POST.get('admin_id')
        admin_pwd = request.POST.get('admin_pwd')

        # Check if admin ID already exists
        if AdminPrincipalRegistration.objects.filter(Adminid=admin_id).exists():
            return HttpResponse("Admin ID already exists. Please choose a different ID.")

        # Create a new admin registration entry
        new_admin = AdminPrincipalRegistration(
            AdminName=admin_name,
            Adminid=admin_id,
            pwd=admin_pwd  # Hash the password before saving
        )
        new_admin.save()  # Save the admin instance

        # Create a token for the new admin
        token, created = Token.objects.get_or_create(user=new_admin)

        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'admin_registration.html')

def login_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        
        # Check for Admin
        try:
            admin = AdminPrincipalRegistration.objects.get(Adminid=user_id, pwd=password)
            request.session['user_type'] = 'admin'
            request.session['user_id'] = admin.Adminid
            print(request.session.get('user_id')) 
            return redirect('admin_dashboard')  # Redirect to admin dashboard

        except AdminPrincipalRegistration.DoesNotExist:
            pass  # Continue to check for student or staff

        # Check for Student
        try:
            student = StudentEnrollment.objects.get(student_id=user_id, student_pwd=password)
            request.session['user_type'] = 'student'
            request.session['user_id'] = student.student_id
            print(request.session.get('user_id')) 
            return redirect('student_dashboard')  # Redirect to student dashboard

        except StudentEnrollment.DoesNotExist:
            pass  # Continue to check for staff

        # Check for Staff
        try:
            staff = StaffEnrollment.objects.get(staff_id=user_id, staff_pwd=password)
            request.session['user_type'] = 'staff'
            request.session['user_id'] = staff.staff_id
            print(request.session.get('user_id'))  # Should print the logged-in staff ID
            return redirect('staff_dashboard')  # Redirect to staff dashboard

        except StaffEnrollment.DoesNotExist:
            return HttpResponse("Invalid credentials. Please try again.")

    return render(request, 'login.html')

def admin_dashboard(request):
        # Check if the user is logged in via session
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'admin':
        messages.error(request, "Please log in to access the dashboard.")
        return redirect('login')
    try:
        # Get the staff member using the user_id from the session
        admin = AdminPrincipalRegistration.objects.get(Adminid=user_id)
    except AdminPrincipalRegistration.DoesNotExist:
        messages.error(request, "Admin is not found.")
        return redirect('login')
    
    # Retrieve data for the admin dashboard
    total_students = StudentProfile.objects.count()
    total_staff = StaffProfile.objects.count()
    total_classes = Class.objects.count()
    total_events = Event.objects.count()
    notifications = Notification.objects.all()[:5]  # Get the latest 5 notifications

    return render(request, 'admin_dashboard.html', {
        'total_students': total_students,
        'total_staff': total_staff,
        'total_classes': total_classes,
        'total_events': total_events,
        'notifications': notifications,
    })

def staff_dashboard(request):
    # Check if the user is logged in via session
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'staff':
        messages.error(request, "Please log in to access the dashboard.")
        return redirect('login')

    try:
        # Get the staff member using the user_id from the session
        staff = StaffEnrollment.objects.get(staff_id=user_id)
    except StaffEnrollment.DoesNotExist:
        messages.error(request, "Staff member not found.")
        return redirect('login')
    print(f"Staff ID: {staff.staff_id}")  # Debugging line

    # Retrieve notifications
    notifications = Notification.objects.all()[:5]
    assigned_subject = staff.subject_assigned
    return render(request, 'staff_dashboard.html', {
        'staff': staff,
        'notifications': notifications,
        'assigned_subject': assigned_subject,
    })
def student_urls(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'student':
        return redirect('login')

    # Here, you can fetch the student details if needed
    student_id = request.user.id # Assuming the session stores the student ID directly

    return render(request, 'all_student_urls.html', {'student_id': student_id})

def staff_urls(request):
    # Check if the user is logged in via session
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'staff':
        messages.error(request, "Please log in to access this page.")
        return redirect('login')

    try:
        # Get the staff member using the user_id from the session
        staff = StaffEnrollment.objects.get(staff_id=user_id)
    except StaffEnrollment.DoesNotExist:
        messages.error(request, "Staff member not found.")
        return redirect('login')

    staff_id = staff.staff_id
    class_id = staff.class_id if hasattr(staff, 'class_id') else None
    subject_id = staff.subject_assigned if hasattr(staff, 'subject_assigned') else None

    # Add additional checks or logic to ensure class_id is set correctly

    return render(request, 'staff_urls.html', {
        'staff_id': staff_id,
        'class_id': class_id,
        'subject_id': subject_id,
    })
    
def student_dashboard(request):
    # Attempt to retrieve the student profile
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')
    
    if not user_id or user_type != 'student':
        messages.error(request, "Please log in to access the dashboard.")
        return redirect('login')

    try:
        student = StudentEnrollment.objects.get(student_id=user_id)
    except StudentEnrollment.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

    # Retrieve the latest notifications
    notifications = Notification.objects.all()[:5]
    
    # Retrieve enrolled class
    enrolled_class = student.class_assigned


    return render(request, 'student_dashboard.html', {
        'student': student,
        'notifications': notifications,
        'enrolled_class': enrolled_class,
    })
    
    
def enroll_student_view(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        student_pwd = request.POST.get('student_pwd')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        class_assigned_id = request.POST.get('class_assigned')
        fee_details = request.POST.get('fee_details')
        date_of_birth = request.POST.get('date_of_birth')  # Make sure to capture this if needed
        address = request.POST.get('address')  # Capture the address if needed
        contact_number = request.POST.get('contact_number')  # Capture the contact number if needed
        image = request.FILES.get('image')  # Handle file upload for the image

        # Create a new StudentEnrollment instance
        new_student = StudentEnrollment(
            student_name=student_name,
            student_id=student_id,
            student_pwd=student_pwd,
            father_name=father_name,
            mother_name=mother_name,
            class_assigned_id=class_assigned_id,
            enrollment_date=timezone.now(),
            fee_details=fee_details
        )
        new_student.save()
        
        # Create a new StudentFee instance for the newly enrolled student
        StudentFee.objects.create(
            student=new_student,
            amount_due=fee_details,  # Assuming the fee_details is the amount due
            amount_paid=0.00,  # Initial payment is zero
            installments=1,  # You can modify this according to your logic
            due_date=timezone.now()  # Set the due date as needed
        )

        # Create a new StudentProfile instance linking to the new StudentEnrollment
        StudentProfile.objects.create(
            enrollment=new_student,
            date_of_birth=date_of_birth,
            address=address,
            image=image,
            contact_number=contact_number
        )

        return redirect('admin_dashboard')  # Redirect to admin dashboard after enrollment

    classes = Class.objects.all()  # Get all classes for the dropdown
    return render(request, 'enroll_student.html', {'classes': classes})

def enroll_staff_view(request):
    if request.method == 'POST':
        staff_name = request.POST.get('staff_name')
        staff_id = request.POST.get('staff_id')
        staff_pwd = request.POST.get('staff_pwd')
        subject_assigned_id = request.POST.get('subject_assigned')
        date_of_hire = request.POST.get('date_of_hire')
        designation = request.POST.get('designation')
        category = request.POST.get('category')  # This should be a boolean value
        experience_in_years = request.POST.get('experience_in_years')
        image = request.FILES.get('image')  # Use request.FILES for file uploads
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        married_status = request.POST.get('married_status') == 'true'  # Convert string to boolean
        salary = request.POST.get('salary')

        # Create a new StaffEnrollment instance
        new_staff = StaffEnrollment(
            staff_name=staff_name,
            staff_id=staff_id,
            staff_pwd=staff_pwd,
            subject_assigned_id=subject_assigned_id,
            date_of_hire=date_of_hire,
            designation=designation,
            category=category,
            salary=salary
        )
        new_staff.save()

        # Create the associated StaffProfile
        StaffProfile.objects.create(
            enrollment=new_staff,
            experience_in_years=experience_in_years,
            image=image,
            address=address,
            date_of_birth=date_of_birth,
            married_status=married_status
        )

        return redirect('admin_dashboard')  # Redirect to admin dashboard after enrollment

    subjects = Subject.objects.all()  # Get all subjects for the dropdown
    return render(request, 'enroll_staff.html', {'subjects': subjects})

def manage_classes_view(request):
    classes = Class.objects.all()  # Retrieve all classes for display

    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        class_id = request.POST.get('class_id')

        if class_id:  # Update existing class
            class_instance = get_object_or_404(Class, id=class_id)
            class_instance.class_name = class_name
            class_instance.save()
        else:  # Add new class
            new_class = Class(class_name=class_name)
            new_class.save()

        return redirect('manage_classes')  # Redirect to the same page after adding/updating

    return render(request, 'manage_classes.html', {'classes': classes})

def delete_class_view(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    class_instance.delete()
    return redirect('manage_classes')  # Redirect after deletion



def manage_subjects_view(request):
    error = None  # Initialize error variable

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        class_assigned_id = request.POST.get('class_assigned')

        # Check for existing subject logic
        if Subject.objects.filter(subject_name=subject_name, class_assigned_id=class_assigned_id).exists():
            error = "Subject already exists for this class."
        else:
            # Create a new subject
            Subject.objects.create(subject_name=subject_name, class_assigned_id=class_assigned_id)

    # Retrieve all classes and existing subjects
    classes = Class.objects.all()
    existing_subjects = Subject.objects.select_related('class_assigned').all()

    # Debugging output to check classes
    print("Classes retrieved:", classes)

    return render(request, 'manage_subjects.html', {
        'classes': classes,
        'existing_subjects': existing_subjects,
        'error': error if error else None,
    })

    
    
def delete_subject_view(request, subject_id):
    subject_instance = get_object_or_404(Subject, id=subject_id)
    subject_instance.delete()
    return redirect('manage_subjects')  # Redirect after deletion

def manage_class_timetable_view(request):
    timetables = ClassTimetable.objects.all()  # Retrieve all timetable entries
    classes = Class.objects.all()  # Retrieve all classes for dropdown
    subjects = Subject.objects.all()  # Retrieve all subjects for dropdown
    staff_members = StaffEnrollment.objects.all()  # Retrieve all staff for dropdown

    if request.method == 'POST':
        class_assigned_id = request.POST.get('class_assigned')
        subject_id = request.POST.get('subject')
        staff_id = request.POST.get('staff')
        day_of_week = request.POST.get('day_of_week')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        timetable_id = request.POST.get('timetable_id')

        # Debugging: Print submitted values
        print(f"Submitted values: Class ID: {class_assigned_id}, Subject ID: {subject_id}, Staff ID: {staff_id}")

        # Validate inputs
        if not class_assigned_id or not subject_id or not staff_id:
            messages.error(request, "Please fill out all fields.")
            return redirect('manage_class_timetable')

        try:
            class_assigned_id = int(class_assigned_id)
            subject_id = int(subject_id)
            staff_id = int(staff_id)  # Ensure staff_id is converted to int

            # Check if the IDs exist in the database
            if not Class.objects.filter(id=class_assigned_id).exists():
                messages.error(request, "Selected class does not exist.")
                return redirect('manage_class_timetable')

            if not Subject.objects.filter(id=subject_id).exists():
                messages.error(request, "Selected subject does not exist.")
                return redirect('manage_class_timetable')

            if not StaffEnrollment.objects.filter(id=staff_id).exists():
                messages.error(request, "Selected staff does not exist.")
                return redirect('manage_class_timetable')

            # Time conflict check
            if timetable_id:  # Updating existing timetable
                existing_timetable = get_object_or_404(ClassTimetable, id=timetable_id)
                existing_start_time = existing_timetable.start_time
                existing_end_time = existing_timetable.end_time
                existing_day = existing_timetable.day_of_week
            else:  # Adding new timetable entry
                existing_start_time = start_time
                existing_end_time = end_time
                existing_day = day_of_week

            # Check for time slot conflicts
            conflicting_entries = ClassTimetable.objects.filter(
                class_assigned_id=class_assigned_id,
                day_of_week=existing_day
            ).exclude(id=timetable_id).filter(
                (Q(start_time__lt=existing_end_time) & Q(end_time__gt=existing_start_time))
            )

            if conflicting_entries.exists():
                messages.error(request, "This class has a conflicting timetable entry during the selected time.")
                return redirect('manage_class_timetable')

            # Proceed to add/update the timetable
            if timetable_id:  # Update existing timetable
                timetable_instance = get_object_or_404(ClassTimetable, id=timetable_id)
                timetable_instance.class_assigned_id = class_assigned_id
                timetable_instance.subject_id = subject_id
                timetable_instance.staff_id = staff_id
                timetable_instance.day_of_week = existing_day
                timetable_instance.start_time = start_time
                timetable_instance.end_time = end_time
                timetable_instance.save()
            else:  # Add new timetable entry
                new_timetable = ClassTimetable(
                    class_assigned_id=class_assigned_id,
                    subject_id=subject_id,
                    staff_id=staff_id,
                    day_of_week=existing_day,
                    start_time=start_time,
                    end_time=end_time
                )
                new_timetable.save()

            messages.success(request, "Timetable entry added/updated successfully.")
            return redirect('manage_class_timetable')  # Redirect after adding/updating

        except (ValueError, TypeError):
            messages.error(request, "Invalid input for class, subject, or staff. Please ensure all fields are filled out correctly.")
            return redirect('manage_class_timetable')

    return render(request, 'manage_class_timetable.html', {
        'timetables': timetables,
        'classes': classes,
        'subjects': subjects,
        'staff_members': staff_members,
    })

def delete_class_timetable_view(request, timetable_id):
    timetable_instance = get_object_or_404(ClassTimetable, id=timetable_id)
    timetable_instance.delete()
    return redirect('manage_class_timetable')  # Redirect after deletion

def manage_attendance_view(request):
    # Retrieve attendance records for students and staff
    student_attendance_records = StudentAttendance.objects.all()
    staff_attendance_records = StaffAttendance.objects.all()

    if request.method == 'POST':
        # Handle adding/updating attendance records
        attendance_type = request.POST.get('attendance_type')  # 'student' or 'staff'
        attendance_id = request.POST.get('attendance_id')
        date = request.POST.get('date')
        is_present = request.POST.get('is_present') == 'True'  # Convert to boolean
        reason = request.POST.get('reason', '')

        if attendance_type == 'student':
            if attendance_id:  # Update existing record
                attendance_instance = get_object_or_404(StudentAttendance, id=attendance_id)
                attendance_instance.date = date
                attendance_instance.is_present = is_present
                attendance_instance.reason = reason
                attendance_instance.save()
            else:  # Add new record
                student_id = request.POST.get('student_id')
                student_instance = get_object_or_404(StudentProfile, id=student_id)
                new_attendance = StudentAttendance(
                    student=student_instance,
                    date=date,
                    is_present=is_present,
                    reason=reason
                )
                new_attendance.save()

        elif attendance_type == 'staff':
            if attendance_id:  # Update existing record
                attendance_instance = get_object_or_404(StaffAttendance, id=attendance_id)
                attendance_instance.date = date
                attendance_instance.is_present = is_present
                attendance_instance.reason = reason
                attendance_instance.save()
            else:  # Add new record
                staff_id = request.POST.get('staff_id')
                staff_instance = get_object_or_404(StaffProfile, id=staff_id)
                new_attendance = StaffAttendance(
                    staff=staff_instance,
                    date=date,
                    is_present=is_present,
                    reason=reason
                )
                new_attendance.save()

        return redirect('manage_attendance')  # Redirect after adding/updating

    return render(request, 'manage_attendance.html', {
        'student_attendance_records': student_attendance_records,
        'staff_attendance_records': staff_attendance_records,
        'students': StudentProfile.objects.all(),  # For attendance entry
        'staffs': StaffProfile.objects.all(),  # For attendance entry
    })

def delete_attendance_view(request, attendance_type, attendance_id):
    if attendance_type == 'student':
        attendance_instance = get_object_or_404(StudentAttendance, id=attendance_id)
    elif attendance_type == 'staff':
        attendance_instance = get_object_or_404(StaffAttendance, id=attendance_id)

    attendance_instance.delete()
    return redirect('manage_attendance')  # Redirect after deletion

def manage_leaves_view(request):
    # Retrieve all leave reports for students and staff
    student_leaves = StudentLeaveReport.objects.all()
    staff_leaves = StaffLeaveReport.objects.all()

    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')  # 'student' or 'staff'
        leave_id = request.POST.get('leave_id')
        action = request.POST.get('action')  # 'approve' or 'reject'

        if leave_type == 'student':
            leave_instance = get_object_or_404(StudentLeaveReport, id=leave_id)
            if action == 'approve':
                leave_instance.status = 'Approved'  # Assuming there's a status field
            elif action == 'reject':
                leave_instance.status = 'Rejected'  # Assuming there's a status field
            leave_instance.save()

        elif leave_type == 'staff':
            leave_instance = get_object_or_404(StaffLeaveReport, id=leave_id)
            if action == 'approve':
                leave_instance.status = 'Approved'
            elif action == 'reject':
                leave_instance.status = 'Rejected'
            leave_instance.save()

        return redirect('manage_leaves')  # Redirect after processing

    return render(request, 'manage_leaves.html', {
        'student_leaves': student_leaves,
        'staff_leaves': staff_leaves,
    })

def create_notification_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        # Create a new notification
        Notification.objects.create(message=message)
        return redirect('manage_notifications')  # Redirect to the notification list

    return render(request, 'create_notification.html')

def manage_notifications_view(request):
    notifications = Notification.objects.all()

    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        action = request.POST.get('action')  # 'delete'

        if action == 'delete':
            Notification.objects.filter(id=notification_id).delete()

        return redirect('manage_notifications')  # Redirect after processing

    return render(request, 'manage_notifications.html', {
        'notifications': notifications,
    })
    
def monitor_fees_view(request):
    # Fetch all student fees with related student data
    student_fees = StudentFee.objects.select_related('student').all()

    print(f'Total student fees records: {student_fees.count()}')

    # For generating reports
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        report_data = StudentFee.objects.filter(student_id=student_id)
        return render(request, 'fee_report.html', {'report_data': report_data})

    return render(request, 'monitor_fees.html', {
        'student_fees': student_fees,
    })




def fee_report_view(request, student_id):
    report_data = StudentFee.objects.filter(student_id=student_id)
    return render(request, 'fee_report.html', {'report_data': report_data})

def schedule_exam_view(request):
    if request.method == 'POST':
        name_of_exam = request.POST.get('name_of_exam')
        subject_id = request.POST.get('subject')
        exam_date = request.POST.get('exam_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        class_id = request.POST.get('class_assigned')

        # Create new ExaminationTimetable entry
        ExaminationTimetable.objects.create(
            name_of_exam=name_of_exam,
            subject_id=subject_id,
            exam_date=exam_date,
            start_time=start_time,
            end_time=end_time,
            class_assigned_id=class_id
        )
        return redirect('schedule_exam')

    subjects = Subject.objects.all()
    classes = Class.objects.all()
    exams = ExaminationTimetable.objects.all()

    return render(request, 'schedule_exam.html', {
        'subjects': subjects,
        'classes': classes,
        'exams': exams,
    })

def update_exam_view(request, exam_id):
    exam = ExaminationTimetable.objects.get(id=exam_id)

    if request.method == 'POST':
        exam.name_of_exam = request.POST.get('name_of_exam')
        exam.subject_id = request.POST.get('subject')
        exam.exam_date = request.POST.get('exam_date')
        exam.start_time = request.POST.get('start_time')
        exam.end_time = request.POST.get('end_time')
        exam.class_assigned_id = request.POST.get('class_assigned')
        exam.save()
        return redirect('schedule_exam')

    subjects = Subject.objects.all()
    classes = Class.objects.all()

    return render(request, 'update_exam.html', {
        'exam': exam,
        'subjects': subjects,
        'classes': classes,
    })

def delete_exam_view(request, exam_id):
    exam = ExaminationTimetable.objects.get(id=exam_id)
    exam.delete()
    return redirect('schedule_exam')

def review_exam_results_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        grades = StudentGrade.objects.filter(student_id=student_id, subject_id=subject_id)

        # Optionally, you can also calculate the average grade here
        average_grade = grades.aggregate(Avg('grade'))['grade__avg']
        return render(request, 'review_exam_results.html', {
            'grades': grades,
            'average_grade': average_grade,
            'student_id': student_id,
            'subject_id': subject_id,
        })

    students = StudentProfile.objects.all()
    subjects = Subject.objects.all()

    return render(request, 'review_exam_results.html', {
        'students': students,
        'subjects': subjects,
    })

def generate_exam_report_view(request):
    grades = StudentGrade.objects.all()
    report_data = {}

    for grade in grades:
        student = grade.student
        subject = grade.subject
        report_data.setdefault(student.student_id, {'name': student.student_name, 'grades': []})
        report_data[student.student_id]['grades'].append({
            'subject': subject.subject_name,
            'grade': grade.grade,
            'date': grade.date_recorded,
        })

    return render(request, 'exam_report.html', {'report_data': report_data})

def edit_student_profile(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    if request.method == 'POST':
        # Update student profile fields
        student.date_of_birth = request.POST['date_of_birth']
        student.address = request.POST['address']
        student.contact_number = request.POST['contact_number']
        student.save()
        return redirect('manage_student_profiles')
    return render(request, 'edit_student.html', {'student': student})

def delete_student_profile(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    student.delete()
    return redirect('manage_student_profiles')

def manage_staff_profiles(request):
    staff = StaffProfile.objects.all()
    return render(request, 'manage_staff.html', {'staff': staff})

def edit_staff_profile(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)
    if request.method == 'POST':
        # Update staff profile fields
        staff.experience_in_years = request.POST['experience_in_years']
        staff.address = request.POST['address']
        staff.date_of_birth = request.POST['date_of_birth']
        staff.married_status = request.POST.get('married_status') == 'True'
        staff.save()
        return redirect('manage_staff_profiles')
    return render(request, 'edit_staff.html', {'staff': staff})

def delete_staff_profile(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)
    staff.delete()
    return redirect('manage_staff_profiles')
def view_leave_requests(request):
    staff_leaves = StaffLeaveReport.objects.all()
    student_leaves = StudentLeaveReport.objects.all()
    return render(request, 'view_leaves.html', {'staff_leaves': staff_leaves, 'student_leaves': student_leaves})

def approve_leave(request, leave_id, leave_type):
    if leave_type == 'staff':
        leave = get_object_or_404(StaffLeaveReport, id=leave_id)
    else:
        leave = get_object_or_404(StudentLeaveReport, id=leave_id)
    leave.approved = True  # Assuming you add an 'approved' field
    leave.save()
    return redirect('view_leave_requests')
def view_attendance_reports(request):
    student_attendance = StudentAttendance.objects.all()
    staff_attendance = StaffAttendance.objects.all()
    return render(request, 'attendance_reports.html', {'student_attendance': student_attendance, 'staff_attendance': staff_attendance})

def manage_fee_structure(request):
    if request.method == 'POST':
        # Logic to add/update fee structure
        pass
    fees = StudentFee.objects.all()
    return render(request, 'manage_fees.html', {'fees': fees})

def delete_fee_structure(request, fee_id):
    fee = get_object_or_404(StudentFee, id=fee_id)
    fee.delete()
    return redirect('manage_fee_structure')

def manage_events(request):
    events = Event.objects.all()
    return render(request, 'manage_events.html', {'events': events})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        # Update event details
        event.name = request.POST['name']
        event.date = request.POST['date']
        event.description = request.POST['description']
        event.save()
        return redirect('manage_events')
    return render(request, 'edit_event.html', {'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('manage_events')

def manage_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'manage_notifications.html', {'notifications': notifications})

def edit_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    if request.method == 'POST':
        notification.message = request.POST['message']
        notification.save()
        return redirect('manage_notifications')
    return render(request, 'edit_notification.html', {'notification': notification})

def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.delete()
    return redirect('manage_notifications')

def manage_exam_schedule(request):
    exams = ExaminationTimetable.objects.all()
    return render(request, 'manage_exams.html', {'exams': exams})

def edit_exam_schedule(request, exam_id):
    exam = get_object_or_404(ExaminationTimetable, id=exam_id)
    if request.method == 'POST':
        exam.name_of_exam = request.POST['name_of_exam']
        exam.exam_date = request.POST['exam_date']
        exam.start_time = request.POST['start_time']
        exam.end_time = request.POST['end_time']
        exam.save()
        return redirect('manage_exam_schedule')
    return render(request, 'edit_exam.html', {'exam': exam})

def delete_exam_schedule(request, exam_id):
    exam = get_object_or_404(ExaminationTimetable, id=exam_id)
    exam.delete()
    return redirect('manage_exam_schedule')

def view_feedback(request):
    student_feedbacks = StudentFeedback.objects.all()
    staff_feedbacks = StaffFeedback.objects.all()
    return render(request, 'view_feedback.html', {'student_feedbacks': student_feedbacks, 'staff_feedbacks': staff_feedbacks})

def generate_class_timetable(request):
    timetables = ClassTimetable.objects.all()
    return render(request, 'class_timetable.html', {'timetables': timetables})
from .models import BehaviorReport

def view_behavior_reports(request):
    reports = BehaviorReport.objects.all()
    return render(request, 'behavior_reports.html', {'reports': reports})
#___________________________________________________________________#
#                            Staff views                            #
#-------------------------------------------------------------------#
def update_staff_profile(request, staff_id):
    staff = get_object_or_404(StaffProfile, enrollment__staff_id=staff_id)
    if request.method == 'POST':
        # Update staff profile fields
        staff.address = request.POST['address']
        staff.date_of_birth = request.POST['date_of_birth']
        staff.married_status = request.POST.get('married_status') == 'True'
        staff.experience_in_years = request.POST['experience_in_years']
        staff.save()
        return redirect('staff_dashboard')  # Redirect to staff dashboard after update
    return render(request, 'update_staff_profile.html', {'staff': staff})

def view_class_students(request, class_id):
    # Retrieve the class instance using the class_id
    class_instance = get_object_or_404(Class, id=class_id)

    # Retrieve students associated with the class
    students = StudentEnrollment.objects.filter(class_assigned=class_instance)

    # Render the template with the class instance and its students
    return render(request, 'class_students.html', {
        'class': class_instance,
        'students': students,
    })

def class_students(request, class_id):
    students = StudentProfile.objects.filter(enrollment__class_assigned__id=class_id)
    return render(request, 'view_students.html', {'students': students})

def view_class_subjects(request):
    classes = Class.objects.all()
    return render(request, 'class_subjects.html', {'classes': classes})
def class_subjects(request, class_id):
    subjects = Subject.objects.filter(class_assigned__id=class_id)
    return render(request, 'view_subjects.html', {'subjects': subjects})
def manage_class_attendance(request):
    classes = Class.objects.all()
    return render(request, 'class_attendance.html', {'classes': classes})

# def mark_attendance(request, class_id):
#     # Retrieve the class instance
#     class_instance = get_object_or_404(Class, id=class_id)
    
#     # Retrieve students associated with the class
#     students = StudentEnrollment.objects.filter(class_assigned=class_instance)

#     if request.method == 'POST':
#         # Process the attendance form submission
#         for student in students:
#             attended = request.POST.get(f'attendance_{student.student_id}') == 'on'
#             # Save attendance record for each student
#             StudentAttendance.objects.create(
#                 student=student,
#                 class_assigned=class_instance,
#                 attended=attended,
#                 date=request.POST.get('date'),  # Make sure you have a date field
#             )
#         return redirect('attendance_success')  # Redirect after successful submission

#     return render(request, 'mark_attendance.html', {
#         'class': class_instance,
#         'students': students,
#     })
def mark_attendance(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    students = StudentEnrollment.objects.filter(class_assigned=class_instance)

    if request.method == 'POST':
        date = request.POST.get('date')  # Retrieve the date from the form
        if not date:
            messages.error(request, "Date is required.")
            return render(request, 'mark_attendance.html', {
                'class': class_instance,
                'students': students,
                'today': datetime.date.today()
            })

        # Validate date format
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()  # Convert to date object
        except ValueError:
            messages.error(request, "Invalid date format. Must be YYYY-MM-DD.")
            return render(request, 'mark_attendance.html', {
                'class': class_instance,
                'students': students,
                'today': datetime.date.today()
            })

        for student in students:
            attended = request.POST.get(f'attendance_{student.student_id}') == 'on'
            # Create or update attendance record
            StudentAttendance.objects.update_or_create(
                student=student,  # Use the correct instance
                class_assigned=class_instance,
                date=date_obj,  # Use the validated date
                defaults={'is_present': attended}
            )

        messages.success(request, "Attendance marked successfully.")
        return redirect('view_attendance_reports')

    return render(request, 'mark_attendance.html', {
        'class': class_instance,
        'students': students,
        'today': datetime.date.today(),  # Pass the current date
    })
    
def manage_self_attendance(request, staff_id):
    # Ensure the staff member exists
    staff_enrollment = get_object_or_404(StaffEnrollment, staff_id=staff_id)

    # Retrieve the related StaffProfile
    staff_profile = get_object_or_404(StaffProfile, enrollment=staff_enrollment)

    if request.method == 'POST':
        date = request.POST.get('date')
        is_present = request.POST.get('is_present') == 'on'
        
        # Create attendance record using StaffProfile instance
        attendance = StaffAttendance.objects.create(
            staff=staff_profile,  # Use the StaffProfile instance
            date=date,
            is_present=is_present
        )
        
        messages.success(request, "Attendance marked successfully.")
        return redirect('staff_dashboard')  # Redirect after marking self-attendance

    return render(request, 'self_attendance.html', {'staff': staff_enrollment})  # Pass staff enrollment to the template

def manage_student_marks(request):
    subjects = Subject.objects.all()
    return render(request, 'student_marks.html', {'subjects': subjects})

def record_student_marks(request, subject_id):
    # Filter students based on the subject
    students = StudentEnrollment.objects.filter(class_assigned__subject__id=subject_id)

    if request.method == 'POST':
        for student in students:
            grade = request.POST.get(f'student_{student.id}')
            if grade:  # Ensure there's a grade before creating
                try:
                    student_profile = StudentProfile.objects.get(enrollment=student)  # Assuming there's a relationship
                    StudentGrade.objects.create(
                        student=student_profile,  # Correctly assign the StudentProfile instance
                        subject_id=subject_id,
                        grade=grade,
                        date_recorded=request.POST['date']
                    )
                except StudentProfile.DoesNotExist:
                    messages.error(request, f"No profile found for student: {student.student_name}")

        messages.success(request, "Marks recorded successfully.")
        return redirect('staff_dashboard')  # Redirect after recording marks

    return render(request, 'record_marks.html', {'students': students})


def view_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications.html', {'notifications': notifications})

def view_subject_timetable(request, subject_id):
    timetable = ClassTimetable.objects.filter(subject_id=subject_id)
    return render(request, 'subject_timetable.html', {'timetable': timetable})

def view_class_timetable(request, class_id):
    timetable = ClassTimetable.objects.filter(class_assigned_id=class_id)
    return render(request, 'class_timetable_staff.html', {'timetable': timetable})
def view_salary_particulars(request, staff_id):
    staff = get_object_or_404(StaffEnrollment, staff_id=staff_id)
    return render(request, 'salary_particulars.html', {'staff': staff})
def staff_logout(request):
    logout(request)
    return redirect('login') 

#___________________________________________________________________#
#                            Student views                          #
#-------------------------------------------------------------------#
def update_student_profile(request, student_id):
    student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
    if request.method == 'POST':
        # Update student profile fields
        student.address = request.POST['address']
        student.date_of_birth = request.POST['date_of_birth']
        student.contact_number = request.POST['contact_number']
        student.save()
        return redirect('student_dashboard')  # Redirect to student dashboard after update
    return render(request, 'update_student_profile.html', {'student': student})

def view_attendance(request, student_id):
    today = timezone.now().date()
    attendance_records = StudentAttendance.objects.filter(student__student_id=student_id)
    return render(request, 'view_attendance.html', {
        'attendance_records': attendance_records,
        'today': today
    })

def view_attendance_month(request, student_id, month, year):
    attendance_records = StudentAttendance.objects.filter(student__enrollment__student_id=student_id, date__month=month, date__year=year)
    return render(request, 'view_attendance_month.html', {'attendance_records': attendance_records})

def view_attendance_range(request, student_id, start_date, end_date):
    attendance_records = StudentAttendance.objects.filter(
        student__enrollment__student_id=student_id,
        date__range=[start_date, end_date]
    )
    
    print(f"Student ID: {student_id}")  # Debugging line
    
    return render(request, 'view_attendance_range.html', {
        'attendance_records': attendance_records,
        'student_id': student_id  # Ensure student_id is included
    })
def view_timetable(request, student_id):
    student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
    timetable = ClassTimetable.objects.filter(class_assigned=student.enrollment.class_assigned)
    return render(request, 'view_timetable.html', {'timetable': timetable})
def view_examination_timetable(request, student_id):
    student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
    exam_timetable = ExaminationTimetable.objects.filter(class_assigned=student.enrollment.class_assigned)
    return render(request, 'view_examination_timetable.html', {'exam_timetable': exam_timetable})

def view_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'view_notifications.html', {'notifications': notifications})
def manage_feedback(request, student_id):
    if request.method == 'POST':
        feedback = StudentFeedback()
        feedback.student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
        feedback.feedback_date = timezone.now()
        feedback.content = request.POST['content']
        feedback.save()
        return redirect('student_dashboard')  # Redirect after submitting feedback
    return render(request, 'manage_feedback.html')

def view_fee_particulars(request, student_id):
    fee_details = StudentFee.objects.filter(student__enrollment__student_id=student_id)
    return render(request, 'view_fee_particulars.html', {'fee_details': fee_details})

def student_logout(request):
    logout(request)
    return redirect('login')
