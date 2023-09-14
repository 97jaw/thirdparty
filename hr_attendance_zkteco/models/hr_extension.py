# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError, UserError
from datetime import date, datetime, timedelta
_logger = logging.getLogger(__name__)
# from odoo.addons.fgp_base.models.method import POST_ADMIN_CHANNEL


class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    last_draft_attendance_id = fields.Many2one('hr.draft.attendance', compute='_compute_last_draft_attendance_id')
    attendance_devices = fields.One2many('employee.attendance.devices', 'employee_id', string='Attendance Devices')

    def _compute_last_draft_attendance_id(self):
        for employee in self:
            draft_atts = self.env['hr.draft.attendance'].search([('employee_id','=',employee.id)], order='name desc')
            employee.last_draft_attendance_id = draft_atts.ids

    @api.depends('last_draft_attendance_id.attendance_status', 'last_draft_attendance_id', 'last_attendance_id.check_in', 'last_attendance_id.check_out', 'last_attendance_id')
    def _compute_attendance_state(self):
        for employee in self:
            if employee.last_attendance_id and not self.env['hr.draft.attendance'].search([('moved_to','=',employee.last_attendance_id.id),
                                                                                           ('employee_id','=',employee.id)]):
                att = employee.last_attendance_id.sudo()
                employee.attendance_state = att and not att.check_out and 'checked_in' or 'checked_out'
            else:
                attendance_state = 'checked_out'
                if employee.last_draft_attendance_id and employee.last_draft_attendance_id.attendance_status == 'sign_in':
                    attendance_state = 'checked_in'
                employee.attendance_state = attendance_state

