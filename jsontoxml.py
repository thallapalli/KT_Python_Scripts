from json import loads
from dicttoxml import dicttoxml

s='{"main" : {"aaa" : "10", "bbb" : [1,2,3]}}'
xml = dicttoxml(loads(s))
print(xml)