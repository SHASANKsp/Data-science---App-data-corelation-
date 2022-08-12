import pandas as pd

df = pd.read_csv(r"C:\Users\priya\Downloads\review_data.csv") #importing file
df.head()

k = df.text.tolist() #converting text column to list
# k.head()

from happytransformer import HappyTextToText 
# Happy Transformer is a package avalable in Hugging Face’s transformer library. 
#It has various modules, one of which is 'Text to Text' that uses T5 grammar correction model

ha_tt = HappyTextToText("T5","vennify/t5-base-grammar-correction")

from happytransformer import TTSettings

args = TTSettings(num_beams=5, min_length=1, max_length= 50, early_stopping=True,)

for i in k:
    string = ("grammar: " + i)
    if len(string.split()) > 4:   #it will only check the grammar of sentences whose length is greater that 4 words.
        result = ha_tt.generate_text(string, args=args)
        print(result.text)
