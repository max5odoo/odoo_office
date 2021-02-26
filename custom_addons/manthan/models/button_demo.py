# -*- coding: utf-8 -*-
from openerp import models, fields, api

# Non-odoo library
import random
from random import randint
import string


class button_action_demo(models.Model):
    _name = 'button.demo'


    user_name = fields.Char(required=True, default='Click on generate name!')
    password = fields.Char()
    name= fields.Char('name of team')


    def generate_record_name(self):
        self.ensure_one()
        # Generates a random name between 9 and 15 characters long and writes it to the record.
        self.user_name= ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9, 15)))