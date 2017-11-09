# -*- coding: utf-8 -*-
# Copyright 2017 Gabriele Baldessari, Abstract-technology
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResUsers(models.Model):

    _inherit = 'res.users'

    sale_team_ids = fields.Many2many(
        string="Sale teams",
        help="Sale teams of which the user is part of.",
        comodel_name="crm.team",
        relation="users_teams_rel",
        column1="user_id",
        column2="team_id"
    )
