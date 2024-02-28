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

    salla_partner = fields.Boolean(string="Created By Salla?",
                                   help="This field will be checked, if this partner created from salla")
    sella_whatsapp = fields.Boolean(string="Whatsapp Sent",
                                    help="This field will be checked, if this partner received whatsapp message")
    def send_whatsapp_message(self):
        whatsapp_tmp = self.env['whatsapp.template']._find_default_for_model(self._name)
        print("whatsapp_tmp: ", whatsapp_tmp)
        composer_obj = self.env['whatsapp.composer']
        for rec in self:
            print("REC: ", rec, rec._name)
            composer_obj.with_context(
                active_model=rec._name, active_ids=rec.ids, default_phone=rec.mobile or rec.phone).create({
                'res_model': rec._name,
                'res_ids': rec.ids,
                'wa_template_id': whatsapp_tmp and whatsapp_tmp.id or False}).action_send_whatsapp_template()
            rec.sella_whatsapp = True
            # TODO: In case of test with action view
            # action = {
            #     'name': _("Send Confirm Salla Message"),
            #     'type': 'ir.actions.act_window',
            #     'res_model': 'whatsapp.composer',
            #     'view_mode': 'form',
            #     'view_id': self.env.ref('whatsapp.whatsapp_composer_view_form').id,
            #     'binding_model_id': self._name,
            #     'context': {'active_model': self._name, 'active_ids': active_ids},
            #     'target': 'new',
            # }
            # return action

    @api.model
    def send_salla_partner_whatsapp_message(self):
        logging.info(blue + "=== Start Cron to send whatsapp message ========" + reset)
        partner_ids = self.search([('salla_partner', '=', True), ('sella_whatsapp', '=', False)])
        logging.info(yellow + "Found Partners: %s" % len(partner_ids) + reset)
        partner_ids.send_whatsapp_message()
        logging.info(blue + "=== End Cron to send whatsapp message ========" + reset)

# Ahmed Salama Code End.
