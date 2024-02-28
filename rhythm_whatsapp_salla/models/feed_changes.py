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


class WkFeedInherit(models.Model):
    _inherit = 'wk.feed'

    def get_partner_invoice_vals(self, partner_id, channel_id):
        """
        Add Salla partner flag to mark partners createdd from salla
        """
        vals = super().get_partner_invoice_vals(partner_id, channel_id)
        vals['salla_partner'] = True
        return vals

    @api.model
    def create_partner_invoice_id(self, partner_id, channel_id, invoice_partner_id=None):
        """
        Replace Core method to add send message code
        """
        partner_obj = self.env['res.partner']
        vals = self.get_partner_invoice_vals(partner_id, channel_id)
        match = None
        if invoice_partner_id:
            match = channel_id.match_partner_mappings(
                invoice_partner_id, 'invoice')
        if match:
            match.odoo_partner.write(vals)
            erp_id = match.odoo_partner
        else:
            erp_id = partner_obj.create(vals)
            # Add method to send whatsapp message
            erp_id.send_whatsapp_message()
            if (not self._context.get('no_mapping') and invoice_partner_id):
                channel_id.create_partner_mapping(erp_id, invoice_partner_id, 'invoice')
        return erp_id

# Ahmed Salama Code End.