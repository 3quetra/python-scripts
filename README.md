# Educational Projects in Python
**This repository contains small Python scripts which were performed with educational purpose.** 

## Brief projects' description (ordered by completion):

### 5. NLP: [text preprocessing scripts](nlp_preprocessing.py)

File contains text preprocessing scripts for nlp used for text cleaning, tokenisation and lemmatization.

----------------------

### 4. Matplotlib graph: ["Limes sale"](limes_sale.py)

Within this small project, I acted as a data analyst for an online lime retailer called "Sublime Limes". One of the product managers at Sublime Limes would like to gain insight into the customers and their sales habits. So using Matplotlib, I have created different line graphs to communicate this information. 

As we can see on the first graph, the clear peak of site visits occurred somewhere in June, but not all lime species have spikes in sales during this period. 
On the opposite, the most popular - Key Lime - had peak of sales in March, and in June it  had one of the most significant sales declines in that year. 
Sales of Blood Lime rose during  April - June, but not too drastically, and stopped in the end of June somewhere around `86` limes, then declined in July to a bit below `70` limes. 
Persian Lime sales increase matched the peak of site visits. The level of sales for this species increased to about `90` limes during April - July. Other spring and summer months weren't this good for Persian Lime though, it once again became a bit more popular in winter (sales increased up to `75` limes), nevertheless Blood Lime and Key Lime had higher sales rates  in winter too - `80` and `>100` respectively.

Resulting graphs:
![image](https://user-images.githubusercontent.com/27677180/152785472-27bbb01e-475e-4144-b9d7-db62f3ca678a.png)
      
----------------------

### 3.**"Filtering in SQL vs. Filtering in Python"**

In a file [script_for_backup.py](script_for_backup.py) there is a program that creates a new database called `backup.db` with the same structure as `original.db` (see previous item) and copies all the values greater than `20.0` from `original.db` to `backup.db`. 
Which approach is faster: filtering values in the query or reading everything into memory and filtering in Python wich is in [script_for_backup2.py](/script_for_backup2.py)? 

After launching 2 files one should be able to compare results. 
    
-----------------------    
    
### 2.**"Filling a Table vs. Printing Values"**

In a file [random.py](random.py) there is a program that creates a new database in a file `original.db` containing a single table called **"pressure"**, with a single field called **"reading"**. The program also inserts into the table `100,000` random numbers between `10.0` and `25.0`. 
Qestions: 
- How long does it take this program to run? 
- How long does it take to run a program that simply writes those random numbers to a file? (The result described in the 2nd variant can be seen if one runs file named [random2.py](random2.py).)

After launching 2 files one should be able to compare results. 

----------------------- 

### 1. Lists, Functions, and Dictionaries: ["Hurricanes"](hurricanes.py)
    
The goal of this project is to find extremes among data points of magor hurricanes via arranging data in dictionaries and lists for calculations convenience and performing sorting.
  
  


    
    


