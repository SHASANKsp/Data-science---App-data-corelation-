# eval1
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
Correlation b/w Rank and Keyword, Rank and App ID, Rank and Short description, Rank and Long description -------pending
A correlation b/w every variable (Rank, Keyword, App ID, Short description and Long description) was found out and ploted as a heatmap with color scheme "coolwarm" ranging from -1 to 1.
