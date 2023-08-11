from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class rule(models.Model):

     _inherit='hr.job'
     _description='hr_job inherit'
     rule_money=fields.Float(string="Số tiền đóng quỹ")