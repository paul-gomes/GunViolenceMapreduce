# Gun Violence Mapreduce

## Dataset Link
https://www.kaggle.com/jameslko/gun-violence-data

## Project Description
This is a map-reduce job to find the state with the most deaths in gun violence. MapReduce job has been written in python langague. 

## Dataset Description

This is a gun violence dataset from 2013 to 2018. Dataset is collected from Kaggle. Dataset has 240k rows and 29 columns. 

- **VOLUME**   : The dataset is quite large as the size of the data is 34MB 
- **VARIETY**  : the dataset is structured and relational 
- **VELOCITY** : The data is updated 3 months ago.  
- **VERACITY** : Source of the data is http://www.gunviolencearchive.org/, which is a non-profit corporation and provides information about the gun violence in the US. Therefore, it is safe to assume that the **veracity** of the dataset is reliable  
- **VALUE**    : we can extract valuable information from the dataset to perform actions against gun violence. 


## Bigdata question #1

- For each state, calculate the number of gun violence incidents.

## Bigdata result chart
![numIncidentsPerState](https://github.com/paul-gomes/GunViolenceMapreduce/blob/master/image/NumOfIncidentsResultChart.PNG "Clustered column chart for number of incidents per state")

## Bigdata qustion #2
- For each state, calculate the sum of the number of injured

## Bigdata result chart
![numInjuredPerState](https://github.com/paul-gomes/GunViolenceMapreduce/blob/master/image/NumOfInjuredResultChart.PNG "Clustered column chart for number of injured per state")

## Bigdata question #3

- For each state, calculate the sum of the number of killed.

## Bigdata result chart
![numKilledPerState](https://github.com/paul-gomes/GunViolenceMapreduce/blob/master/image/NumOfKilledResultChart.PNG "Clustered column chart for number of kills per state")



