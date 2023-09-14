# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError, UserError
from datetime import date, datetime, timedelta
_logger = logging.getLogger(__name__)


class hrDraftAttendance(models.Model):
    _name = 'hr.draft.attendance'
    _description = 'Biometric Logs'
    # _inherit = ['portal.mixin','mail.thread', 'mail.activity.mixin']
    _inherit = ['portal.mixin', 'mail.thread.cc', 'mail.activity.mixin', 'rating.mixin']
    _order = 'name desc'

    name = fields.Datetime('Datetime', required=False,tracking=True)
    date = fields.Date('Date', required=False,tracking=True)
    day_name = fields.Char('Day',tracking=True)
    attendance_status = fields.Selection([('sign_in', 'Sign In'), ('sign_out', 'Sign Out'), ('sign_none', 'None')], 'Attendance State', required=True,tracking=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee',tracking=True)
    lock_attendance = fields.Boolean('Lock Attendance',tracking=True)
    biometric_attendance_id = fields.Integer(string='Biometric Attendance ID',tracking=True)
    is_missing = fields.Boolean('Missing', default=False,tracking=True)
    moved = fields.Boolean(default=False)
    moved_to = fields.Many2one(comodel_name='hr.attendance', string='Moved to HR Attendance')
    device_id = fields.Many2one(comodel_name='biomteric.device.info', string='Device')
    cron_activity = fields.Boolean(string="Cron Activity")

    def unlink(self):
        for rec in self:
            if rec.moved == True:
                if rec.moved_to:
                    raise UserError(_("You can`t delete Moved Attendance"))
        return super(hrDraftAttendance, self).unlink()

    def action_invalidate_log(self):
        for rec in self:
            rec.moved = True

    def action_force_sync(self):
        messages = ""
        for rec in self.sorted(key=lambda l: l.name):
            hr_attendance = self.env['hr.attendance']
            if rec.attendance_status == 'sign_in':
                vals = {
                    'employee_id': rec.employee_id.id,
                    'check_in': rec.name,
                }
                hr_attendance  = hr_attendance.sudo().create(vals)
            elif rec.attendance_status == 'sign_out':
                hr_attendance = hr_attendance.sudo().search(
                    [('employee_id', '=', rec.employee_id.id), ('check_out', '=', False)],limit=1)

                hr_attendance.sudo().write({'check_out': rec.name})

            if hr_attendance:
                # rec.moved = True
                rec.sudo().write({
                    'moved': True,
                    'moved_to': hr_attendance.id,
                })

                messages += "<p>%s <a href=# data-oe-model=%s data-oe-id=%d>%s</a></p>" % (rec.employee_id.name, rec._name, rec.id, rec.name)

        subject = "Force Sync Created"
        message = "<p>Force Sync Created for:</p>" + messages
        # POST_ADMIN_CHANNEL(self, subject, message)

    def action_mark_activity_done(self):
        for rec in self.activity_ids:
            if rec.user_id.id == self.env.user.id:
                rec.action_feedback("Done")
