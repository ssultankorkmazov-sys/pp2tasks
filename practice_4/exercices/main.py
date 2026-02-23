import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':44} {'Description':13} {'Speed':10} {'MTU':6}")
print("-" * 42, " ", "-"*10, "  ", "-"*6, "  ", '-'*5)
for i in range(3):
    attributes = data['imdata'][i]['l1PhysIf']['attributes']
    print(f"{attributes['dn']:44} {attributes['descr']:13} {attributes['speed']:10} {attributes['mtu']:6}")
