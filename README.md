<img align="right" src="https://github.com/Jackson-hub/CROPify/blob/main/static/images/logo.png" width="100" height="100">

# CROPify
A Flask-based web application for farmers to find out the crops which can grow perfectly on their fields.

### This is my submission for HackDSC-2021.

# Motivation:
Traditional cropping patterns are not effective in today's rapidly changing, unpredicted climate and polluted soils. Likewise, every region is unique in relation to each other and has various properties. Your goal is to design a system to predict the most suitable crop for that region, harvest time, plantation pattern and maintenance of that crop for better yield utilizing information like soil quality, weather, resources and other factors that affect crop production.
<p> 
Keeping this in mind, I have created a web application which will help farmers to identify the best crop that they can grow in their respective fields, keeping in mind all the properties discussed before.

# Tech Stack Used:
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="30" src="https://github.com/tomchen/stack-icons/raw/master/logos/bootstrap.svg"></code>
<code><img height="30" src="https://symbols.getvecta.com/stencil_80/56_flask.3a79b5a056.jpg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code>
<code><img height="30" src="https://matplotlib.org/_static/logo2.svg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code>

# Data-set Used:
For this application, I used datasets from Kaggle.
- [Crop Recommendation ](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset) 

# Algorithms Used:
I have used a variety of algorithms for this problem, namely Logistic Regression, Decision Trees, SVM, Random Forest to name a few.
<br>
For me, Random Forest has worked wonders, as it gave me 100% accuracy.
If you want an in-depth explaination on random Forest and how do they work, feel free to checkout <a href = "https://towardsdatascience.com/understanding-random-forest-58381e0602d2">this article</a>. 
<br>
![](https://github.com/Jackson-hub/CROPify/blob/main/static/images/comparisionCROPify.png)
<br>
# Features Used:
### The features used to solve this problem are:
1. Nitrogen Level: The percentage of nitrogen present in the soil.
2. Phosphorus Level: The percentage of phosphorus present in the soil.
3. Potasium Level: The percentage of potassium present in the soil.
4. Temperature: Temperature of the soil.
5. Humidity Level: Percentage of humidity of the soil.
6. PH Value: PH value of the soil.
7. Rainfall: The amount of rainfall(In mm).

# Functionalities of this application:
 1. On putting features like nitrogen %, phosphorus % etc, a farmer could find out which crop will suit his field the best.
 2. The farmer would also know the type of crop to field(for eg; a Rabi, or a Kharif crop). The application will also provide the suitable sowing and harvesting dates for the crops.
 3. After finding out the name of the crop, the farmer could also find out the importance of each feature; so as to get more acquainted with how the different features affect the soil.


#### To run this on your machine:
1. Make sure you have Python3, Flask installed.
2. In your terminal, cd to the folder you got this project in, and type <b><i>python run app.py<i></b>
3. And voila!!

# Screenshots:
![](https://github.com/Jackson-hub/CROPify/blob/main/static/images/crop1.png)
<br>
![](https://github.com/Jackson-hub/CROPify/blob/main/static/images/crop2.png)
<br>
![](https://github.com/Jackson-hub/CROPify/blob/main/static/images/crop3.png)

# Demo Video:
<div align="center">
  <img src="https://github.com/Jackson-hub/CROPify/blob/main/static/images/CROPifydemolast.gif" width="100%">  
</div>

# Explanation Presentation:
You can access the presentation <a href="https://docs.google.com/presentation/d/1kEqwQipxB7r72Ew_C2hjVFVZkyzEVBj5MPVLlRcQSkI/edit?usp=sharing">here</a>

# Future Improvements:
 1. An Crop Disease predictor could be added to this application. It could take input in for of an image, and predict if it is diseased or not.
 2. A feature in which after a farmer finds out about the most suitable crop, he could directy call any supplier of the said crop.
 3. This web application is not mobile-first. So if anyone out there could make it mobile-reponsive, that'd be great.

# Issues:
 1. The designing part of the web application is in a bit of mess😅.
 2. The UI could be improved.
 3. The web application is a bit slow during rendering. So anything to help speed up rendering would be great. 

# Hosting:
This application is hosted on Heroku:
https://cropify-northkeys.herokuapp.com/
<br>
P.S: It will take a ittle time to get started, but it's worth the wait!
