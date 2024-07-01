# -*- coding: utf-8 -*-
{
    'name': "Training Odoo (Delvito)",

    'summary': """
        This module provides training materials and resources for learning Odoo. It includes various views for managing bus schedules, HR employees, and menu items.""",
        
    'description': """
        The module provides training materials and resources for learning Odoo. It includes various views for managing bus schedules, HR employees, and menu items. It also allows users to view and manage passenger information, bus details, and bus routes. This module is designed to enhance the transportation management capabilities of Odoo and improve the overall efficiency of transportation operations.
    """,

    'author': "Delvito Rahim Derivansyah",
    'website': "https://github.com/delvitord",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Transportation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/passenger_view.xml',
        'views/bus_schedule_view.xml',
        'views/bus_view.xml',
        'views/bus_route_view.xml',
        'views/hr_employee_view.xml',
        'views/menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
