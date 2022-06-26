{
    'name': 'Hospital Management System',
    'depends':['crm'],
    'data':[
        'security/hms_security.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
        'views/hms_department_views.xml',
        'views/hms_doctor_views.xml',
        'views/hms_menus.xml',
        'views/res_partner_views.xml',
        'reports/hms_templates.xml',
        'reports/hms_reports.xml',
    ]
}
