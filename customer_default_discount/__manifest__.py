# -*- coding: utf-8 -*-
{
    'name': "Customer Based Discount",

    'summary': """Customer Based Discount on Sales and Invoice""",

    'description': """Customer Based Discount or Customer Default Discount module will help you to set default and 
    specific discount for customers and that discount will apply on sale orders and invoices. You can also set a 
    different discount then the default discount for a order or invoice  also. It will be more handy to apply discounts 
    for your customers. 
    Default sales discount""",

    'author': 'Azkob',
    'category': 'Sales',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'price': 0,
    'currency': 'EUR',
}
