kontak = {"Joni": 628123321, "Nadin": 628987789}
print(kontak['Joni'])
kontak["Farrel"] = 628234432
kontak["Nadin"] = 628987789
print(kontak.keys())
print(kontak.values())
print(kontak.items())
del kontak["Nadin"]
print(kontak.items())
