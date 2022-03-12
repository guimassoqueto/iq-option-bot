#! /usr/bin/python3

from helpers.helping_functions import all_tradeable_actives

print([active for active in all_tradeable_actives() if active.endswith('OTC')])