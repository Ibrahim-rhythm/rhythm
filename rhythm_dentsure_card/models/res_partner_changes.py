# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
grey = '\x1b[38;21m'
yellow = '\x1b[33;21m'
red = '\x1b[31;21m'
bold_red = '\x1b[31;1m'
reset = '\x1b[0m'
green = '\x1b[32m'
blue = '\x1b[34m'
# Ahmed Salama Code Start ---->


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    dentsure_diagnose_ids = fields.One2many('dentsure.diagnose',
                                            'patient_id',
                                            "Dentsure Diagnoses")
    dentsure_type = fields.Selection([("patient", "Patient"),
                                      ("doctor", "Doctor")], string="Densure Type")
    patient_member_no = fields.Char("Member No.")
    identification_id = fields.Char(string='Identification No')
    birthday = fields.Date("Birthdate")
    card_exp_date = fields.Date("Expiration Date")

# Ahmed Salama Code End.
