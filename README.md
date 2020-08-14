### DigitalCognition
DigitalCognition - a Master Data Management System with built-in capability for Business Analytics and creating out of the box Machine Learning models and pipelines. 


### Business Offerings 

> Disparate Data Sources - Data integration involves combining data from several disparate sources, which are stored using various technologies and provide a unified view of the data.   


> Self Service Business Intelligence - As business you demand flexibility and less dependence on IT teams , while deriving maximum intel from your data.   


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
