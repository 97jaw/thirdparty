# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'User Warehouse Location own Access',
    'version': '16.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Warehouse',
    'description':
        """
This Module add below functionality into odoo

        1.Using this odoo application you can control which user can use which warehouse location\n

odoo app allow to access own Warehouse Location only, control warehouse location by user, warehouse location restrict, user warehouse location, user own location, user available location, user access location, user stock location, stock location by user, own warehouse location

    """,
    'summary': 'odoo app allow user to access own Warehouse Location only, control warehouse location by user, warehouse location restrict, user warehouse location, user own location, user available location, user access location, user stock location, stock location by user, own warehouse location',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['stock'],
    'data': [
        'security/security.xml',
        'views/users_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':11.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/BxDjiPy_jHo',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
