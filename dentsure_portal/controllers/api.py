import json
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class DentsureAPI(http.Controller):

    @http.route('/dentsure/clinic',
                type='http', auth='public', website=True, csrf=False,  methods=['GET', 'POST'])
    def dentsure_report(self, **kw):
        print("\n\n\n::: DATA FORM 1 :::")
        print(kw)
        DntsureObject = request.env['dentsure.diagnose']
        values = self.prepare_data(**kw)
        record = DntsureObject.sudo().create(values)
        if record.id:
            result = {'message': '', 'status': True, 'record_id': record.id}
        else:
            result = {'message': 'Faild', 'status': False}
        return json.dumps(result)

    def prepare_data(self, **kw):
        # data = {}
        # data[] =
        return {
            'patient_id': kw.get('patient_id'),
            'doctor_id': kw.get('doctor_id'),

        }

