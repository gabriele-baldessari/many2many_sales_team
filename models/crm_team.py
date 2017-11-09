# -*- coding: utf-8 -*-
# Copyright 2017 Gabriele Baldessari, Abstract-technology
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmTeam(models.Model):

    _inherit = 'crm.team'

    member_ids = fields.Many2many(
        string="Team Members",
        help="Users that are part of the sales team",
        comodel_name="res.users",
        relation="users_teams_rel",
        column1="team_id",
        column2="user_id",
    )
