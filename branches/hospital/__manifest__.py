{
    'name': 'Hospital Management System',
    'author': 'eya',
    'version': '1.0',
    'summary': 'Hospital Management System',
    'sequence': 1,
    'category': 'Hospital',
    'website': 'https://hospital.com',
    'depends': ['base', 'mail', 'account', 'sale'],
    'data': [
        "data/sequence.xml",
        "views/patient.xml",
        "views/doctor.xml",
        "views/invoice.xml",
        "views/menu.xml",
        "report/patient_report.xml",
        "report/patient_template.xml"
    ],
    'installable': True,
    'auto_install': True,
}
