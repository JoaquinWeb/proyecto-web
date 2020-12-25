# -*- coding: utf-8 -*-
{
    'name': "gep",

    'summary': """
       Modulo de Gestion de proyectos""",

    'description': """
        Sistema que permite llevar control de las mantenciones realizadas
    """,


    'author': "Gaston Latorre Bariggi",
    'website': "gastonlatorrebariggi@gmail.com",

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
        'views/views_cliente.xml',
        'views/views_evaluacion.xml',
        'views/views_proyecto.xml',
        'views/templates.xml',
    ],
    
}