# -*- coding: utf-8 -*-
from openerp import fields, models


class FleetVehicle(models.Model):

    _inherit = 'fleet.vehicle'

    def _get_odometer(self,  ids, odometer_id, arg, context):
        res = super(FleetVehicle, self)._get_odometer( ids, odometer_id, arg, context)
        return res

    def _set_odometer(self,  id, name, value, args=None, context=None):
        res = super(FleetVehicle, self)._set_odometer( id, name, value, args, context)
        return res


    odometer = fields.Float(compute="_get_odometer", fnct_inv=_set_odometer, string='Last Odometer'
                                    help='Odometer measure of the vehicle at the moment of this log',
                                    track_visibility='onchange'),

