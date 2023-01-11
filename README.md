# Machine-Learning-aided-Flood-Forecasting

![Flash-Flood_Floods_KIDS_1022_2x1](https://user-images.githubusercontent.com/105945382/211735853-064fd590-47e1-4c0e-a2f0-f35103c8e131.jpg)
<hr>

**A comparative study between different machine learning and deep learning algorithms to predict future flood disasters by analyzing 
historical data of previous flood data that ocurred in _Assam_ from 1926 to 2015.**

### This project was done under Internship programme at NUS-School of Computing in December 2022
<img align="right" width=450 src="https://user-images.githubusercontent.com/105945382/211739166-c812c826-0171-43cb-9855-2bc694ceb2ef.png" />

Floods are a recurrent phenomenon, the most common natural disaster in India, which cause huge loss of lives and 
damage to livelihood systems, property, 
infrastructure and public utilities. 
On average nearly 1600 people die every year due to floods, 75 lakh hectares of land is affected and the damage caused to crops, 
houses and public utilities is Rs. 1805 crores due to floods.
Flood prediction is difficult to predict due to its nonlinear and dynamic nature, 
various researchers have tackled this problem using different techniques ranging from physical models to image processing, 
we picked up time series forecasting by creating our own dataset from scratch extracted from different stations and government of India websites.

<hr>

## Dataset Used 

- We took data from the [Indian Flood Inventory](https://link.springer.com/article/10.1007/s11069-021-04698-6) to find the dates for floods.

- We extracted the information of Rain statewise data from [India Environment Portal](http://www.indiaenvironmentportal.org.in/media/iep/infographics/Rainfall%20in%20India/112%20years%20of%20rainfall.html).

- We have also extracted information of population from [world bank](https://data.worldbank.org/indicator/SP.POP.TOTL?locations=IN)  

- and [temperature](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data ) and made a dataset using all these features to perform our time series analysis.
