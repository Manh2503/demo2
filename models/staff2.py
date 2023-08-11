from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import datetime


class Staff2(models.Model):
    _inherit = "hr.employee"
    _description = "inherit hr_employee model"
    state = fields.Boolean(string="Trạng thái đóng quỹ",default=False,compute="get_state")

    def get_staff_no_revenue(self):
        ngay_hom_nay = datetime.date.today()
        ngay_dau_thang = ngay_hom_nay.replace(day=1)
        han_dong = ngay_hom_nay.replace(day=12)
        nhan_vien_all = self.search([])
        nhan_vien_da_dong = self.env['revenue2'].search(
            [('revenue_date', '>=', ngay_dau_thang), ('revenue_date', '<=', han_dong)])
        nhan_vien_chua_dong = nhan_vien_all - nhan_vien_da_dong.mapped('employee_id')
        danh_sach_nhan_vien_chua_dong = []
        for rec in nhan_vien_chua_dong:
            danh_sach_nhan_vien_chua_dong.append(rec.id)
        return danh_sach_nhan_vien_chua_dong

    def get_state(self):
        nhan_vien = self.search([])
        for rec in nhan_vien:
            if rec.id in self.get_staff_no_revenue():
                rec.state = False
            else:
                rec.state = True

    def send_mail_from_auto(self):
        template = self.env.ref('demo_2.send_mail_template_2')
        nhan_vien = self.search([])
        for rec in nhan_vien:
            if rec.state == False:
                print(rec.id)
                template.send_mail(rec.id)
