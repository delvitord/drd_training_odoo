# -*- coding: utf-8 -*-
{
    'name': "Training Odoo (Delvito)",

    'summary': """
        Training Odoo by Delvito""",

    'description': """
        This module provides training materials and resources for learning Odoo. It includes various views for managing bus schedules, HR employees, and menu items. It depends on the 'base' and 'hr' modules. The module also includes security settings and a demonstration mode with demo data.
    """,

    'author': "Delvito Rahim Derivansyah",
    'website': "https://github.com/delvitord",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bus_schedule_view.xml',
        'views/menuitem.xml',
        'views/hr_employee_view.xml',
        'views/passenger_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
