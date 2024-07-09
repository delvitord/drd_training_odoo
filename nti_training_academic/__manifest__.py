# -*- coding: utf-8 -*-
{
    'name': "Training Academic (Delvito)",

    'summary': """
        Subject, Class, Student, Lecturer, Schedule Management""",

    'description': """
        This module is used to manage academic, including subject, class, student, lecturer, and schedule management.
    """,

    'author': "NTI",
    'website': "http://www.nti.co.id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academic',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml'    ,
        'views/class_view.xml',
        'views/subject_view.xml',
        'views/subject_line_view.xml',
        'reports/class_report.xml',
        'views/menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
