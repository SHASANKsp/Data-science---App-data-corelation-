#PART 1
#question 2

import streamlit as st #importing streamlit module 
import pandas as pd #importing pandas module

#setting up the title
st.title('Jr Data scientist - evaluation 1')
#setting up the header
st.header('Filtering Playstore reviews')
# description of the app
st.write('When given review data of an app from playstore in proper format it filters reviews with positive comments but low rating')

#taking .csv file as input
uf = st.file_uploader("Upload the file", type= ['csv'])

#checking if upload is successful
if uf is not None:
    fd = {"FileName": uf.name, "FileType": uf.type, "FileSize": uf.size }
    st.write(fd) #printing the details of the file
    file = pd.read_csv(uf)
    nfile = file[["Star","ID","Text"]] #creating a subset with star, id and text

    lowi= nfile.loc[nfile['Star'] <= 3]  #filering out all the entries with rating lower then 4 
    
    #Set of positive words used
    positive = ['Good','good','Nice', 'Very nice','helpful','Excellent','Awesome','Super','Perfect','Outstanding']
    #resetiing the index
    lowi = lowi.reset_index()

    k=0
    st.text("ID of the reviews")
    for line in lowi['Text']:
        word = line.split(' ') #spliting up the sentence 
        for j in word:
            if j in positive:
                #print(lowi.loc[k])
                st.text(lowi.loc[k]["ID"])
        k+=1
