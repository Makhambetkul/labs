import json

with open("sample.json", "r") as myfile:
    str_data = myfile.read()

data = json.loads(str_data)

print('Interface Status')
print('='*80)
print('{:<50} {:<20} {:<8} {:<6}'.format("DN", "Description", "Speed", "MTU"))
print('-'*50, '-'*20, '-'*8, '-'*6)

imdata = data.get('imdata', [])

for i in imdata:
    l1PhysIf = i.get('l1PhysIf', {})
    attributes = l1PhysIf.get('attributes', {})

    dn = attributes.get('dn', "")
    descr = attributes.get('descr', "")
    speed = attributes.get('speed', "")
    mtu = attributes.get('mtu', "")
    print('{:<50} {:<20} {:<8} {:<6}'.format(dn, descr, speed, mtu))