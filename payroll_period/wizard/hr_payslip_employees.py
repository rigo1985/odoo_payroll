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
from openerp import models, fields

from ..models.hr_fiscal_year import get_schedules


class HrPayslipEmployees(models.TransientModel):

    _inherit = 'hr.payslip.employees'

    company_id = fields.Many2one(
        'res.company',
        'Company',
        readonly=True
    )
    schedule_pay = fields.Selection(
        get_schedules,
        'Scheduled Pay',
        readonly=True
    )