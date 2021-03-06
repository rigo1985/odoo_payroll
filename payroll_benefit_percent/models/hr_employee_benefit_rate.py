# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, models, _


class HrEmployeeBenefitRate(models.Model):
    _inherit = 'hr.employee.benefit.rate'

    @api.model
    def get_all_amount_types(self):
        res = super(HrEmployeeBenefitRate, self).get_all_amount_types()

        res.append(('percent_gross', _('Percent of Gross Salary')))

        return res

    @api.model
    def _get_line_base_ratio(self, line, payslip):
        if line.amount_type == 'percent_gross':
            return payslip.gross_salary / 100

        return super(HrEmployeeBenefitRate, self)._get_line_base_ratio(
            line, payslip)
