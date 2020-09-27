import csv
from jinja2 import Template, StrictUndefined

with open('./kea-dhcp4.conf') as g:
    template = Template(g.read(), undefined=StrictUndefined)

with open('info.csv') as f:
    data = csv.DictReader(f, delimiter=',', skipinitialspace=True)
    data = list(data)

with open('output.txt', 'w') as h:
    h.write(template.render(hosts=data))
    
print(template.render(hosts=data))
