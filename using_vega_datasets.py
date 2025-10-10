# print('Hello world' * 2)

from vega_datasets import data    # Здесь без импорта обошлось. А в jupyter нет!
dss = data.list_datasets()
print(dss) #[:3])
print(type(data._datasets))
# for i in dss[:3]:
#     print()
# print(data._datasets[dss[0]].description)
df = data.barley
print(df.description)