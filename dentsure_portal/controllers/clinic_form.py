from odoo import http
from odoo.http import request


class Clinic(http.Controller):
    @http.route(['/dentsure/clinic'], type='http', website=True, auth='public')
    def clinic_report(self, **post):
        # print("********************************here")
        tooth = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        mouth = ['Upper Right', 'Upper Left', 'Lower Right', 'Lower Left']
        key_1 = ['upper_right', 'upper_left', 'lower_right', 'lower_left']
        diagnose_id = []
        key_2 = ['']
        return http.request.render('dentsure_portal.clinic_template',
                                   {'mouth': mouth, 'key_1': key_1, 'tooth': tooth, 'key': key,
                                    'diagnose_id': diagnose_id, 'key_2': key_2})

    @http.route(['/get_diagnose/submit'], type='http', auth="public", website=True)
    def get_diagnose(self, **post):
        diagnose_vals = []
        dental_line_vals = []
        dental_line_vals = request.env['dental.line'].sudo().create({
            'mouth_sector': post.get('mouth_sector'),
            'tooth_number': post.get('tooth_number'),
            'notes': post.get('notes'),
        })
        print(dental_line_vals)
        diagnose = request.env['dentsure.diagnose'].sudo().create({
            'patient_id': post.get('patient_id'),
            'mobile_number': post.get('mobile_number'),
            'doctor_id': post.get('doctor_id'),
            'dental_line_ids': dental_line_vals,
        })

        vals = {'diagnose': diagnose, 'dental_line_ids': dental_line_vals.id}
        print(vals)
        return request.render("dentsure_portal.tmp_form_success", vals)
        # if 'radio7' in post:
        #     diagnose_vals.append((0, 0, {
        #         'diagnose_id': post.get('selection7'),
        #         'notes': post.get('description7'),
        #     }))

        # if 'radio1' in post:
        #     dental_line_vals.append((0, 0, {
        #         'mouth': post.get('mouth_sector'),
        #         'tooth': post.get('tooth_number'),
        #         'notes': post.get('notes'),
        #     }))
