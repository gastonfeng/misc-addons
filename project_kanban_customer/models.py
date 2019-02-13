# -*- coding: utf-8 -*-
from openerp import fields
from openerp import models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    partner_country_image = fields.Binary('Partner\'s country flag', related='partner_id.country_id.image')
    partner_country_name = fields.Char('Partner\'s country name', related='partner_id.country_id.name')

    def name_get(self, ids):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(ids, ['partner_id', 'name'])
        res = []
        for record in reads:
            name = record['name'] or ''
            partner = record['partner_id'] or ''
            if partner:
                name = '%s (%s)' % (name, partner[1])
            res.append((record['id'], name))
        return res

    def name_search(self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            ids = self.search(['|', ('partner_id', operator, name), ('name', operator, name)] + args, limit=limit)
        else:
            ids = self.search(args, limit=limit)
        return self.name_get(ids)
