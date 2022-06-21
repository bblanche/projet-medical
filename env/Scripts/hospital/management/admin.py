from django.contrib import admin
from .models import Nurse, Admins, PaymentMotif, PatientDepartments, Prescriptions, Cashier, PrincipalReceptionist, ServiceReceptionist, Parameters, Departments, Doctors, Patients, Appointments, DoctorsSchedule, Payments
# Register your models here.

class AdminAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation']
    search_fields = ('first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class ServiceReceptionistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class NurseAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'department', 'is_active', 'activate_by_admin', 'user', 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'principal_receptionist', 'marital_status', 'location', 'profession', 'date_creation']
    search_fields = ('first_name', 'last_name', 'principal_receptionist', 'marital_status', 'location', 'profession', 'date_creation')

class ParametersAdmin(admin.ModelAdmin):
    list_display = ['blood_pressure', 'pulse', 'breathing_rate', 'heart_rate', 'weight', 'height', 'blood_sugar', 'temperature', 'department', 'nurse', 'patient', 'date_creation']
    search_fields = ('blood_pressure', 'pulse', 'breathing_rate', 'heart_rate', 'weight', 'height', 'blood_sugar', 'temperature', 'department', 'nurse', 'patient' , 'date_creation')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['date_appointment', 'patient', 'service_receptionist', 'doctor', 'state', 'date_creation']
    search_fields = ('date_appointment', 'patient', 'service_receptionist', 'doctor', 'state', 'date_creation')

class PatientDepartmentsAdmin(admin.ModelAdmin):
    list_display = [ 'patient', 'department', 'has_paid']
    search_fields = ( 'patient', 'department', 'has_paid')



class PrincipalReceptionnistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active', 'activate_by_admin', 'user'  , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

class CashierAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active', 'activate_by_admin', 'user'  , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation' ]
    search_fields = ('first_name', 'last_name', 'is_active', 'activate_by_admin', 'user' , 'gender', 'marital_status', 'date_of_birth','email','phone','location', 'date_creation')

    
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['cashier', 'patientDepartment', 'motif', 'payment_method', 'valid']
    search_fields = ('cashier', 'patientDepartment', 'motif', 'payment_method', 'valid')

class PaymentMotifAdmin(admin.ModelAdmin):
    list_display = ['payment_motif', 'amount_motif','department']
    search_fields = ('payment_motif', 'amount_motif','department')

    
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient','department', 'doctor', 'symptoms', 'drug_prescription', 'examinations', 'recommendations', 'prescripted_date']
    search_fields = ('patient','department', 'doctor', 'symptoms', 'drug_prescription', 'examinations', 'recommendations', 'prescripted_date')

admin.site.register(Departments)
admin.site.register(Admins, AdminAdmin)
admin.site.register(Doctors, DoctorAdmin)
admin.site.register(ServiceReceptionist, ServiceReceptionistAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(PrincipalReceptionist, PrincipalReceptionnistAdmin)
admin.site.register(Patients, PatientAdmin)
admin.site.register(Appointments, AppointmentAdmin)
admin.site.register(DoctorsSchedule)
admin.site.register(Payments, PaymentsAdmin)
admin.site.register(Parameters, ParametersAdmin)
admin.site.register(Cashier, CashierAdmin)
admin.site.register(Prescriptions, PrescriptionAdmin)
admin.site.register(PaymentMotif, PaymentMotifAdmin)
admin.site.register(PatientDepartments, PatientDepartmentsAdmin)

