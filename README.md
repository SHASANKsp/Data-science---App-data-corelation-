Data science project: Next growth lab

Part 1 - Using Regex to filter out patterns in the file

Using regex and json module for processing the data and to convert list to string respectively.
The text was saved as a dict. and orders and error were extracted.
Search module of regex was used to search for values after ":" and the last char were striped and the required numbers were printed.


Part 2 - Deploying the script build for filtering app reviews having negative reviews but positive comments

Streamlit and pandas were used in this problem. A title, header and description was added. The "st.file_uploader" function was used to get the uploaded fle. 
Once the file is stored in a variable it is procesed further. 
A subset was created containing Star, ID and Text, followed by filtering out entries with more than 3 stars. 
Setting up positive words for searching, followed by spliting each words of the text and finding the presecne of any of the positive words and printing of the IDs


Part 3 - Making co-relaation matrix between variable and ploting a heatmap

Importing pandas and numpy for solving the problem, followed by reading the csv file.
Changing all the datatype of values to categorical in order to find the correlation between them.
Correlation b/w Rank and Keyword, Rank and App ID, Rank and Short description, Rank and Long description.

Correlation b/w Rank and App ID: 0.5286928662558547
Correlation b/w Rank and Keyword: 0.10376306847431489
Correlation b/w Rank and Short description: -0.22266243001247427
Correlation b/w Rank and Long description: 0.3394301028172409

Correlation b/w Rank and App ID is found to be most relabable,
A correlation b/w every variable (Rank, Keyword, App ID, Short description and Long description) was found out and ploted as a heatmap 
with color scheme "coolwarm" ranging from -1 to 1. This was done to note any other correlation in the dataset.


![Screenshot 2022-07-03 195804](https://user-images.githubusercontent.com/58630523/177044279-30f51dd1-88c5-464f-a7df-a9f6f0114c92.png)



Part 4 - Using a pre trained model to check the grammer of te comments

Happy Transformer is a package avalable in Hugging Face’s transformer library. (https://happytransformer.com/)
It has various modules, one of which is 'Text to Text' that uses T5 grammar correction model
In addition to this pandas module was also used

Parameters used in TTSettings are:
Num_beams=5 - Number of steps for each search path
Min_length=1 - Minimum number of generated tokens
Max_length= 50 -  Maximum number of generated tokens
Early_stopping=True - When True, generation finishes if the EOS token is reached

It will only check the grammar of sentences whose length is greater that 4 words and check the grammer and make chenges.
At the end it will print the edited lines.
