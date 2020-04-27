# DigitalCognition
DigitalCognition - Main repo - Core Product 

### Broad level steps to follow - in case you get stuck get in touch with Rohit 
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

- Create a ANACONDA virtual environment witrh Pythin=3.8 - name it - dc_venv. 

```
$ conda create -n dc_venv python=3.8
```

- Install all the dependencies from  - requirements.txt , file 

```
$ pip install -r requirements.txt
```

- Run the initial Migrations for the Django apps 

```
$ python manage.py migrate
```



