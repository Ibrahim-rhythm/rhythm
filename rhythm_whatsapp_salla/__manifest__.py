# -*- coding: utf-8 -*-
{
    'name': "Rhythm Whatsapp Salla",

    'summary': "This module is used to send whatsapp message once partner are recived from salla",

    'description': """
This module is used to send whatsapp message once partner are recived from salla
    """,

    'author': "Rhythm/Ahmed Salama",
    'website': "https://www.rhythm.sa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'odoo_multi_channel_sale', 'whatsapp'],

    # always loaded
    'data': [
        'data/cron.xml',

        'views/res_partner_view_changes.xml',
    ],

}

