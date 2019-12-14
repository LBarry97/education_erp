from odoo import models, fields, api, _


class IhsanLangLevel(models.Model):
    _name = 'ihsan.school'

    name = fields.Char('School', required=True)

    _sql_constraints = [
        ('unique_school',
         'unique(name)',
         'School name must be unique.'),
    ]