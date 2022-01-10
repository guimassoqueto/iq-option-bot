#! /usr/bin/python3

from helping_functions import login_IQ_Option

iqoption = login_IQ_Option()
all_actives = iqoption.get_all_ACTIVES_OPCODE()
all_tradeable_actives = []

for key in all_actives.keys():
    all_tradeable_actives.append(key)

all_tradeable_actives.sort()