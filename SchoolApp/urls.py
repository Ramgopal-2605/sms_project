from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path




# Initialize the router
router = DefaultRouter()
# router.register(r'classes', ClassViewSet, basename='class')
# router.register(r'subjects', SubjectViewSet, basename='subject')
# router.register(r'notifications', NotificationViewSet, basename='notification')
# router.register(r'students', StudentProfileViewSet, basename='student')
# router.register(r'staff', StaffProfileViewSet, basename='staff')
# router.register(r'feedback', StudentFeedbackViewSet, basename='feedback')
# router.register(r'behavior-reports', BehaviorReportViewSet, basename='behavior_report')
# router.register(r'grades', StudentGradeViewSet, basename='grade')

urlpatterns = [
    # path('api/register/', AdminRegistrationView.as_view(), name='registration'),
    # path('api/login/', LoginView.as_view(), name='login'),
    # path('api/student/enroll/', EnrollStudentView.as_view(), name='enroll_student'),
    # path('api/staff/enroll/', EnrollStaffView.as_view(), name='enroll_staff'),
    # path('api/', include(router.urls)),
    path('register/', admin_registration, name='registration'),
    path('index/', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student/enroll/', enroll_student_view, name='enroll_student'),
    path('staff/enroll/', enroll_staff_view, name='enroll_staff'),
    path('classes/manage/', manage_classes_view, name='manage_classes'),
    path('classes/delete/<int:class_id>/', delete_class_view, name='delete_class'),
    path('subjects/manage/', manage_subjects_view, name='manage_subjects'),
    path('subjects/delete/<int:subject_id>/', delete_subject_view, name='delete_subject'),
    path('class/timetable/manage/', manage_class_timetable_view, name='manage_class_timetable'),
    path('class/timetable/delete/<int:timetable_id>/', delete_class_timetable_view, name='delete_class_timetable'),
    path('attendance/manage/', manage_attendance_view, name='manage_attendance'),
    path('attendance/delete/<int:attendance_id>/', delete_attendance_view, name='delete_attendance'),
    path('leaves/manage/', manage_leaves_view, name='manage_leaves'),
    path('notification/create/', create_notification_view, name='create_notification'),
    path('notifications/manage/', manage_notifications_view, name='manage_notifications'),
    path('fees/monitor/', monitor_fees_view, name='monitor_fees'),
    path('fee/report/', fee_report_view, name='fee_report'),
    path('fee/report/<str:student_id>/', fee_report_view, name='fee_report'),
    path('exam/schedule/', schedule_exam_view, name='schedule_exam'),
    path('exam/update/<int:exam_id>/', update_exam_view, name='update_exam'),
    path('exam/delete/<int:exam_id>/', delete_exam_view, name='delete_exam'),
    path('exam/review/', review_exam_results_view, name='review_exam_results'),
    path('exam/report/generate/', generate_exam_report_view, name='generate_exam_report'),
    path('student/edit/<int:student_id>/', edit_student_profile, name='edit_student'),
    path('student/delete/<int:student_id>/', delete_student_profile, name='delete_student'),
    path('staff/manage/', manage_staff_profiles, name='manage_staff'),
    path('staff/edit/<int:staff_id>/', edit_staff_profile, name='edit_staff'),
    path('staff/delete/<int:staff_id>/', delete_staff_profile, name='delete_staff'),
    path('leaves/view/', view_leave_requests, name='view_leave_requests'),
    path('leaves/approve/<int:leave_id>/', approve_leave, name='approve_leave'),
    path('attendance/reports/', view_attendance_reports, name='view_attendance_reports'),
    path('fees/manage/', manage_fee_structure, name='manage_fee_structure'),
    path('fees/delete/<int:fee_id>/', delete_fee_structure, name='delete_fee_structure'),
    path('events/manage/', manage_events, name='manage_events'),
    path('event/edit/<int:event_id>/', edit_event, name='edit_event'),
    path('event/delete/<int:event_id>/', delete_event, name='delete_event'),
    path('notifications/edit/<int:notification_id>/', edit_notification, name='edit_notification'),
    path('notifications/delete/<int:notification_id>/', delete_notification, name='delete_notification'),
    path('exam/manage/', manage_exam_schedule, name='manage_exam_schedule'),
    path('exam/edit/<int:exam_id>/', edit_exam_schedule, name='edit_exam_schedule'),
    path('exam/delete/<int:exam_id>/', delete_exam_schedule, name='delete_exam_schedule'),
    path('feedback/view/', view_feedback, name='view_feedback'),
    path('class/timetable/generate/', generate_class_timetable, name='generate_class_timetable'),
    path('behavior/reports/view/', view_behavior_reports, name='view_behavior_reports'),
    #staff urls
    path('staff/update/<str:staff_id>/', update_staff_profile, name='update_staff_profile'),
    path('class/<int:class_id>/students/', view_class_students, name='view_class_students'),
    path('class/<int:class_id>/students/view/', class_students, name='class_students'),
    path('class/<int:class_id>/subjects/', view_class_subjects, name='view_class_subjects'),
    path('class/<int:class_id>/subjects/view/', class_subjects, name='class_subjects'),
    path('attendance/manage/class/', manage_class_attendance, name='manage_class_attendance'),
    path('attendance/mark/<int:class_id>/', mark_attendance, name='mark_attendance'),
    path('attendance/self/', manage_self_attendance, name='manage_self_attendance'),
    path('attendance/self/<str:staff_id>/', manage_self_attendance, name='manage_self_attendance'),
    path('marks/manage/', manage_student_marks, name='manage_student_marks'),
    path('marks/record/<int:subject_id>/', record_student_marks, name='record_student_marks'),
    path('notifications/view/', view_notifications, name='view_notifications'),
    path('subject/timetable/<int:subject_id>/', view_subject_timetable, name='view_subject_timetable'),
    path('class/timetable/<int:class_id>/', view_class_timetable, name='view_class_timetable'),
    path('salary/particulars/<str:staff_id>/', view_salary_particulars, name='view_salary_particulars'),
    path('staff/logout/', staff_logout, name='staff_logout'),
    #students urls
    path('student/update/<str:student_id>/', update_student_profile, name='update_student_profile'),
    path('attendance/view/<str:student_id>/', view_attendance, name='view_attendance'),
    path('attendance/view/<str:student_id>/month/<int:month>/<int:year>/', view_attendance_month, name='view_attendance_month'),
    path('attendance/view/<str:student_id>/range/<str:start_date>/<str:end_date>/', view_attendance_range, name='view_attendance_range'),
    path('timetable/view/<str:student_id>/', view_timetable, name='view_timetable'),
    path('exam/timetable/view/<str:student_id>/', view_examination_timetable, name='view_examination_timetable'),
    #path('notifications/view/student/<str:student_id>/', view_notifications, name='view_notifications'),
    path('feedback/manage/<str:student_id>/', manage_feedback, name='manage_feedback'),
    path('fees/view/<str:student_id>/', view_fee_particulars, name='view_fee_particulars'),
    path('student/logout/', student_logout, name='student_logout'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('student/urls/', student_urls, name='student_urls'),  # New URL for student URLs
    path('staff-urls', staff_urls, name='staff_urls'), 
    #path('add-class/', add_class, name='add_class'),
    # path('view-classes/', view_classes, name='view_classes'),
    # path('update-class/<str:class_id>/', update_class, name='update_class'),  # URL for updating a class
    # path('delete-class/<str:class_id>/', delete_class, name='delete_class'),  # URL for deleting a class
    
#
]