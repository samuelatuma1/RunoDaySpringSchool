# RunoDaySpringSchool

<h1>To run locally, do the usual:</h1>
  <li>Create a Python 3.8+ virtualenv</li>
  <ul>
    Install dependencies:
    <li>pip install -r requirements.txt</li>
  </ul>

  <ul>
    Make Migrations
    <li>python manage.py makemigrations</li>
    <li>python manage.py migrate</li>
  </ul>

  <ul>
    Create SuperUser
    <li>python manage.py createsuperuser</li>
  </ul>

  <p>Create a .env file on the root folder.</p>
  Here is the content of the .env file
  <ul style='background-color : grey; padding : 10px;'>
    SECRET_KEY = 'django-insecure-oabe-2rg*#fwz+vk&wxjricrl6i8j+jiy3(+ju9@jb7qw#-#(!'
    DB_NAME = 'runodayspring3'
    DB_PASSWORD = '11235813'
    DB_USER = 'runodayspring'
    EMAIL_HOST_USER = 'atumasaake@gmail.com'
    EMAIL_HOST_PASSWORD = '11235813'
  </ul>


<section>
  <header>About </header>
  <main>
      <p>
        This application serves the need of a school website as well as a school management system.  
      </p>
      <ul>
        It provides interface for
        <li>Registration of school staff and pupils</li>
        <li>School teaching staff to upload puplils results</li>
        <li>Interaction between staff and pupils</li>
        <li>Pupils to view/download results</li>
      </ul>

  </main>
</section>


