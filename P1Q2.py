#PART 1
#question 2

import streamlit as st
import pandas as pd

uf = st.file_uploader("Upload the file", type= ['csv'])

if uf is not None:
    fd = {"FileName": uf.name, "FileType": uf.type, "FileSize": uf.size }
    st.write(fd)
    st.write("to next step")
    file = pd.read_csv(uf)
    print(file)
    nfile = file[["Star","ID","Text"]]
    ffile = nfile.loc[nfile["Star"] < 4]
    print("ffile")

    lowi= ffile.loc[ffile['Star'] <= 3]
    positive = ['Good','good','Nice', 'Very nice','helpful','Excellent','Awesome','Super','Perfect','Outstanding']

    lowi = lowi.reset_index()
    print(lowi)

    k=0
    for line in lowi['Text']:
        word = line.split(' ')
        for j in word:
            if j in positive:
                #print(lowi.loc[k])
                st.text(lowi.loc[k]["ID"])
        k+=1

