# Visualizing Data

## Preview
In the final assignment are presented visualized data, taken from NESARC codebook, in order to examine the correlation between cannabis use and mental disorders such as major depression and general anxiety diagnosed in the last 12 months in a sample of  9535 U.S. young adults, aged from 18 to 30 years old. I used Spyder IDE to create both univariate and bivariate bar charts for the selected variables. More specifically, with variable ‘AGE’ between 18 and 30, I built unvariate graphs for categorical variables **‘S3BQ1A5’** which represents cannabis use, **‘S3BD5Q2E’**  which is frequency of this use, **‘MAJORDEP12’** that stands for major depression diagnosis in the last 12 months and **‘GENAXDX12’** that indicates general anxiety diagnosis in the same period. In addition, you will find another univariate graph for the quantitative variable  **‘NUMJOPMOTH_EST’**, which I created in my previous assignment by multiplying frequency of cannabis use and average quantity of joints smoked, in order to estimate the total number of joints smoked per month by the individuals. As far as the bivariate graphs are concerned, I chose to examine visualized the association between cannabis use (C->C) and both mentioned disorders and additionally the relationship between frequency (C->C) and quantity (Q->C) of this use with both depression and anxiety. Thus, bar charts were created combining variables  **‘S3BQ1A5’** (cannabis use), ‘S3BD5Q2E’ (frequency of use) and **‘NUMJOPMOTH_EST’** (quantity of joints) with variables **‘MAJORDEP12’** (major depression) and  **‘GENAXDX12’** (general anxiety). Concluding, for the quantitative variable both center and spread were measured and describe function was used in order to examine useful information, about the selected categorical variables.

## Output

### Univariate graphs:
![out1](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out1.png)

A random sample of 9535 U.S. young adults, aged 18-30, were asked, as a part of NESARC survey, the following question: “Have you ever used cannabis?” A percentage of 25.29% (or 7042 individuals) answered “Yes”, whereas 73.85% (or about 2500 individuals) answered “No” which was the most frequent answer. Also a significantly small percentage of 0.84%, fell into category 9 (“Unknown“) which is our missing data.

![out2](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out2.png)

To the question of “How often did you use cannabis when using the most?”, the top answer was “Every day”, since 534 individuals fell into this category, followed by “Once a year” category with approximately 400 individuals. Less than 100 people chose “7-11 times per year” category, which was the least frequent answer.

![out3](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out3.png)

Of the total number of participants (18-30) who answered “Yes” to the question of cannabis use, only those who were smoking marijuana in last 12 months and prior were taken into consideration for the next two questions. 

To the question of “Have you been diagnosed with non-hierarchical major depression in the last 12 months?”, about 660 participants or 79.04% answered “No” which was the most frequent answer, whereas 175 or 20.95% fell into “Yes”.

For the question, ”Have you been diagnosed with non-hierarchical generalized anxiety in the last 12 months?”, 802 individuals or 96.04% answered “No“ that was our top answer, while only 33 or 3.95% chose “Yes“.

![out4](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out4.png)

For the estimated number of joints smoked per month by cannabis users, ages 18-30, it noticeable from the graph that there was a skewed-right distribution. The spread or the standard deviation of the variable is extremely large which indicates a large variety of answers among the participants. The three main numerical measures of the center of the distribution are the mode, the median, and the mean. Here we can see that mode is equal to 0.1 and it was the most common occurring value in the distribution, which means that most of participants smoked less than 1 joint per month. The mean is equal to 70.1 which indicates that cannabis users smoked about 70 joints per month on average and the median or the middle value is 6.

![out5](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out5.png)

Estimated number of joints smoked per month binned to groups as illustrated above. Another way of visualizing the distribution of variable **‘NUMJOPMOTH_EST’**. We can see that most individuals, about 990, smoked less than one joint per month and the shape of the distribution is right-skewed.

### Bivariate graphs:
![out6](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out6.png)
![out7](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out7.png)

In the bar charts above we can see the relationship between quantity of joints smoked per month by cannabis user, aged 18 to 30 years old, and both major depression (first) and general anxiety (second) diagnoses in the last 12 months (Q->C). The explanatory variable is quantity of joints (quantitative), while the response variables are depression and anxiety diagnoses (categorical). There is a slightly increasing trend in the first graph, but not in the second.

![out10](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out10.png)
![out11](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out11.png)

In the graphs presented above we can see the correlation between frequency of cannabis use and both major depression and general anxiety (C->C). The explanatory variable is frequency of cannabis use (categorical), while the response variables are depression and anxiety diagnoses (categorical). Again, for the first graph we have a right-skewed distribution, which indicates that the more an individual smoked cannabis, the better were the chances to get diagnosed with depression. However, we cannot support the same as far as anxiety is concerned, which appears to have a more raffle and abnormal distribution. 

![out8](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out8.png)
![out9](https://github.com/Gkontopodis/Data-Management-Visualization/blob/master/Assignment%20Week%204/Graphs%20-%20Screenshots/out9.png)

The graphs presented above illustrate the association between cannabis use and both major depression and general anxiety diagnoses in young adults, aged from 18 to 30 years old, in the last 12 months (C->C). The explanatory variable is cannabis use (categorical) and the response variables are depression and anxiety diagnoses (categorical).

## Summary
To sum up, looking through the the last graphs, it can be noticed that there are some slight differences between the percentages of cannabis users compared to non-users. Major depression cases in cannabis users young adults (20.95%) seem to be slightly more than double compared to those of non-users (8.42%).In addition, general anxiety diagnoses in cannabis users (3.95%) appear to be also marginally more than double in comparison to the non-users (1.63%). It could be supported that there is a relative association between cannabis and such mental disorders, thus cannabis use increases the likelihood of meeting criteria for depression or general anxiety in the future. However, the sample is extremely small and it is unclear how representative it is, making the findings less reliable, since a large amount of error may be involved. 
