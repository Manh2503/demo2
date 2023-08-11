from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class Detail(models.Model):
    _name = "detail.purchase"
    _description = "detail puchase model"

    product = fields.Text(string='Sản phẩm', required=True)
    quantity = fields.Float(string='Số lượng sản phẩm', required=True)
    unit_price = fields.Float(string="Đơn giá", required=True)
    product_money = fields.Float(string='Số tiền sản phẩm',compute='_product_money',store=True)
    purchase_id = fields.Many2one('purchase')

    @api.depends('quantity', 'unit_price')
    def _product_money(self):
        for rec in self:
            rec.product_money = rec.unit_price * rec.quantity
