from odoo import models, fields, api, _


class IhsanStudent(models.Model):
    _inherit = 'op.student'

    birthplace = fields.Many2one('res.country', 'Birthplace')
    phone = fields.Char('Phone', size=9)
    mobile_phone = fields.Char('Mobile Phone', size=9)
    old_student = fields.Boolean('Old Student')
    lang_level = fields.Many2one('ihsan.lang.level', 'Language level')
    school = fields.Many2one('ihsan.school', 'School')