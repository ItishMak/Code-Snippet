import sys
import pandas as pd
system = sys.argv[1:]
flag=0
for i in range(len(system)):
    file = system[i]
    for chunk in pd.read_csv(file,chunksize=10):
        chunk["filename"]  = file.split('/')[-1]
        # chunk = chunk.style.hide_index()        
        if(flag==0):
            print(chunk.to_csv(index=False,header=True,line_terminator='\n'),end = '')
            flag=1
        else:
            print(chunk.to_csv(index=False,header=False,line_terminator='\n'),end = '')



