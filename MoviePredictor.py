# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:38:49 2019

@author: vishnu



* Action
* Adventure
* Animation
* Children's
* Comedy
* Crime
* Documentary
* Drama
* Fantasy
* Film-Noir
* Horror
* Musical
* Mystery
* Romance
* Sci-Fi
* Thriller
* War
* Western
*
"""

import pandas as pd
import numpy as np
import os.path
import json

df=pd.read_excel("final_movies.xlsx")
features=df.iloc[:,1:].values
labels=df.iloc[:,0].values

print("Welcome to Movie Predictor")
if not os.path.exists("USER_INFO.txt"):
    user_info={"Vishnu":3.5,"Aiswarya":5}
else:
    user_info={}
    with open("USER_INFO.txt","r") as databasefile:
        user_info=json.load(open("USER_INFO.txt"))
            
print("Enter your user id: ")
username=input()
print("Signing in...Please Wait!")
print(" ")

if username in user_info:
    avg_rating=user_info.get(username)
    new_user=0
else:
    user_info[username]=3.5
    avg_rating=user_info.get(username)
    new_user=1


with open("USER_INFO.txt","w") as databasefile:
      databasefile.write(json.dumps(user_info))


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(features_train,labels_train)

print("Choose one or more from the following genres you'd like to watch: ")
print(" ")
print("Enter all the genres you'd like from the following in a single line with space: ")
print(" ")
print("Action")
print("Adventure")
print("Children")
print("Comedy")
print("Crime")
print("Documentary")
print("Drama")
print("Fantasy")
print("Horror")
print("Musical")
print("Mystery")
print("Romance")
print("Sci-Fi")
print("Thriller")
print("War")

user_pref=input()
print(" ")
print("Loading your suggestions...Please Wait!")
print(" ")
default_values=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
user_array=np.append(avg_rating,default_values)
if "Action" in user_pref:
    user_array[1]=1
if "Adventure" in user_pref:
    user_array[2]=1
if "Children" in user_pref:
    user_array[3]=1
if "Comedy" in user_pref:
    user_array[4]=1
if "Crime" in user_pref:
    user_array[5]=1
if "Documentary" in user_pref:
    user_array[6]=1
if "Drama" in user_pref:
    user_array[7]=1
if "Fantasy" in user_pref:
    user_array[8]=1
if "Horror" in user_pref:
    user_array[9]=1
if "Musical" in user_pref:
    user_array[10]=1
if "Mystery" in user_pref:
    user_array[11]=1
if "Romance" in user_pref:
    user_array[12]=1
if "Sci-Fi" in user_pref:
    user_array[13]=1
if "Thriller" in user_pref:
    user_array[14]=1
if "War" in user_pref:
    user_array[15]=1

columns=['ratings','Action','Adventure','Children','Comedy','Crime','Documentary','Drama','Fantasy','Horror',
         'Musical','Mystery','Romance','Sci-Fi','Thriller','War']
new_df=pd.DataFrame(user_array.reshape(-1,len(user_array)),columns=columns).values

labels_pred=classifier.predict(new_df)
print("Your Recommended Movie is: ")
print(" ")
print(labels_pred)
print(" ")
print("Please rate the movie after watching it: ")
end_rate=float(input())
import statistics
average=[3.5]
average.append(end_rate)
if (new_user == 0):
    user_info[username]=statistics.mean(average)
if (new_user == 1):
    user_info[username]=statistics.mean(average)
print("Thank you!")
