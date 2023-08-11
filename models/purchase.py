from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Expense(models.Model):
    _name = "purchase"
    _description = "purchase model"

    purchase_date = fields.Date(string='Thời gian mua', default=fields.Datetime.now())
    total_money = fields.Float(string='Tổng số tiền', compute='_total_money',store=True)
    employee_id = fields.Many2one('hr.employee')
    product_ids = fields.One2many('detail.purchase','purchase_id',string="Các sản phẩm đã mua")

    @api.depends('product_ids')
    def _total_money(self):
        for rec in self:
            rec.total_money = 0
            for id in rec.product_ids:
                rec.total_money += id.product_money



