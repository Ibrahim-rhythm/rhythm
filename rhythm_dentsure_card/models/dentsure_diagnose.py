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

    name = fields.Char("No.", copy=False, readonly=True, default=_('New'))
    patient_id = fields.Many2one('res.partner', "Patient", required=True,
                                 domain=[('dentsure_type', '=', 'patient')])
    doctor_id = fields.Many2one('res.partner', "Doctor", required=True,
                                domain=[('dentsure_type', '=', 'doctor')])
    diagnoses_date = fields.Date("Diagnose Date", required=True, default=fields.Date.today())
    dental_line_ids = fields.One2many('dental.line', 'parent_id',
                                 'Dental Doiagnos')
    diagnose_line_ids = fields.One2many('diagnose.line', 'parent_id',
                                   'Doiagnoses')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('dental_diagnose_code')
        return super().create(vals)


class DentistLine(models.Model):
    _name = 'dental.line'
    _description = "Patient Dental Line"
    _rec_name = 'complete_name'

    parent_id = fields.Many2one('dentsure.diagnose', "Diagnose")
    mouth_sector = fields.Selection([('upper_right', 'Upper Right'), ('upper_left', 'Upper Left'),
                                     ('lower_right', 'Lower Right'), ('lower_left', 'Lower Left')],
                                    required=True, string="Quadrant")
    tooth_number = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                     ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')],
                                    required=True, string="Tooth Num.")
    notes = fields.Text("Diagnose")
    complete_name = fields.Char("Name", compute='_get_complete_name')

    @api.onchange('mouth_sector', 'parent_id', 'tooth_number')
    def _get_complete_name(self):
        for rec in self:
            complete_name = ""
            if rec.parent_id:
                complete_name += "[%s] %s/%s" % (rec.parent_id.name, rec.mouth_sector, rec.tooth_number)
            rec.complete_name = complete_name

# TODO: to be deleted
class DentalDiagnose(models.Model):
    _name = 'dental.diagnose'


class DiagnoseLine(models.Model):
    _name = 'diagnose.line'
    _description = "Patient Diagnose Lines"

    parent_id = fields.Many2one('dentsure.diagnose', "Detsure Diagnose")
    diagnose_id = fields.Many2one('diagnose.diagnose', "Diagnose", required=True)
    notes = fields.Text("Notes")


class Diagnose(models.Model):
    _name = 'diagnose.diagnose'
    _description = "Patient Diagnoses"

    name = fields.Char("Diagnose", required=True)
    notes = fields.Text("Notes")


# Ahmed Salama Code End.
