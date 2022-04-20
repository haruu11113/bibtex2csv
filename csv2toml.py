# imrpot csv file
import pandas as pd
input_path = './bibsheet.csv'
output_path = './bibsheet.toml'

df = pd.read_csv(input_path, index_col=0)
cols = df.columns

# convert csv to toml
tomls = ''
for i in range(len(df)):
    toml = '[[paper]]\n'
    for c in cols:
        d = '' if str(df.loc[i, c]) == 'nan' else str(df.loc[i, c]) 
        toml = toml + "{0} = '{1}'\n".format(c, d)
    tomls = tomls + '\n' + toml


# export toml
f = open(output_path, 'w')
f.write(tomls)
f.close()