# -*- coding: utf-8 -*-
{
    'name': 'Ihsan Base',
    'version': '11.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 1,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'author': 'Alhasan',
    'website': 'http://www.ihsanmallorca.es',
    'depends': ['openeducat_core'],
    'data': [
        'security/ihsan_base_security.xml',
        'security/ir.model.access.csv',
        'data/ihsan_base_lang_level.xml',
        'views/ihsan_base_student_view.xml',
        'menu/ihsan_base_hidden_menu.xml'
    ],
    'demo': [

    ],
    'test': [

    ],
    'css': [],
    'qweb': [

    ],
    'js': [],
    'images': [
    
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
