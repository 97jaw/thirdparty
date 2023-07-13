# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd
#    (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields


class Users(models.Model):
    _inherit = 'res.users'

    allowed_location_ids = fields.Many2many('stock.location', string='Locations')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: