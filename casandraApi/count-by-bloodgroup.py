#!/usr/bin/env python
'''Count records by blood group'''
from cassandra.auth import PlainTextAuthProvider
from prettytable import PrettyTable
from cassandra.cluster import Cluster
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
import config as cfg

def PrintTable(rows, keys):
    t = PrettyTable(['ID', 'Name', 'Sex', 'Blood Group', 'SSN'])
    for r in rows:
        t.add_row([r.id, r.name, r.sex, r.blood_group, r.ssn])
    print(t)


keys = ['id', 'address', 'blood_group', 'company', 'job', 'mail', 'name', 'residence', 'sex', 'ssn', 'username']

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port=cfg.config['port'], auth_provider=auth_provider, ssl_context=ssl_context)
session = cluster.connect()

records = {}
blood_groups = ['A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

print("Counting records by blood group ...")

for group in blood_groups:
    count = session.execute("SELECT COUNT(*) FROM candidates.blood_group WHERE blood_group = '{}'".format(group)).one()
    records[group] = count.system_count

t = PrettyTable(records.keys())
t.add_row(records.values())
print(t)
