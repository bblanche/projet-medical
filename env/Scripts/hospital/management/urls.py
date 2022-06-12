from django.urls import path, include
from django.conf.urls import url
from .views import     add_admin, admin_admin, add_patient_department_admin, add_patient_admin, add_motif, payment_motif_admin, department_staff_admin, patient_department_admin, patient_department_service_receptionist, patient_department_doctor, patient_department_info, patient_info, patient_admin, service_receptionist_admin, doctor_admin, cashier_admin, principalReceptionist_admin, department_info_admin, add_cashier, add_doctor, add_service_receptionist, add_principal_receptionist, homeCashier, viewPrescriptionPatient, all_department_principal_receptionist, me_cashier, me_principal_receptionist, doctor_make_appointment, me_doctor, me_service_receptionist, receptionist_profile, department_receptionist, department_add_patients_accueil, doctor_appointments, doctor_make_prescription, doctor_patients, doctor_prescriptions, patient_informations, paymentReceiptCashier, other, paymentSortedByDepartmentCashier, addPaymentPatientDepartmentCashier, departmentCashier, patientDepartmentPrincipalReceptionist, departmentPrincipalReceptionist, parametres_profile, home, doctors_profile,patients,patients_profile_accueil,schedule,appointment,department_doctors, search, department_add_department
#department_patients,
app_name = 'management'

urlpatterns = [
    
    path('', home , name="home"),
    #path('doctors/', doctors, name="doctors"), affiche tous les docteurs de l'hopital
    
    #****************************************ROUTES LIES A L'ADMIN********************************************************#
    #---------------------DEPARTMENTS-------------------------------#
    path('admin/add_department', department_add_department, name="department_add_department_admin"), #ajouté
    path('admin/department_informations', department_info_admin, name="department_info"),
    #---------------------DEPARTMENTS-------------------------------#
   
   #---------------------STAFF-------------------------------#
    path('admin/principal_receptionist_informations', principalReceptionist_admin, name="principalReceptionist_admin"),
    path('admin/cashier_informations', cashier_admin, name="cashier_admin"),
    path('admin/doctor_informations', doctor_admin, name="doctor_admin"),
    path('admin/service_receptionist_informations', service_receptionist_admin, name="service_receptionist_admin"),
    path('admin/admin_informations', admin_admin, name="admin_admin"),
    #---------------------STAFF-------------------------------#
    #---------------------DEPARTMENTS-------------------------------#
    path('admin/departments/<int:pk>/staff', department_staff_admin, name="department_staff_admin"),
    path('admin/departments/<int:pk>/patients', patient_department_admin, name="patient_department_admin"),
    path('admin/departments/<int:pk>/payment_motif', payment_motif_admin, name="payment_motif_admin"),
    path('admin/departments/<int:pk>/payment_motif/<int:pk2>/add_motif', add_motif, name="add_motif"),
    #---------------------DEPARTMENTS-------------------------------#
    
    #---------------------PATIENTS-------------------------------#
    path('admin/patient_informations', patient_admin, name="patient_admin"),
    path('admin/patient_informations/<int:pk>/', patient_info, name="patient_info"),
    path('admin/patient_informations/<int:pk>/<int:pk2>/', patient_department_info, name="patient_department_info"),
    path('admin/patient_informations/add_patient', add_patient_admin, name="add_patient_admin"),
    path('admin/patient_informations/<int:pk>/add_department', add_patient_department_admin, name="add_patient_department_admin"),
    
    #---------------------PATIENTS-------------------------------#
    
    #---------------------ADD STAFF-------------------------------#
    path('admin/add_principal_receptionist', add_principal_receptionist, name="add_principal_receptionist"),
    path('admin/add_cashier', add_cashier, name="add_cashier"),
    path('admin/add_doctor', add_doctor, name="add_doctor"),
    path('admin/add_service_receptionist', add_service_receptionist, name="add_service_receptionist"),
    path('admin/add_admin', add_admin, name="add_admin"),
    
    #---------------------ADD STAFF-------------------------------#
    #****************************************FIN ROUTES LIES A L'ADMIN********************************************************#
    


    #****************************************ROUTES LIES A LA RECEPTIONNISTE DU SERVICE********************************************************#
    #---------------------docteur-------------------------------#
    path('nurse/doctors/', department_doctors, name="department_doctors"), #ajouté
    path('nurse/doctors/profile/<int:pk>/', doctors_profile, name="doctors_profile"),
    #---------------------docteur-------------------------------#
   
   #---------------------receptionists-------------------------------#
    path('nurse/receptionists/', department_receptionist, name="department_receptionist"), #ajouté
    path('nurse/receptionists/profile/<int:pk>/', receptionist_profile, name="receptionist_profile"),
    #---------------------receptionists-------------------------------#
    
    #---------------------me-------------------------------#
    path('nurse/my_profile_Service_receptionist/', me_service_receptionist, name="meServiceReceptionist"), #ajouté
    #logout
    #---------------------me-------------------------------#
    
    

    #---------------------patient-------------------------------#
    path('nurse/patients/', patients, name="department_patients"),
    path('nurse/addpatients/', department_add_patients_accueil, name="department_add_patients"),
    #path('patients/add', add_patients, name="add_patients"),
    path('nurse/patients/profile/modifyprofile/<int:pk>/', patients_profile_accueil, name="patients_profile"),
    
    path('nurse/patients/patient_department_service_receptionist/<int:pk>/', patient_department_service_receptionist, name="patient_department_service_receptionist"),
    path('nurse/patients/profile/other/<int:pk>/<int:pk2>/', other, name="other_profile"),
    path('nurse/patients/profile/parameters/<int:pk>/', parametres_profile, name="parametres_profile"),#---------------------patient-------------------------------#
    #path('doctors/add/', add_doctors, name="add_doctors"),-----------------pour l'admin
    #---------------------patient-------------------------------#
    path('home/', home , name="homeReceptionist"),
    
    
    #---------------------appointment-------------------------------#
    path('nurse/appointment/', appointment , name="appointment"),
    path('nurse/schedule/', schedule , name="schedule"),
    #---------------------appointment-------------------------------#
    #****************************************FIN ROUTES LIES A LA RECEPTIONNISTE DU SERVICE********************************************************#
    
    #****************************************ROUTES LIES A LA RECEPTIONNISTE D'ACCUEIL********************************************************#
    path('principalReceptionist/department/', all_department_principal_receptionist , name="all_department_principal_receptionist"),
    path('principalReceptionist/department/<int:pk>/', departmentPrincipalReceptionist , name="department_principal_receptionist"),
    path('principalReceptionist/patient/department/<int:pk>/', patientDepartmentPrincipalReceptionist , name="patient_department_principal_receptionist"),
    #---------------------me-------------------------------#
    path('my_profile_principal_receptionist/', me_principal_receptionist, name="mePrincipalReceptionist"), #ajouté
    #logout
    #---------------------me-------------------------------#
    


    #****************************************FIN ROUTES LIES A LA RECEPTIONNISTE D'ACCUEIL********************************************************#
    
    #****************************************ROUTES LIES A LA CAISSIERE********************************************************#
    path('cashier/department/<int:pk>/', departmentCashier, name="department_cashier"),
    path('cashier/department/patient/<int:pk>', addPaymentPatientDepartmentCashier, name="add_payment_patient_department_cashier"),
    path('cashier/department/informations/sortedByDepartment', paymentSortedByDepartmentCashier, name="payment_sorted_by_department_cashier"),
    path('cashier/department/informations/paymentReceipt/<int:pk>', paymentReceiptCashier, name="payment_receipt_cashier"),
    

    #---------------------me-------------------------------#
    path('my_profile_cashier/', me_cashier, name="meCashier"), #ajouté
    #logout
    #---------------------me-------------------------------#
    

    #****************************************FIN ROUTES LIES A LA CAISSIERE********************************************************#
    
    
    #****************************************ROUTES LIES AU DOCTEUR********************************************************#
    path('doctorAppointments/', doctor_appointments , name="doctorAppointments"),
    path('doctorPatients/', doctor_patients , name="doctorPatients"),
    path('doctorMakePrescription/<int:pk>/', doctor_make_prescription , name="doctorMakePrescriptions"),
    path('doctorPrescriptions/', doctor_prescriptions , name="doctorPrescriptions"),
    path('doctorPatients/patient_department/<int:pk>/', patient_department_doctor, name="patient_department_doctor"),
    
    path('doctorPatients/patient_department/informations/<int:pk>/<int:pk2>', patient_informations, name="informations"),
    path('patients/prescriptions/<int:pk>/', viewPrescriptionPatient, name="view_prescription_patient"),
    path('doctorMakePrescription/', doctor_make_appointment , name="doctorMakeAppointment"),
    #---------------------me-------------------------------#
    path('my_profile_doctor/', me_doctor, name="meDoctor"), #ajouté
    #logout
    path('homecashier/', homeCashier, name="home_cashier"), #ajouté
    #---------------------me-------------------------------#
    #****************************************FIN ROUTES LIES AU DOCTEUR********************************************************#
     



        ##########################principal RECEPTIONIST#######################

    #path('', index , name="index"),
    #path('home/', homePrincipalReceptionnist , name="homePrincipalReceptionist"),
    #path('<name>/info/', department_info, name="department_info"),
    #path('all_patients/', all_patients , name="all_patients"),
    path('search/', search , name="search"),
#############################################################################
    
    #path('add_payments/', add_payments , name="add_payments"),
    #path('payments/', payments , name="payments"),
    #path('departments/', departments, name="departments"),
    
    path('search/', search, name="search"),
    #path('department/', department, name="department"),
    #path('patients/', department_patients, name="department_patients"),
    
    
]