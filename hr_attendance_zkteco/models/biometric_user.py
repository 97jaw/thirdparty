# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError, UserError
from datetime import date, datetime, timedelta
_logger = logging.getLogger(__name__)

class EmployeeAttendanceDevices(models.Model):
    _name = 'employee.attendance.devices'
    _description = 'Employee Attendance Devices'
    _order = 'name'

    name = fields.Char(string='Name')
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee')
    # location_id = fields.Many2one(related='employee_id.location_id', store=True)
    attendance_id = fields.Char("Biometric ID", required=True)
    device_id = fields.Many2one(comodel_name='biomteric.device.info', string='Biometric Device', required=True, ondelete='cascade')
    card_number = fields.Char(string="RFID Number")
    access_type = fields.Selection([('14','ADMIN'),
                                    ('0','USER')], string="Access")
    new_biometric_id = fields.Integer(string="New Biometric ID")
    active = fields.Boolean('Active', default=True)

    @api.constrains('attendance_id', 'device_id', 'name')
    def _check_unique_constraint(self):
        for rec in self:
            record = self.search([('attendance_id', '=', rec.attendance_id), ('device_id', '=', rec.device_id.id)])
            if len(record) > 1:
                raise ValidationError('Employee with Id ('+ str(rec.attendance_id)+') exists on Device ('+ str(rec.device_id.name)+') !')
            record = self.search([('name', '=', rec.employee_id.id), ('device_id', '=', rec.device_id.id)])
            if len(record) > 1:
                raise ValidationError('Configuration for Device ('+ str(rec.device_id.name)+') of Employee  ('+ str(rec.name.name)+') already exists!')

    def unlink(self):
        active_id = self.device_id
        try:
            conn = active_id._connect_device()
            for rec in self:
                conn.delete_user(uid=int(rec.attendance_id))
        except Exception as e:
            _logger.info(Warning(e))
        conn.disconnect()
        return super(EmployeeAttendanceDevices, self).unlink()
