import json
with open("parameters.json.old") as f:
    data = json.loads(f.read())

keyz = [x for x in data.keys() if 'junction' in x]
result = {}
for k in keyz:
    val = 0
    if 'lenght' in k:
        val = 100
    result[len(k)+val] = result.get(len(k)+val,[]) + [k]

result = [v for _, v in result.items()]

for rr in result:
    value = data[rr[0]]
    print (f"{rr[0]} -> {value}")
    for i in rr[1:]:
        value = data[i]
        print (f"   {value}")
    
    if 'dist' in rr[0]:
        for i in rr:
            data[i] = 0.03

    if 'height' in rr[0]:
        for i in rr:
            data[i] = 0.07

    if 'lenght' in rr[0]:
        for i in rr:
            data[i] = 0.05

with open("parameters.json","w") as f:
    f.write(json.dumps(data,indent=4,sort_keys=True))


            