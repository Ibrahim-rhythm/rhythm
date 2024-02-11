# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################
from odoo import models, fields, api
from odoo.exceptions import UserError

from urllib.parse import urljoin
from logging import getLogger
_logger = getLogger(__name__)


class MultiChannelWebhook(models.Model):
    _inherit = "multi.channel.sale"

    # Webhooks Available/Not Available

    # New Order Webhook
    is_create_order_webhook = fields.Boolean(string="Activate Webhook")
    order_webhook_url = fields.Char(string="New Created Order Webhook-Url", compute="_order_webhook_url")
    order_webhook_id = fields.Char(help="Store the New Created Order Webhook ID of the Ecomm end if supported!")

    # Order Update webhook
    is_update_order_webhook = fields.Boolean(string="Activate Update Webhook")
    order_update_webhook_url = fields.Char(string="Update Order Webhook-Url", compute="_order_update_webhook_url")
    order_update_webhook_id = fields.Char(help="Store the Update order Webhook ID if Supported!")

    # Activate Developer Mode
    def channel_activate_developer_mode(self):
        """Activate the Developer mode
        """
        url = self.redirect_to_channel(self.id)
        append_url = '/web?debug=0'
        if self._context.get('debug_activate'):
            append_url = '/web?debug=1'
        url = url.replace('/web', append_url)
        return {
                'type': 'ir.actions.act_url',
                'target': 'self',
                'url': url
            }

    def redirect_to_channel(self, instance_id=False):
        """Method to get the channel's form view URL
        """
        action_id = self.env.ref('odoo_multi_channel_sale.action_multi_channel_view').id
        url = "/web#action={}&model=multi.channel.sale".format(action_id)
        if instance_id:
            url = "/web#id={}&action={}&model=multi.channel.sale&view_type=form".format(instance_id, action_id)
        return url

    channel_configs = fields.Char(compute="_channel_available_configs")

    def available_configs(self):
        return [
                # Webhooks Add from extension when implemented
                # 'webhook_available', 
                # 'create_order_webhook',
                # 'update_order_webhook',

                # Import Crons
                'cron_available',
                'import_order_cron',
                'order_created_after',
                'order_updated_after',
                'import_product_cron',
                'product_created_after',
                'product_updated_after',
                'import_partner_cron',
                'partner_created_after',
                'partner_updated_after',
                'import_category_cron',

                # realtime export
                'sync_order_invoice',
                'sync_order_shipment',
                'sync_order_cancel',
            ]

    def _channel_available_configs(self):
        """Get all the available features per channel"""
        all_configs = self.available_configs()
        method = f'{self.channel}_available_configs'
        if hasattr(self, method):
            channel_configs = getattr(self, method, False)
            if channel_configs:
                all_configs = channel_configs()
        channel_configs = ','.join(set(all_configs))
        self.write({'channel_configs': channel_configs})

    def _order_webhook_url(self):
        """
            Computed Webhook URL for Created Order
        """
        url = urljoin(self.get_base_url(), f'multichannel/create/order/webhook/{self.id}')
        self.order_webhook_url = url

    def _order_update_webhook_url(self):
        """
            Computed Webhook URL for Updated Order
        """
        url = urljoin(self.get_base_url(), f'multichannel/update/order/webhook/{self.id}')
        self.order_update_webhook_url = url

    @api.constrains('is_create_order_webhook')
    def change_order_webhook(self):
        """
            Create following method in extension only if it's webhook enables
            using API Call.
            Eg. method=>: activate_salla_order_webhook, deactivate_salla_order_webhook
            or
            When no need to add url manually to ecomm end. Otherwise extension will
            provide the required information regarding how to enable webhook.
        """
        if self.state == 'validate':
            method, webhook_type = False, 'Active/Inactive'
            webhook_url = self.order_webhook_url
            message = f'Error in {webhook_type} Order Webhook: '
            if self.is_create_order_webhook and hasattr(self, f'activate_{self.channel}_order_webhook'):
                webhook_type = 'Activating'
                method = getattr(self, f'activate_{self.channel}_order_webhook', False)
            elif not self.is_create_order_webhook and hasattr(self, f'deactivate_{self.channel}_order_webhook'):
                webhook_type = 'Deactivating'
                method = getattr(self, f'deactivate_{self.channel}_order_webhook', False)
            if method:
                try:
                    method(webhook_url, 'create')
                except Exception as e:
                    message += str(e)
                    if self.is_create_order_webhook:
                        raise UserError(message)
                    _logger.error(message)


    @api.constrains('is_update_order_webhook')
    def change_update_order_webhook(self):
        """
            Create following method in extension only if
            it's webhook enables/disable using API Calls.
            Eg. method=>: activate_salla_order_webhook, deactivate_salla_order_webhook
            or
            When no need to add url manually to ecomm end. Otherwise extension will
            provide the required information regarding how to enable webhook.
        """
        if self.state == 'validate':
            method, webhook_type = False, 'Active/Inactive'
            webhook_url = self.order_update_webhook_url
            message = f'Error in {webhook_type} Update Order Webhook: '
            if self.is_update_order_webhook and hasattr(self, f'activate_{self.channel}_order_webhook'):
                method = getattr(self, f'activate_{self.channel}_order_webhook', False)
            elif not self.is_update_order_webhook and hasattr(self, f'deactivate_{self.channel}_order_webhook'):
                method = getattr(self, f'deactivate_{self.channel}_order_webhook', False)
            if method:
                try:
                    method(webhook_url, 'update')
                except Exception as e:
                    message += str(e)
                    if self.is_update_order_webhook:
                        raise UserError(message)
                    _logger.error(message)