from django.db import models


class AdminPrincipalRegistration(models.Model):
    AdminName = models.CharField(max_length=50)
    Adminid = models.CharField(unique=True, max_length=100)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return self.AdminName


class Class(models.Model):
    class_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return f"{self.class_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
    class Meta:
        unique_together = ('subject_name', 'class_assigned')

class StudentEnrollment(models.Model):
    student_name = models.CharField(max_length=255)
    student_id = models.CharField(unique=True, max_length=255)
    student_pwd = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    fee_details = models.DecimalField(max_digits=10, decimal_places=2)


class StaffEnrollment(models.Model):
    staff_name = models.CharField(max_length=255)
    staff_id = models.CharField(unique=True, max_length=255)
    staff_pwd = models.CharField(max_length=255)
    subject_assigned = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    date_of_hire = models.DateField()
    designation = models.CharField(max_length=255)
    category = models.BooleanField(choices=[(True, 'Teaching Staff'), (False, 'Non-Teaching Staff')])
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class StudentProfile(models.Model):
    enrollment = models.OneToOneField(StudentEnrollment, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()
    image = models.ImageField(upload_to='student_img/')
    contact_number = models.CharField(max_length=15)

class StaffProfile(models.Model):
    enrollment = models.OneToOneField(StaffEnrollment, on_delete=models.CASCADE)
    experience_in_years = models.IntegerField()
    image = models.ImageField(upload_to='staff_img/')
    address = models.TextField()
    date_of_birth = models.DateField()
    married_status = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])

class Parent(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

class StudentFee(models.Model):
    student = models.ForeignKey(StudentEnrollment, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    installments = models.IntegerField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.student.student_name} - Due: {self.amount_due}, Paid: {self.amount_paid}"

class StaffSalary(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

class StaffAttendance(models.Model):
    staff = models.ForeignKey(StaffEnrollment, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    reason = models.TextField(null=True, blank=True)

class StudentAttendance(models.Model):
    student = models.ForeignKey(StudentEnrollment, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    reason = models.TextField(null=True, blank=True)

class StaffAttendanceReport(models.Model):
    staff = models.ForeignKey(StaffEnrollment, on_delete=models.CASCADE)
    attendance_date_range_start = models.DateField()
    attendance_date_range_end = models.DateField()
    total_present_days = models.IntegerField()
    total_absent_days = models.IntegerField()

class StudentAttendanceReport(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    attendance_date_range_start = models.DateField()
    attendance_date_range_end = models.DateField()
    total_present_days = models.IntegerField()
    total_absent_days = models.IntegerField()

class StaffLeaveReport(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    reason = models.TextField()

class StudentLeaveReport(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    reason = models.TextField()

class StudentFeedback(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    feedback_date = models.DateField()
    content = models.TextField()

class StaffFeedback(models.Model):
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    feedback_date = models.DateField()
    content = models.TextField()

class StudentGrade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    date_recorded = models.DateField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    participants = models.ManyToManyField(StudentProfile, blank=True)

class ExtracurricularActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.ManyToManyField(StudentProfile, blank=True)

class Notification(models.Model):
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class ClassTimetable(models.Model):
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffEnrollment, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

class ExaminationTimetable(models.Model):
    name_of_exam = models.CharField(max_length=225)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)

class CounselingSession(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    counselor = models.ForeignKey(StaffProfile, on_delete=models.SET_NULL, null=True)
    notes = models.TextField()

class BehaviorReport(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    report_date = models.DateField()
    description = models.TextField()
    action_taken = models.TextField()

class CertificateRequestsStudent(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=255)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.certificate_type} requested by {self.student.student_name} on {self.request_date}"

