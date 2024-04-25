# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'DentSure Portal',
    'category': 'Website/Website',
    'sequence': 2000,
    'summary': 'DentSure Clinic Portal',
    'website': 'https://www.odoo.com/app/website',
    'version': '1.0.0',
    'depends': [
        'base',
        'website',
        'digest',
        'web',
        'web_editor',
        'http_routing',
        'portal',
        'social_media',
        'auth_signup',
        'mail',
        'google_recaptcha',
        'utm',
        'rhythm_whatsapp_salla',
        'rhythm_dentsure_card',

    ],
    'installable': True,
    'data': [
        # security.xml first, data.xml need the group to exist (checking it)
        # 'security/ir.model.access.csv',
        'data/form.xml',
        'views/clinic_template.xml',
        'views/submit_form.xml',
    ],
    'demo': [],
    'application': True,
    # 'assets': {
    #     'web.assets_common':[
    #         '/dentsure_portal/static/src/js/add_line.js',
    #     ]
    # },
    'license': 'LGPL-3',
}
