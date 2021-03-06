# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Emanuel Cino <ecino@compassion.ch>
#
#    The licence is in the file __openerp__.py
#
##############################################################################

from openerp import models, fields


class product_template(models.Model):
    _inherit = 'product.template'

    gp_fund_id = fields.Integer('GP Fund id', size=4)


class product(models.Model):
    _inherit = 'product.product'

    gp_fund_id = fields.Integer('GP Fund id',
                                related='product_tmpl_id.gp_fund_id')
