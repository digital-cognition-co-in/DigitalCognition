### MOVED HERE -- https://github.com/RohitDhankar/digitalCognition






#

</br>

### DigitalCognition
DigitalCognition - a Master Data Management System with built-in capability for Business Analytics and creating out of the box Machine Learning models and pipelines. 

##### Existing product demo videos are here - feel free to go through the entire PlayList of Videos

- YouTube link of Demo Videos - https://www.youtube.com/watch?v=DTAgjm3VOjQ&list=PLLpHcww3qjp5DGRe_OTVO94n7i13bvTdV&index=9
- YouTube link of Demo Videos - https://www.youtube.com/watch?v=zydsrBWTbEA&list=PLLpHcww3qjp5DGRe_OTVO94n7i13bvTdV&index=5

### Highly Customizable SaaS product with high level features as enlisted below 

> Disparate Data Sources - Data integration involves combining data from several disparate sources, which are stored using various technologies and provide a unified view of the data.   


> Self Service Business Intelligence - As business you demand flexibility and less dependence on IT teams , while deriving maximum intel from your data.   


#

<br/>


### Features and Offerings

> Kindly consider this is a work in progress project . As listed below we mention our features to be ```Tableau like``` , this does not in any manner mean we are Copying from Tableau or any such other BI tools etc . We are just very highly inspired by them and others in this niche. 

- [X] `EDA- Exploratory Data Analysis - Work in Progress` 
- [X] `Tableau like MetaData Management - Work in Progress` 
- [X] `Tableau like Drag and Drop widgets - Work in Progress` 
- [X] `Tableau like Forms and Reports - Work in Progress` 
- [X] `Tableau like Executive Dashboards - Work in Progress`
- [X] `Work in Progress` 

<br/>


#



#### For developers > If you want to contribute

- Clone the repository on your local machine. 
```
$ git init
$ git clone https://github.com/digital-cognition-co-in/DigitalCognition.git
$ cd DigitalCognition/
```
- See which all branches are available on the remote
```
$ git branch -a
```
- Move to the - develop , branch
```
$ git checkout develop
```
- You should now see the asterix in front of the branch *develop 

```
* develop
  master
```

- Create a CONDA virtual environment with Python=3.8 , lets say u name it - dc_venv. 

```
$ conda create -n dc_venv python=3.8
```

- Install all dependencies from  the - requirements.txt , file 

```
$ pip install -r requirements.txt
```

- Run the initial Migrations for the Django apps 

```
$ python manage.py migrate
```
