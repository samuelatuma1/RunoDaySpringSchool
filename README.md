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
  Here is the example content of the .env file
  <ul style='background-color : grey; padding : 10px;'>
    <p>SECRET_KEY = 'secret_key_only_me_know'</p>
    <p>DB_NAME = 'db_name'</p>
    <p>DB_PASSWORD = '12345'</p>
    <p>DB_USER = 'db_user'</p>
    <p>EMAIL_HOST_USER = 'emailusername'</p>
    <p>EMAIL_HOST_PASSWORD = 'email Password'</p>
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


