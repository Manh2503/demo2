from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import datetime


class Revenue(models.Model):
    _name = "revenue2"
    _description = "Revenue 2 model"

    revenue_date = fields.Date(string='Ngày đóng quỹ', required=True)
    # revenue_money = fields.Float('revenue_money', required = True)
    revenue_money = fields.Float(string="Số tiền đóng",compute='_money', store=True)
    # staff_name = fields.Char('_compute_name')
    employee_id = fields.Many2one('hr.employee')
    job_choice = fields.Integer(string="mã nhân viên")

    @api.depends('employee_id')
    def _money(self):
        for rec in self:
            rec.job_choice = rec.employee_id.job_id
            rec.revenue_money = self.env['hr.job'].search([('id','=',rec.job_choice)]).rule_money


