# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    enable_default_discount = fields.Boolean()
    default_discount = fields.Float(string="Default Discount %")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    default_discount = fields.Float(string="Default Discount %")
    enable_default_discount = fields.Boolean(related="partner_id.enable_default_discount")

    @api.onchange("partner_id")
    def set_default_discount(self):
        if self.env.user.has_group(
                'product.group_discount_per_so_line') and self.partner_id and self.enable_default_discount:
            self.default_discount = self.partner_id.default_discount
        else:
            self.default_discount = 0


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("product_id")
    def set_default_discount(self):
        if self.product_id and self.env.user.has_group('product.group_discount_per_so_line'):
            self.discount = self.order_id.default_discount
        else:
            self.discount = 0


class AccountMove(models.Model):
    _inherit = "account.move"

    default_discount = fields.Float(string="Default Discount %")
    enable_default_discount = fields.Boolean(related="partner_id.enable_default_discount")

    @api.onchange("partner_id")
    def set_default_discount(self):
        if self.env.user.has_group(
                'product.group_discount_per_so_line') and self.partner_id and self.enable_default_discount:
            self.default_discount = self.partner_id.default_discount
        else:
            self.default_discount = 0


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.onchange("product_id")
    def set_default_discount(self):
        if self.product_id and self.env.user.has_group('product.group_discount_per_so_line'):
            self.discount = self.move_id.default_discount
        else:
            self.discount = 0
