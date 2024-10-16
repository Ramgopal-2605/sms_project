import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.db.models import Avg
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import login as auth_login
from django.utils.crypto import get_random_string
from .models import AdminPrincipalRegistration
from .serializers import AdminPrincipalRegistrationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import (
    AdminPrincipalRegistration,
    Class,
    Subject,
    StudentEnrollment,
    StaffEnrollment,
    StudentProfile,
    StaffProfile,
    StudentFee,
    StaffSalary,
    StaffAttendance,
    StudentAttendance,
    StaffAttendanceReport,
    StudentAttendanceReport,
    StaffLeaveReport,
    StudentLeaveReport,
    StudentFeedback,
    StaffFeedback,
    StudentGrade,
    Event,
    ExtracurricularActivity,
    Notification,
    ClassTimetable,
    ExaminationTimetable,
    CounselingSession,
    BehaviorReport,
    CertificateRequestsStudent,
)
from .serializers import (
    AdminPrincipalRegistrationSerializer,
    ClassSerializer,
    SubjectSerializer,
    StudentEnrollmentSerializer,
    StaffEnrollmentSerializer,
    StudentProfileSerializer,
    StaffProfileSerializer,
    StudentFeeSerializer,
    StaffSalarySerializer,
    StaffAttendanceSerializer,
    StudentAttendanceSerializer,
    StaffAttendanceReportSerializer,
    StudentAttendanceReportSerializer,
    StaffLeaveReportSerializer,
    StudentLeaveReportSerializer,
    StudentFeedbackSerializer,
    StaffFeedbackSerializer,
    StudentGradeSerializer,
    EventSerializer,
    ExtracurricularActivitySerializer,
    NotificationSerializer,
    ClassTimetableSerializer,
    ExaminationTimetableSerializer,
    CounselingSessionSerializer,
    BehaviorReportSerializer,
    CertificateRequestsStudentSerializer,
)


# class AdminRegistrationView(viewsets.ModelViewSet):
#     queryset = AdminPrincipalRegistration.objects.all()
#     serializer_class = AdminPrincipalRegistrationSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ClassViewSet(viewsets.ModelViewSet):
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer
#     permission_classes = [IsAuthenticated]


# class SubjectViewSet(viewsets.ModelViewSet):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#     permission_classes = [IsAuthenticated]


# class StudentEnrollmentViewSet(viewsets.ModelViewSet):
#     queryset = StudentEnrollment.objects.all()
#     serializer_class = StudentEnrollmentSerializer
#     permission_classes = [IsAuthenticated]


# class StaffEnrollmentViewSet(viewsets.ModelViewSet):
#     queryset = StaffEnrollment.objects.all()
#     serializer_class = StaffEnrollmentSerializer
#     permission_classes = [IsAuthenticated]


# class StudentProfileViewSet(viewsets.ModelViewSet):
#     queryset = StudentProfile.objects.all()
#     serializer_class = StudentProfileSerializer
#     permission_classes = [IsAuthenticated]


# class StaffProfileViewSet(viewsets.ModelViewSet):
#     queryset = StaffProfile.objects.all()
#     serializer_class = StaffProfileSerializer
#     permission_classes = [IsAuthenticated]


# class StudentFeeViewSet(viewsets.ModelViewSet):
#     queryset = StudentFee.objects.all()
#     serializer_class = StudentFeeSerializer
#     permission_classes = [IsAuthenticated]


# class StaffSalaryViewSet(viewsets.ModelViewSet):
#     queryset = StaffSalary.objects.all()
#     serializer_class = StaffSalarySerializer
#     permission_classes = [IsAuthenticated]


# class StudentAttendanceViewSet(viewsets.ModelViewSet):
#     queryset = StudentAttendance.objects.all()
#     serializer_class = StudentAttendanceSerializer
#     permission_classes = [IsAuthenticated]


# class StaffAttendanceViewSet(viewsets.ModelViewSet):
#     queryset = StaffAttendance.objects.all()
#     serializer_class = StaffAttendanceSerializer
#     permission_classes = [IsAuthenticated]


# class StaffAttendanceReportViewSet(viewsets.ModelViewSet):
#     queryset = StaffAttendanceReport.objects.all()
#     serializer_class = StaffAttendanceReportSerializer
#     permission_classes = [IsAuthenticated]


# class StudentAttendanceReportViewSet(viewsets.ModelViewSet):
#     queryset = StudentAttendanceReport.objects.all()
#     serializer_class = StudentAttendanceReportSerializer
#     permission_classes = [IsAuthenticated]


# class StaffLeaveReportViewSet(viewsets.ModelViewSet):
#     queryset = StaffLeaveReport.objects.all()
#     serializer_class = StaffLeaveReportSerializer
#     permission_classes = [IsAuthenticated]


# class StudentLeaveReportViewSet(viewsets.ModelViewSet):
#     queryset = StudentLeaveReport.objects.all()
#     serializer_class = StudentLeaveReportSerializer
#     permission_classes = [IsAuthenticated]


# class StudentFeedbackViewSet(viewsets.ModelViewSet):
#     queryset = StudentFeedback.objects.all()
#     serializer_class = StudentFeedbackSerializer
#     permission_classes = [IsAuthenticated]





# class StudentGradeViewSet(viewsets.ModelViewSet):
#     queryset = StudentGrade.objects.all()
#     serializer_class = StudentGradeSerializer
#     permission_classes = [IsAuthenticated]


# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [IsAuthenticated]


# class ExtracurricularActivityViewSet(viewsets.ModelViewSet):
#     queryset = ExtracurricularActivity.objects.all()
#     serializer_class = ExtracurricularActivitySerializer
#     permission_classes = [IsAuthenticated]


# class NotificationViewSet(viewsets.ModelViewSet):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer
#     permission_classes = [IsAuthenticated]


# class ClassTimetableViewSet(viewsets.ModelViewSet):
#     queryset = ClassTimetable.objects.all()
#     serializer_class = ClassTimetableSerializer
#     permission_classes = [IsAuthenticated]


# class ExaminationTimetableViewSet(viewsets.ModelViewSet):
#     queryset = ExaminationTimetable.objects.all()
#     serializer_class = ExaminationTimetableSerializer
#     permission_classes = [IsAuthenticated]


# class CounselingSessionViewSet(viewsets.ModelViewSet):
#     queryset = CounselingSession.objects.all()
#     serializer_class = CounselingSessionSerializer
#     permission_classes = [IsAuthenticated]


# class BehaviorReportViewSet(viewsets.ModelViewSet):
#     queryset = BehaviorReport.objects.all()
#     serializer_class = BehaviorReportSerializer
#     permission_classes = [IsAuthenticated]


# class CertificateRequestsStudentViewSet(viewsets.ModelViewSet):
#     queryset = CertificateRequestsStudent.objects.all()
#     serializer_class = CertificateRequestsStudentSerializer
#     permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    return Response({"message": "Welcome to the API"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def admin_registration(request):
    serializer = AdminPrincipalRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        # Hash the password
        password = (serializer.validated_data['pwd'])
        
        # Create a user instance
        user = User.objects.create_user(
            username=serializer.validated_data['Adminid'],  # Use Adminid as the username
            password=password
        )

        # Save the new admin instance
        admin = serializer.save()
        admin.user = user  # Link the admin to the user
        admin.save()

        # Create a token for the new admin
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "admin_id": admin.Adminid,
            "message": "Admin registered successfully."
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    user_id = request.data.get('user_id')
    password = request.data.get('password')

    # Check for Admin
    try:
        admin = AdminPrincipalRegistration.objects.get(Adminid=user_id, pwd=password)
        request.session['user_type'] = 'admin'
        request.session['user_id'] = admin.Adminid
        return Response({"message": "Admin login successful"}, status=status.HTTP_200_OK)

    except AdminPrincipalRegistration.DoesNotExist:
        pass

    # Check for Student
    try:
        student = StudentEnrollment.objects.get(student_id=user_id, student_pwd=password)
        request.session['user_type'] = 'student'
        request.session['user_id'] = student.student_id
        return Response({"message": "Student login successful"}, status=status.HTTP_200_OK)

    except StudentEnrollment.DoesNotExist:
        pass

    # Check for Staff
    try:
        staff = StaffEnrollment.objects.get(staff_id=user_id, staff_pwd=password)
        request.session['user_type'] = 'staff'
        request.session['user_id'] = staff.staff_id
        return Response({"message": "Staff login successful"}, status=status.HTTP_200_OK)

    except StaffEnrollment.DoesNotExist:
        return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'admin':
        return Response({"error": "Please log in to access the dashboard."}, status=status.HTTP_403_FORBIDDEN)

    try:
        admin = AdminPrincipalRegistration.objects.get(Adminid=user_id)
    except AdminPrincipalRegistration.DoesNotExist:
        return Response({"error": "Admin not found."}, status=status.HTTP_404_NOT_FOUND)

    # Retrieve data for the admin dashboard
    total_students = StudentProfile.objects.count()
    total_staff = StaffProfile.objects.count()
    total_classes = Class.objects.count()
    total_events = Event.objects.count()
    notifications = Notification.objects.all()[:5]

    return Response({
        'total_students': total_students,
        'total_staff': total_staff,
        'total_classes': total_classes,
        'total_events': total_events,
        'notifications': notifications,
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def staff_dashboard(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'staff':
        return Response({"error": "Please log in to access the dashboard."}, status=status.HTTP_403_FORBIDDEN)

    try:
        staff = StaffEnrollment.objects.get(staff_id=user_id)
    except StaffEnrollment.DoesNotExist:
        return Response({"error": "Staff member not found."}, status=status.HTTP_404_NOT_FOUND)

    notifications = Notification.objects.all()[:5]
    assigned_subject = staff.subject_assigned

    return Response({
        'staff': staff,
        'notifications': notifications,
        'assigned_subject': assigned_subject,
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_urls(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'student':
        return Response({"error": "Please log in to access this resource."}, status=status.HTTP_403_FORBIDDEN)

    student_id = request.user.id  # Assuming the session stores the student ID directly
    return Response({"student_id": student_id}, status=status.HTTP_200_OK)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import StaffEnrollment, StudentEnrollment, Notification
from .serializers import StaffEnrollmentSerializer, StudentEnrollmentSerializer, NotificationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def staff_urls(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'staff':
        return Response({"error": "Please log in to access this page."}, status=status.HTTP_403_FORBIDDEN)

    try:
        staff = StaffEnrollment.objects.get(staff_id=user_id)
    except StaffEnrollment.DoesNotExist:
        return Response({"error": "Staff member not found."}, status=status.HTTP_404_NOT_FOUND)

    staff_data = StaffEnrollmentSerializer(staff).data
    class_id = staff.class_id if hasattr(staff, 'class_id') else None
    subject_id = staff.subject_assigned if hasattr(staff, 'subject_assigned') else None

    return Response({
        'staff': staff_data,
        'class_id': class_id,
        'subject_id': subject_id,
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_dashboard(request):
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if not user_id or user_type != 'student':
        return Response({"error": "Please log in to access the dashboard."}, status=status.HTTP_403_FORBIDDEN)

    try:
        student = StudentEnrollment.objects.get(student_id=user_id)
    except StudentEnrollment.DoesNotExist:
        return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    notifications = Notification.objects.all()[:5]
    enrolled_class = student.class_assigned

    return Response({
        'student': StudentEnrollmentSerializer(student).data,
        'notifications': NotificationSerializer(notifications, many=True).data,
        'enrolled_class': enrolled_class,
    }, status=status.HTTP_200_OK)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import StudentEnrollment, StaffEnrollment, Class, StudentProfile, StaffProfile, StudentFee
from .serializers import (
    StudentEnrollmentSerializer,
    StaffEnrollmentSerializer,
    ClassSerializer,
)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_student_view(request):
    data = request.data
    try:
        # Create the new student enrollment
        new_student = StudentEnrollment.objects.create(
            student_name=data['student_name'],
            student_id=data['student_id'],
            student_pwd=data['student_pwd'],  # Ensure to hash the password if needed
            father_name=data['father_name'],
            mother_name=data['mother_name'],
            class_assigned_id=data['class_assigned'],
            enrollment_date=timezone.now(),  # Automatically set the enrollment date
            fee_details=data['fee_details']
        )

        # Create the student fee record
        StudentFee.objects.create(
            student=new_student,
            amount_due=data['fee_details'],
            amount_paid=0.00,
            installments=1,
            due_date=timezone.now()  # Adjust this as necessary
        )

        # Create the student profile (if applicable)
        StudentProfile.objects.create(
            enrollment=new_student,
            date_of_birth=data['date_of_birth'],
            address=data['address'],
            image=data.get('image'),
            contact_number=data['contact_number']
        )

        return Response({
            "message": "Student enrolled successfully."
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_staff_view(request):
    data = request.data
    try:
        # Create the new staff enrollment
        new_staff = StaffEnrollment.objects.create(
            staff_name=data['staff_name'],
            staff_id=data['staff_id'],
            staff_pwd=data['staff_pwd'],
            subject_assigned_id=data['subject_assigned'],
            date_of_hire=data['date_of_hire'],
            designation=data['designation'],
            category=data['category'],
            salary=data['salary']
        )

        # Create the staff profile
        StaffProfile.objects.create(
            enrollment=new_staff,
            experience_in_years=data['experience_in_years'],
            image=data.get('image'),
            address=data['address'],
            date_of_birth=data['date_of_birth'],
            married_status=data['married_status']
        )

        # Optionally, you could return a success message without a token
        return Response({
            "message": "Staff enrolled successfully."
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_classes_view(request):
    if request.method == 'GET':
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        class_id = data.get('class_id')

        if class_id:  # Update existing class
            class_instance = get_object_or_404(Class, id=class_id)
            class_instance.class_name = data['class_name']
            class_instance.save()
        else:  # Add new class
            Class.objects.create(class_name=data['class_name'])

        return Response({"message": "Class saved successfully."}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_class_view(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    class_instance.delete()
    return Response({"message": "Class deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Subject, ClassTimetable, StudentAttendance, StaffAttendance, StudentProfile, StaffProfile
from .serializers import SubjectSerializer, ClassTimetableSerializer, AttendanceSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_subjects_view(request):
    if request.method == 'GET':
        subjects = Subject.objects.select_related('class_assigned').all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        subject_name = data.get('subject_name')
        class_assigned_id = data.get('class_assigned')

        if Subject.objects.filter(subject_name=subject_name, class_assigned_id=class_assigned_id).exists():
            return Response({"error": "Subject already exists for this class."}, status=status.HTTP_400_BAD_REQUEST)

        Subject.objects.create(subject_name=subject_name, class_assigned_id=class_assigned_id)
        return Response({"message": "Subject created successfully."}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_subject_view(request, subject_id):
    subject_instance = get_object_or_404(Subject, id=subject_id)
    subject_instance.delete()
    return Response({"message": "Subject deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_class_timetable_view(request):
    if request.method == 'GET':
        timetables = ClassTimetable.objects.all()
        serializer = ClassTimetableSerializer(timetables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        class_assigned_id = data.get('class_assigned')
        subject_id = data.get('subject')
        staff_id = data.get('staff')
        day_of_week = data.get('day_of_week')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        timetable_id = data.get('timetable_id')

        if not class_assigned_id or not subject_id or not staff_id:
            return Response({"error": "Please fill out all fields."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check for time slot conflicts
            conflicting_entries = ClassTimetable.objects.filter(
                class_assigned_id=class_assigned_id,
                day_of_week=day_of_week
            ).exclude(id=timetable_id).filter(
                start_time__lt=end_time, end_time__gt=start_time
            )

            if conflicting_entries.exists():
                return Response({"error": "This class has a conflicting timetable entry during the selected time."}, status=status.HTTP_400_BAD_REQUEST)

            if timetable_id:  # Update existing timetable
                timetable_instance = get_object_or_404(ClassTimetable, id=timetable_id)
                timetable_instance.class_assigned_id = class_assigned_id
                timetable_instance.subject_id = subject_id
                timetable_instance.staff_id = staff_id
                timetable_instance.day_of_week = day_of_week
                timetable_instance.start_time = start_time
                timetable_instance.end_time = end_time
                timetable_instance.save()
            else:  # Add new timetable entry
                ClassTimetable.objects.create(
                    class_assigned_id=class_assigned_id,
                    subject_id=subject_id,
                    staff_id=staff_id,
                    day_of_week=day_of_week,
                    start_time=start_time,
                    end_time=end_time
                )

            return Response({"message": "Timetable entry added/updated successfully."}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_class_timetable_view(request, timetable_id):
    timetable_instance = get_object_or_404(ClassTimetable, id=timetable_id)
    timetable_instance.delete()
    return Response({"message": "Timetable entry deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_attendance_view(request):
    if request.method == 'GET':
        # Fetching attendance records
        student_attendance_records = StudentAttendance.objects.all()
        staff_attendance_records = StaffAttendance.objects.all()
        
        # Serializing attendance records
        student_serializer = StudentAttendanceSerializer(student_attendance_records, many=True)
        staff_serializer = StaffAttendanceSerializer(staff_attendance_records, many=True)
        
        return Response({
            "students": student_serializer.data,
            "staff": staff_serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        attendance_type = data.get('attendance_type')  # 'student' or 'staff'
        attendance_id = data.get('attendance_id')
        date = data.get('date')
        is_present = data.get('is_present') == 'True'  # Convert to boolean
        reason = data.get('reason', '')

        if attendance_type == 'student':
            if attendance_id:  # Update existing record
                attendance_instance = get_object_or_404(StudentAttendance, id=attendance_id)
                attendance_instance.date = date
                attendance_instance.is_present = is_present
                attendance_instance.reason = reason
                attendance_instance.save()
            else:  # Add new record
                student_id = data.get('student_id')
                student_instance = get_object_or_404(StudentProfile, id=student_id)
                StudentAttendance.objects.create(
                    student=student_instance,
                    class_assigned=student_instance.class_assigned,  # Ensure this is defined in the StudentAttendance model
                    date=date,
                    is_present=is_present,
                    reason=reason
                )

        elif attendance_type == 'staff':
            if attendance_id:  # Update existing record
                attendance_instance = get_object_or_404(StaffAttendance, id=attendance_id)
                attendance_instance.date = date
                attendance_instance.is_present = is_present
                attendance_instance.reason = reason
                attendance_instance.save()
            else:  # Add new record
                staff_id = data.get('staff_id')
                staff_instance = get_object_or_404(StaffEnrollment, id=staff_id)
                StaffAttendance.objects.create(
                    staff=staff_instance,
                    date=date,
                    is_present=is_present,
                    reason=reason
                )

        return Response({"message": "Attendance record added/updated successfully."}, status=status.HTTP_201_CREATED)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_attendance_view(request, attendance_type, attendance_id):
    if attendance_type == 'student':
        attendance_instance = get_object_or_404(StudentAttendance, id=attendance_id)
    elif attendance_type == 'staff':
        attendance_instance = get_object_or_404(StaffAttendance, id=attendance_id)

    attendance_instance.delete()
    return Response({"message": "Attendance record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    StudentLeaveReport,
    StaffLeaveReport,
    Notification,
    StudentFee,
    ExaminationTimetable,
    Subject,
    Class,
)
from .serializers import (
    NotificationSerializer,
    StudentFeeSerializer,
    ExaminationTimetableSerializer,
)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_leaves_view(request):
    if request.method == 'GET':
        student_leaves = StudentLeaveReport.objects.all()
        staff_leaves = StaffLeaveReport.objects.all()
        student_serializer = StudentLeaveReportSerializer(student_leaves, many=True)
        staff_serializer = StaffLeaveReportSerializer(staff_leaves, many=True)
        return Response({
            'student_leaves': student_serializer.data,
            'staff_leaves': staff_serializer.data,
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        leave_type = request.data.get('leave_type')  # 'student' or 'staff'
        leave_id = request.data.get('leave_id')
        action = request.data.get('action')  # 'approve' or 'reject'

        if leave_type == 'student':
            leave_instance = get_object_or_404(StudentLeaveReport, id=leave_id)
        elif leave_type == 'staff':
            leave_instance = get_object_or_404(StaffLeaveReport, id=leave_id)
        else:
            return Response({"error": "Invalid leave type."}, status=status.HTTP_400_BAD_REQUEST)

        if action == 'approve':
            leave_instance.status = 'Approved'
        elif action == 'reject':
            leave_instance.status = 'Rejected'
        leave_instance.save()

        return Response({"message": "Leave status updated successfully."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_notification_view(request):
    message = request.data.get('message')
    Notification.objects.create(message=message)
    return Response({"message": "Notification created successfully."}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_notifications_view(request):
    if request.method == 'GET':
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        notification_id = request.data.get('notification_id')
        Notification.objects.filter(id=notification_id).delete()
        return Response({"message": "Notification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def monitor_fees_view(request):
    if request.method == 'GET':
        student_fees = StudentFee.objects.select_related('student').all()
        serializer = StudentFeeSerializer(student_fees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        student_id = request.data.get('student_id')
        report_data = StudentFee.objects.filter(student_id=student_id)
        serializer = StudentFeeSerializer(report_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fee_report_view(request, student_id):
    report_data = StudentFee.objects.filter(student_id=student_id)
    serializer = StudentFeeSerializer(report_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def schedule_exam_view(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        classes = Class.objects.all()
        exams = ExaminationTimetable.objects.all()
        return Response({
            'subjects': subjects.values(),
            'classes': classes.values(),
            'exams': exams.values(),
        }, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        ExaminationTimetable.objects.create(
            name_of_exam=data.get('name_of_exam'),
            subject_id=data.get('subject'),
            exam_date=data.get('exam_date'),
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            class_assigned_id=data.get('class_assigned')
        )
        return Response({"message": "Examination scheduled successfully."}, status=status.HTTP_201_CREATED)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    ExaminationTimetable,
    StudentGrade,
    StudentProfile,
    StaffProfile,
    StaffLeaveReport,
    StudentLeaveReport,
    StudentAttendance,
    StaffAttendance,
    StudentFee,
    Event,
    Notification,
)
from .serializers import (
    ExaminationTimetableSerializer,
    StudentGradeSerializer,
    StudentProfileSerializer,
    StaffProfileSerializer,
    AttendanceSerializer,
    StudentFeeSerializer,
    EventSerializer,
    NotificationSerializer,
)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def update_exam_view(request, exam_id):
    exam = get_object_or_404(ExaminationTimetable, id=exam_id)

    if request.method == 'POST':
        serializer = ExaminationTimetableSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Exam updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = ExaminationTimetableSerializer(exam)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_exam_view(request, exam_id):
    exam = get_object_or_404(ExaminationTimetable, id=exam_id)
    exam.delete()
    return Response({"message": "Exam deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_exam_results_view(request):
    if request.method == 'POST':
        student_id = request.data.get('student_id')
        subject_id = request.data.get('subject_id')
        grades = StudentGrade.objects.filter(student_id=student_id, subject_id=subject_id)
        average_grade = grades.aggregate(Avg('grade'))['grade__avg']
        serializer = StudentGradeSerializer(grades, many=True)

        return Response({
            'grades': serializer.data,
            'average_grade': average_grade,
            'student_id': student_id,
            'subject_id': subject_id,
        }, status=status.HTTP_200_OK)

    students = StudentProfile.objects.all()
    subjects = Subject.objects.all()
    student_serializer = StudentProfileSerializer(students, many=True)
    return Response({
        'students': student_serializer.data,
        'subjects': [subject.subject_name for subject in subjects],  # Assuming subject_name is the field you need
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

    return Response({'report_data': report_data}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_student_profile(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    if request.method == 'PUT':
        serializer = StudentProfileSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student profile updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = StudentProfileSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_student_profile(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    student.delete()
    return Response({"message": "Student profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manage_staff_profiles(request):
    staff = StaffProfile.objects.all()
    serializer = StaffProfileSerializer(staff, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_staff_profile(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)
    if request.method == 'PUT':
        serializer = StaffProfileSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Staff profile updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = StaffProfileSerializer(staff)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_staff_profile(request, staff_id):
    staff = get_object_or_404(StaffProfile, id=staff_id)
    staff.delete()
    return Response({"message": "Staff profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_leave_requests(request):
    staff_leaves = StaffLeaveReport.objects.all()
    student_leaves = StudentLeaveReport.objects.all()
    staff_serializer = StaffLeaveReportSerializer(staff_leaves, many=True)
    student_serializer = StudentLeaveReportSerializer(student_leaves, many=True)
    
    return Response({
        'staff_leaves': staff_serializer.data,
        'student_leaves': student_serializer.data,
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_leave(request, leave_id, leave_type):
    if leave_type == 'staff':
        leave = get_object_or_404(StaffLeaveReport, id=leave_id)
    else:
        leave = get_object_or_404(StudentLeaveReport, id=leave_id)
    
    leave.approved = True  # Assuming you add an 'approved' field
    leave.save()
    return Response({"message": "Leave approved successfully."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_attendance_reports(request):
    student_attendance = StudentAttendance.objects.all()
    staff_attendance = StaffAttendance.objects.all()
    student_serializer = AttendanceSerializer(student_attendance, many=True)
    staff_serializer = AttendanceSerializer(staff_attendance, many=True)

    return Response({
        'student_attendance': student_serializer.data,
        'staff_attendance': staff_serializer.data,
    }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_fee_structure(request):
    if request.method == 'GET':
        fees = StudentFee.objects.all()
        serializer = StudentFeeSerializer(fees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = StudentFeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Fee structure added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_fee_structure(request, fee_id):
    fee = get_object_or_404(StudentFee, id=fee_id)
    fee.delete()
    return Response({"message": "Fee structure deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manage_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Event updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = EventSerializer(event)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return Response({"message": "Event deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def manage_notifications(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    if request.method == 'PUT':
        notification.message = request.data.get('message', notification.message)
        notification.save()
        return Response({"message": "Notification updated successfully."}, status=status.HTTP_200_OK)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    Notification,
    ExaminationTimetable,
    StudentFeedback,
    StaffFeedback,
    ClassTimetable,
    BehaviorReport,
    Class,
    StudentEnrollment,
    Subject,
)
from .serializers import (
    NotificationSerializer,
    ExaminationTimetableSerializer,
    StudentFeedbackSerializer,
    StaffFeedbackSerializer,
    ClassTimetableSerializer,
    BehaviorReportSerializer,
    ClassSerializer,
    SubjectSerializer,
)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.delete()
    return Response({"message": "Notification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manage_exam_schedule(request):
    exams = ExaminationTimetable.objects.all()
    serializer = ExaminationTimetableSerializer(exams, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_exam_schedule(request, exam_id):
    exam = get_object_or_404(ExaminationTimetable, id=exam_id)
    if request.method == 'PUT':
        serializer = ExaminationTimetableSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Exam schedule updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = ExaminationTimetableSerializer(exam)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_exam_schedule(request, exam_id):
    exam = get_object_or_404(ExaminationTimetable, id=exam_id)
    exam.delete()
    return Response({"message": "Exam schedule deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_feedback(request):
    student_feedbacks = StudentFeedback.objects.all()
    staff_feedbacks = StaffFeedback.objects.all()
    student_serializer = StudentFeedbackSerializer(student_feedbacks, many=True)
    staff_serializer = StaffFeedbackSerializer(staff_feedbacks, many=True)
    
    return Response({
        'student_feedbacks': student_serializer.data,
        'staff_feedbacks': staff_serializer.data,
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_class_timetable(request):
    timetables = ClassTimetable.objects.all()
    serializer = ClassTimetableSerializer(timetables, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_behavior_reports(request):
    reports = BehaviorReport.objects.all()
    serializer = BehaviorReportSerializer(reports, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_class_students(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    students = StudentEnrollment.objects.filter(class_assigned=class_instance)
    student_data = [student.student_profile for student in students]  # Assuming a relationship to StudentProfile
    return Response({
        'class': class_instance.name,  # Assuming there's a name field
        'students': student_data,
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_students(request, class_id):
    students = StudentProfile.objects.filter(enrollment__class_assigned__id=class_id)
    serializer = StudentProfileSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_class_subjects(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_subjects(request, class_id):
    subjects = Subject.objects.filter(class_assigned__id=class_id)
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manage_class_attendance(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import (
    Class,
    StudentEnrollment,
    StudentAttendance,
    StaffEnrollment,
    StaffAttendance,
    StudentGrade,
    Notification,
    ClassTimetable,
    StudentFeedback,
    StudentProfile,
    StudentFee,
    ExaminationTimetable,
)
from .serializers import (
    StudentAttendanceSerializer,
    StaffAttendanceSerializer,
    StudentGradeSerializer,
    NotificationSerializer,
    ClassTimetableSerializer,
    StudentFeedbackSerializer,
    StudentProfileSerializer,
    StudentFeeSerializer,
)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_attendance(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    students = StudentEnrollment.objects.filter(class_assigned=class_instance)
    date = request.data.get('date')

    if not date:
        return Response({"error": "Date is required."}, status=status.HTTP_400_BAD_REQUEST)

    # Validate date format
    try:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({"error": "Invalid date format. Must be YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    for student in students:
        attended = request.data.get(f'attendance_{student.student_id}') == 'on'
        StudentAttendance.objects.update_or_create(
            student=student,
            class_assigned=class_instance,
            date=date_obj,
            defaults={'is_present': attended}
        )

    return Response({"message": "Attendance marked successfully."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manage_self_attendance(request, staff_id):
    staff_enrollment = get_object_or_404(StaffEnrollment, staff_id=staff_id)
    staff_profile = get_object_or_404(StaffProfile, enrollment=staff_enrollment)
    
    date = request.data.get('date')
    is_present = request.data.get('is_present') == 'on'
    
    StaffAttendance.objects.create(
        staff=staff_profile,
        date=date,
        is_present=is_present
    )
    
    return Response({"message": "Attendance marked successfully."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manage_student_marks(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def record_student_marks(request, subject_id):
    students = StudentEnrollment.objects.filter(class_assigned__subject__id=subject_id)

    for student in students:
        grade = request.data.get(f'student_{student.id}')
        if grade:  # Ensure there's a grade before creating
            try:
                student_profile = StudentProfile.objects.get(enrollment=student)
                StudentGrade.objects.create(
                    student=student_profile,
                    subject_id=subject_id,
                    grade=grade,
                    date_recorded=request.data.get('date')
                )
            except StudentProfile.DoesNotExist:
                return Response({"error": f"No profile found for student: {student.student_name}"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Marks recorded successfully."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_notifications(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_subject_timetable(request, subject_id):
    timetable = ClassTimetable.objects.filter(subject_id=subject_id)
    serializer = ClassTimetableSerializer(timetable, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_class_timetable(request, class_id):
    timetable = ClassTimetable.objects.filter(class_assigned_id=class_id)
    serializer = ClassTimetableSerializer(timetable, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_salary_particulars(request, staff_id):
    staff = get_object_or_404(StaffEnrollment, staff_id=staff_id)
    serializer = StaffEnrollmentSerializer(staff)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_student_profile(request, student_id):
    student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)

    if request.method == 'POST':
        student.address = request.data.get('address')
        student.date_of_birth = request.data.get('date_of_birth')
        student.contact_number = request.data.get('contact_number')
        student.save()
        return Response({"message": "Student profile updated successfully."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_attendance(request, student_id):
    attendance_records = StudentAttendance.objects.filter(student__student_id=student_id)
    serializer = StudentAttendanceSerializer(attendance_records, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_attendance_month(request, student_id, month, year):
    attendance_records = StudentAttendance.objects.filter(
        student__enrollment__student_id=student_id, 
        date__month=month, 
        date__year=year
    )
    serializer = StudentAttendanceSerializer(attendance_records, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_attendance_range(request, student_id, start_date, end_date):
    attendance_records = StudentAttendance.objects.filter(
        student__enrollment__student_id=student_id,
        date__range=[start_date, end_date]
    )
    serializer = StudentAttendanceSerializer(attendance_records, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_timetable(request, student_id):
    student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
    timetable = ClassTimetable.objects.filter(class_assigned=student.enrollment.class_assigned)
    serializer = ClassTimetableSerializer(timetable, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_examination_timetable(request, student_id):
    student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
    exam_timetable = ExaminationTimetable.objects.filter(class_assigned=student.enrollment.class_assigned)
    serializer = ExaminationTimetableSerializer(exam_timetable, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def staff_logout(request):
    logout(request)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manage_feedback(request, student_id):
    feedback = StudentFeedback()
    feedback.student = get_object_or_404(StudentProfile, enrollment__student_id=student_id)
    feedback.feedback_date = timezone.now()
    feedback.content = request.data.get('content')
    feedback.save()
    return Response({"message": "Feedback submitted successfully."}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_fee_particulars(request, student_id):
    fee_details = StudentFee.objects.filter(student__enrollment__student_id=student_id)
    serializer = StudentFeeSerializer(fee_details, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_logout(request):
    logout(request)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_staff_profile(request, staff_id):
    staff = get_object_or_404(StaffProfile, enrollment__staff_id=staff_id)

    serializer = StaffProfileSerializer(staff, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)