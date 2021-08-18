# -*- coding: utf-8 -*-

from odoo import models


class ResPartnerInheritEmail(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('email_uniq', 'unique (email)','Email already used.')
    ]

    