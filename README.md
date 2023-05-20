# Web analytics on Quora website
**Business question:** How Quora makes money by displaying advertisements on its content pages. 

**How this model helps Quora:**
1.	By helping them figure out which questions/topics generate more revenue. As a result, Quora will be able to position ads on topics that drive more page visits, which in turn may help increase their income.
2.	By exploring what different factors influence the earnings and how much each factor contributes to earnings on the page.

**Why do people use Quora?**
•	People use Quora for a variety of reasons, to get answers to their questions, including information searching, personal and professional growth, networking, sharing knowledge, and amusement and enjoyment. Quora offers a platform for users to learn, discuss, interact, and engage with a varied community of people interested in various topics and themes. 
•	To make money by answering people’s questions if the topic is their area of expertise.

Dataset was downloaded from Kaggle [1]:
https://www.kaggle.com/datasets/alexgibso/5000-quora-questions-with-earnings

This dataset contains nearly 2557 questions and 8 columns as shown in Figure 1.
![image](https://github.com/susmithashetty94/Web-analytics/assets/134163863/3736e9e5-665d-4c0a-b160-8673b64e7ac7)

Around 58% of records did not have any earnings associated with them.

**Data Cleaning**
1.	Checked data for missing values and duplicates. There were no missing values. But had 33 duplicates that were removed from the dataset.
2.	Changed a few Ad Impressions values to 0 since they were non-numerical.
3.	Changed earnings variable to a binary/categorical variable to address one of our business problems.
4.	Removed the ‘$’ sign from the Earnings column to convert it to a numerical value for analysis.

**Research Questions**

Analysis focused on answering the following questions:
1.	What kind of topics/categories are generating more revenue/earnings, views, ad impressions, and followers on Quora?
2.	How do requests, answers, views, followers, and ad impressions variables affect the earnings on Quora?
3.	There were many questions that did not generate revenue. What can we infer from them? (Here we would like to analyze and draw some commonalities among them.)

**Business Question:**
1.	What kind of topics/categories are generating more earnings, views, ad impressions, and followers on Quora?
1.	To address any of the research questions the dataset was inadequate. 
2.	No tags related to topics exist on the Quora website or in the dataset.
3.  Came up with 2 approaches - 
a)	Manually find the popular topics for the questions in the dataset by the trial-and-error method.
b)	Developed code using Python to scrape the dataset for keywords from the questions column (popular topics).


![image](https://github.com/susmithashetty94/Web-analytics/assets/134163863/49a20f77-41dc-429b-857a-86ee74cbb57c)
Keywords: Sample keywords for each category. The python program will look for these keywords from the python dictionary (Figure 2) and accordingly increase the count for respective categories. Followed the same approach for the variables (earnings, followers, views, ad impressions, requests, answers)
![image](https://github.com/susmithashetty94/Web-analytics/assets/134163863/9a525d3e-f004-4a7a-bd2f-c70c86d66cbe)



