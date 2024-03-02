# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
igrey = '\x1b[38;21m'
yellow = '\x1b[33;21m'
red = '\x1b[31;21m'
bold_red = '\x1b[31;1m'
reset = '\x1b[0m'
green = '\x1b[32m'
blue = '\x1b[34m'
# Ahmed Salama Code Start ---->


class DentsureDiagnose(models.Model):
    _name = 'dentsure.diagnose'
    _description = "Densure Diagnose"

    name = fields.Char("No.", copy=False, readonly=True, default=lambda x: _('New'))
    patient_id = fields.Many2one('res.partner', "Patient", required=True,
                                 domain=[('dentsure_type', '=', 'patient')])
    doctor_id = fields.Many2one('res.partner', "Doctor", required=True,
                                domain=[('dentsure_type', '=', 'doctor')])
    diagnoses_date = fields.Date("Diagnose Date", required=True, default=fields.Date.today())
    dental_diagnose_ids = fields.One2many('dental.diagnose', 'diagnose_id',
                                          'Dental Doiagnose')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('rhythm_dentsure_card.dental_diagnose_code') or _('New')
        return super().create(vals_list)


class DentistDiagnose(models.Model):
    _name = 'dental.diagnose'
    _description = "Patient Dental Diagnose"
    _rec_name = 'complete_name'

    diagnose_id = fields.Many2one('dentsure.diagnose', "Diagnose")
    mouth_sector = fields.Selection([('upper_right', 'Upper Right'), ('upper_left', 'Upper Left'),
                                     ('lower_right', 'Lower Right'), ('lower_left', 'Lower Left')],
                                    required=True, string="Quadrant")
    tooth_number = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                     ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')],
                                    required=True, string="Tooth Num.")
    diagnose = fields.Text("Diagnose")
    complete_name = fields.Char("Name", compute='_get_complete_name')

    @api.onchange('mouth_sector', 'diagnose_id', 'tooth_number')
    def _get_complete_name(self):
        for rec in self:
            complete_name = ""
            if rec.partner_id:
                complete_name += "[%s] %s/%s" % (rec.diagnose_id.name, rec.mouth_sector, rec.tooth_number)
            rec.complete_name = complete_name

# Ahmed Salama Code End.