#django-app to seacrh playstore app

Required libraries 

```pip install -r requirements.txt```
Frontend Depandencies ( need node, bower )
```
   Install node from node site 
   npm install -g bower
```  

You can then install dependencies using
  ```  bower install```


To run this project 

   Go to directory containing manage.py


Initially will need to run 

```
   python manage.py makemigrations 
   python manage.py migrate
   python manage.py runserver
```
You can visit the site at:
   
   - http://127.0.0.1:8000/pstore/search_results/
   - http://127.0.0.1:8000/pstore/search_apps/
