from odoo import http
from odoo.http import request

class ReportAndDelivery(http.Controller):
    @http.route('/shop/report_and_delivery', type='http', auth="public", website=True, sitemap=False)
    def report_and_delivery(self):
        context = {}

        order = request.website.sale_get_order()
        report = request.env['product.template'].search([('type', '=', 'report')], order="sequence")
        delivery = request.env['product.template'].search([('type', '=', 'delivery')], order="sequence")

        context.update({
            'order': order,
            'report': report,
            'delivery': delivery
        })

        return request.render('report_and_delivery.report_and_delivery', context)