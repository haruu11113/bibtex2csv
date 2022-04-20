import re
import pandas as pd
input_path = './test.bib'
output_path = './bibsheet.csv'

# split 1 article
entory = ''
entories = []
with open(input_path) as f:
    for line in f:
        if re.match(r"@[a-zA-Z0-9_]", line):
            entories.append(entory)
            entory = ''
        else:
            entory = str(entory) + line

# convert bibtex to rows
result = {}
for i, entory in enumerate(entories):
    if entory is None:
        continue

    e_li = entory.split('},\n')
    e_dic = {}
    for e in e_li:
        tmp_e = e.replace('}', '').replace('{', '').replace('\n', '').split(' = ')
        if len(tmp_e) < 2:
            continue
        e_dic[tmp_e[0]] = tmp_e[1]
    result[i] = e_dic

# exportting csv
df = pd.DataFrame(result).T
col = {c:c.replace('None', '') for c in df.columns}
df = df.rename(columns=col)
df.to_csv(output_path)
print('exported to: {0}'.format(output_path))
