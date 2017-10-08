#django-app to seacrh playstore app
#initial version just to get and show 10 results in a table
#Installation

Required libraries 

   pip install -r requirements.txt
Frontend Depandencies ( need node, bower )
   Install node from node site 
   npm install -g bower
  

You can then install dependencies using
    bower install


To run this project 

   Go to directory containing manage.py


Initially will need to run 
   python manage.py migrate
   ( The above is to stop the warning messages from dango)
   python manage.py runserver

You can visit the site at:
   http://127.0.0.1/pstore/search_results/
# Some caveats I misunderstood the instructions and created an initial version which displays 'category', 'title', and 'link'.
# Then noticed that what you want is only app categories and respective fields So this change is done later
# I also thought that you wanted to cache the search results in some things like memcashe so as to retrieve results later.
# Changes applied later
