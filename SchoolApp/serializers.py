from rest_framework import serializers
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


class AdminPrincipalRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminPrincipalRegistration
        fields = ['AdminName', 'Adminid', 'pwd']

    

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_name', 'class_assigned']


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = ['student_name', 'student_id', 'student_pwd', 'father_name', 'mother_name', 'class_assigned', 'enrollment_date', 'fee_details']


class StaffEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffEnrollment
        fields = ['staff_name', 'staff_id', 'staff_pwd', 'subject_assigned', 'date_of_hire', 'designation', 'category', 'salary']


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['enrollment', 'date_of_birth', 'address', 'image', 'contact_number']


class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = ['enrollment', 'experience_in_years', 'image', 'address', 'date_of_birth', 'married_status']


class StudentFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFee
        fields = ['student', 'amount_due', 'amount_paid', 'installments', 'due_date']


class StaffSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffSalary
        fields = ['staff', 'amount', 'payment_date']


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'date', 'is_present', 'reason']


class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = ['student', 'class_assigned', 'date', 'is_present', 'reason']


class StaffAttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendanceReport
        fields = ['staff', 'attendance_date_range_start', 'attendance_date_range_end', 'total_present_days', 'total_absent_days']


class StudentAttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendanceReport
        fields = ['student', 'attendance_date_range_start', 'attendance_date_range_end', 'total_present_days', 'total_absent_days']


class StaffLeaveReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLeaveReport
        fields = ['staff', 'leave_start_date', 'leave_end_date', 'reason']


class StudentLeaveReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLeaveReport
        fields = ['student', 'leave_start_date', 'leave_end_date', 'reason']


class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback
        fields = ['student', 'feedback_date', 'content']


class StaffFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffFeedback
        fields = ['staff', 'feedback_date', 'content']


class StudentGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGrade
        fields = ['student', 'subject', 'grade', 'date_recorded']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'participants']


class ExtracurricularActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularActivity
        fields = ['name', 'description', 'participants']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'date_sent', 'is_read']


class ClassTimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTimetable
        fields = ['class_assigned', 'subject', 'staff', 'day_of_week', 'start_time', 'end_time']


class ExaminationTimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationTimetable
        fields = ['name_of_exam', 'subject', 'exam_date', 'start_time', 'end_time', 'class_assigned']


class CounselingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingSession
        fields = ['student', 'date', 'counselor', 'notes']


class BehaviorReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BehaviorReport
        fields = ['student', 'report_date', 'description', 'action_taken']


class CertificateRequestsStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateRequestsStudent
        fields = ['student', 'certificate_type', 'request_date']

from rest_framework import serializers
from .models import (
    StudentAttendance,
    StaffAttendance,
    StudentFee,
    StaffSalary,
    Notification,
    StudentFeedback,
    StaffFeedback,
    StudentLeaveReport,
    StaffLeaveReport,
    AdminPrincipalRegistration,
)

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance  # Adjust if using StaffAttendance separately
        fields = ['student', 'class_assigned', 'date', 'is_present', 'reason']

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFee
        fields = ['student', 'amount_due', 'amount_paid', 'installments', 'due_date']

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationTimetable  # Adjust based on your actual exam model
        fields = ['name_of_exam', 'subject', 'exam_date', 'start_time', 'end_time', 'class_assigned']

class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminPrincipalRegistration
        fields = ['AdminName', 'Adminid', 'pwd']

    def create(self, validated_data):
        admin = AdminPrincipalRegistration(**validated_data)
        admin.set_password(validated_data['pwd'])  # Hash the password if needed
        admin.save()
        return admin

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        # Implement your login logic here
        return attrs

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback  # Adjust for StaffFeedback if needed
        fields = ['student', 'feedback_date', 'content']

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLeaveReport  # Adjust if you need to differentiate staff/student leave
        fields = ['student', 'leave_start_date', 'leave_end_date', 'reason']

from rest_framework import serializers
from .models import StudentEnrollment, StaffEnrollment

class EnrollStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = [
            'student_name',
            'student_id',
            'student_pwd',
            'father_name',
            'mother_name',
            'class_assigned',
            'enrollment_date',
            'fee_details'
        ]

    def create(self, validated_data):
        student = StudentEnrollment(**validated_data)
        student.set_password(validated_data['student_pwd'])  # Hash the password if needed
        student.save()
        return student

class EnrollStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffEnrollment
        fields = [
            'staff_name',
            'staff_id',
            'staff_pwd',
            'subject_assigned',
            'date_of_hire',
            'designation',
            'category',
            'salary'
        ]

    def create(self, validated_data):
        staff = StaffEnrollment(**validated_data)
        staff.set_password(validated_data['staff_pwd'])  # Hash the password if needed
        staff.save()
        return staff
