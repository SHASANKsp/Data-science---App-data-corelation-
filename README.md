eval1
codes of first evaluation


Part 1 - Question 1
Using regex and json module for processing the data and to coonvert list to string respectively.
The text was saved as a dict. and orders and error were extracted.
search module of regex was used to search for values after : and the last char were striped and the required numbers were printed.


Part 1 - Quection 2
Streamlit and pandas were used in this problem.
A title, header and description was added. 
"st.file_uploader" function was used to get the uploaded fle. Once the file is stored in a variable it is procesed further.
A subset was created containing Star, ID and Text, followed by filtering out entries with more than 3 stars.
setting up positive words for searching.
followed by spliting each words of the text and finding the presecne of any of the positive words and printing of the IDs


Part 1 - Quection 3
importing pandas and numpy for solving the problem, followed by reading the csv file.
Changing all the datatype of values to categorical in order to find the correlation  between them.
Correlation b/w Rank and Keyword, Rank and App ID, Rank and Short description, Rank and Long description.
Correlation b/w Rank and App ID: 0.5286928662558547
Correlation b/w Rank and Keyword: 0.10376306847431489
Correlation b/w Rank and Short description: -0.22266243001247427
Correlation b/w Rank and Long description: 0.3394301028172409

Correlation b/w Rank and App ID is found to be most relabable,
A correlation b/w every variable (Rank, Keyword, App ID, Short description and Long description) was found out and ploted as a heatmap with color scheme "coolwarm" ranging from -1 to 1. This was done to note any other correlation in the dataset


![Screenshot 2022-07-03 195804](https://user-images.githubusercontent.com/58630523/177044279-30f51dd1-88c5-464f-a7df-a9f6f0114c92.png)



Part 2
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
