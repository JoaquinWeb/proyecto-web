# -*- coding: utf-8 -*-
{
    'name': "Inventarios",

    'summary': """
        Este modulo sirve para anotar y llevar un registro """,

    'description': """
        Modulo creado para la empresa de transporte 
    """,

    'author': "Joaquin Callejon",
    'website': "jcallejon17@alumnos.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_bodega.xml',
        'views/views_retiro.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}