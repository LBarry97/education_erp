from odoo import models, fields, api, _


class IhsanLangLevel(models.Model):
    _name = 'ihsan.lang.level'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', size=2)
    description = fields.Text('Description')

    _sql_constraints = [
        ('unique_lang_level',
         'unique(code)',
         'Language level code must be unique.'),
    ]