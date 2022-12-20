# Backend for Recipe Manager

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/vtwoptwo/ie-backend">
    <img src="img/recipe.png" alt="Logo" width="200" height="200">
  </a>



  <p align="center">
    An end to end process to develop, test, and deploy a small scale application using CI/CD, GitHub Actions, and Docker.  The application is built using two repositories: one for the frontend and one for the backend. 
    <br />
    <br />
    <br />
    <a href="https://github.com/vtwoptwo/ie-frontend"><strong>See the Frontend»</strong></a>
    ·
    <a href="#about-the-project"><strong>See the project»</strong></a>
    ·
    <a href=#usage>How to use this repo</a>
    ·
    <a href="https://github.com/vtwoptwo/ie-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/vtwoptwo/ie-backend/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is to practice end-to-end development using best practice implementations of early functional as well as unit testing, CI/CD and Dockerization of applicatins. 

I am also making this repo explicity detailed so that anyone can follow it from start to finish.


<h3> General description </h3>
<br>
<br>
Implement an anonymous web application for managing cooking recipes.
Single page application.
<br>

Functional requirements:
* The user must be able to create, read, update, and delete recipes (CRUD).
* The user must be able to rate recipes from 1 to 5 stars.
* The user must be able to mark recipes as Favorite with a checkbox.
* The user must be able to create and edit recipes in a modal view. 
* User authentication is not needed.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![VueJs][Vue.js]][Vue-url]
* [![Postgres][Postgres]][Postgres-url]
* [![Flask][Flask]][Flask-url]
* ![Bicep](https://img.shields.io/badge/BICEP-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)


### Tools Used

* [![Postman][Postman]][Postman-url]
* [![Docker][Docker]][Docker-url]
* ![Azure](https://img.shields.io/badge/BICEP-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
<h3> Make sure you know about the following concepts before starting: </h3>

### RestAPI

* REST (Representational State Transfer) is a software architectural style that defines a set of constraints to be used for creating web services. 

* A REST API (Application Programming Interface) is a set of rules that defines how two systems can interact over the internet, using the HTTP protocol. 

* A REST API defines a set of functions that a developer can use to send requests and receive responses. The requests and responses are typically in the form of JSON (JavaScript Object Notation) or XML (Extensible Markup Language) messages.





### Flask

<p align="left">Flask is a web (micro)framework for Python:
  <ul> 
    <li>Multiple extensions available to enhance features</li>
    <li>It makes programming a website much easier than usingplain HTTPServer.</li>
    <li>Integrated support for unit testing</li>
    <li>Contains development server and debugger</li>
    <li>Relies on Jinja templating engine to ease HTML creation </li>
  </ul>
<p>

### Postgres / PgAdmin
The Database: 
* PGAdmin is a PostgreSQL Management Tool used to interact with the Postgres database sessions, both locally and remote servers as well. You can use PGAdmin to perform any sort of database administration required for a Postgres database.
* PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users. It is the default database for macOS Server, and is also available for Linux, FreeBSD, OpenBSD, and Windows.








### Prerequisites
You will need the following software downloaded on your workstation:

* [PostgreSQL](https://www.postgresql.org/download/) 
* [PgAdmin](https://www.youtube.com/watch?v=h4WbPpQQekw)
* [Postman](https://www.postman.com/downloads/)
* [Node.js](https://nodejs.org/en/download/)


### Installation

1. Clone the backend repo
   ```sh
   git clone https://github.com/vtwoptwo/ie-backend.git
   ```
1. Clone the frontend repo
   ```sh
   git clone https://github.com/vtwoptwo/ie-frontend.git
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- USAGE EXAMPLES -->





## Usage


<div align="center">
    <img style="border-radius:10px;" src="img\homepage.JPG">
</div>
<div align="center">
    <img style="border-radius:10px;" src="img\recipes.JPG">
</div>

<div align="center">
    <img style="border-radius:10px;" src="img\createrecipe.JPG">
</div>

<div align="center">
    <img style="border-radius:10px;" src="img\editrecipe.JPG">
</div>

<div align="center">
    <img style="border-radius:10px;" src="img\updaterecipe.JPG">
</div>




<!-- ROADMAP -->
## Roadmap in Steps
Make sure you have everything downloaded from the [pre-requisites](#prerequisites) before continuing.

### Set-Up


1. Create project repository in Github
  ```sh
  Name: Backend | Access: Public |                         Add .gitignore template: None
   ```
2. Open VSCode and select "Clone Github Repository"
3. Install Virtualenv: 
  ```sh
  pip install virtualenv
  #I had an error for so run this command just in case before starting
  python -m pip install psycopg2 
  ```
  
4. Create new virtualenv:
  ```sh
  py –m venv .venv
  ```

5. Activate new virtual environment
  ```sh
  .venv/scripts/activate
  ```

6. Install Flask 
  ```sh
  pip install flask, flask_sqlalchemy, python-dotenv, flask_cors
  ```  


### Implementing the Flask API

1. In your PGAdmin right click on databases and create a new database. The following is the table we will create in the dabase using code-first architecture. 

  <table align="center" >
  <tr>
    <th>Attribute</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Name</td>
    <td>String</td>
    <td>Name of recipe</td>
  </tr>
  <tr>
    <td>Ingredients</td>
    <td>String</td>
    <td>Required Ingredients</td>
  </tr>
  <tr>
    <td>Steps</td>
    <td>String</td>
    <td>Instructions on creating the recipe</td>
  </tr>
  <tr>
    <td>Rating</td>
    <td>Int</td>
    <td>1-5 Star Rating</td>
  </tr>
  <tr>
    <td>Favorite</td>
    <td>bool</td>
    <td>Marked as either a favorite or not</td>
  </tr>
</table>

<br>

2. In your requirements make sure you have the following requirements set: 
  ```sh
  Flask==2.2.2
Flask-Cors==3.0.10
Flask-SQLAlchemy==2.5.1
psycopg2==2.9.3
python-dotenv==0.21.0
SQLAlchemy==1.4.41
pytest
pytest-cov
  ```
```sh
pip install -r ./requirements.txt
```
3. Implementing the "Code-First Approach" with the DB

Creating a table model for our recipe tracker (in models.py)
```sh
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.String(500), nullable=False)
    favorite = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name}'
    
    def __init__(self, name, ingredients, instructions, favorite, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.favorite = favorite
        self.rating = rating
```
In the python CLI to test the code/database: 
```sh 
from app import app,db,Recipe
with app.app_context():
  db.create_all()
r1 = Recipe(name="Soup", ingredients="veggies,vegeta,water,chicken", instructions=("Boil all ingredients for a few hours"), favorite=True, rating=5) 
>>> with app.app_context():
  db.session.add(r1)
  db.session.commit()
```
run the backend
```sh
py ./run.py
```

### Frontend
Implementing vue.js

1. In your frontend folder run the following: 
```sh 
$ npm install -g @vue/cli
$ vue create frontend

#Manually select features (Babel, Router)
#Version: 2.x
#History mode for router: yes
#Config: dedicated config files
#Save for future projects: No
```

to run the vue application run:
```sh 
cd frontend
npm run serve
```
To create a production build, run 
```sh 
npm run build
```
To quit running it
```sh
crtl + c
```




2. Install the following libraries


```sh
npm i axios
npm install bootstrap@4.6.0 --save


```

3. Testing the API by opening up POSTMAN and sending in requests to http://127.0.0.1:5000/recipes

Request = GET
```sh

{
    "name": "Tortilla de patata",
    "ingredients": "potatoes,onions,salt,eggs",
    "instructions": "if u dont know how to make it google it",
    "favorite": false,
    "rating": 4
}
```

Request = POST
```sh

{
    "name": "Tortilla de patata",
    "ingredients": "potatoes,onions,salt,eggs",
    "instructions": "if u dont know how to make it google it",
    "favorite": True,
    "rating": 4
}
```
4. Ensure that your index folder has the same routes as your backend_api/routes.py 

```sh
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }, 

  {
    path: '/skull',
    name: 'Skull',
    component: Skull
  },
  {
    path: '/recipes',
    name: 'AppRecipes',
    component: AppRecipes
  }
]
```

5. Your main.js initiates the App.vue app: ensure that any extra components frome vue that you use are imported in the main.js file


More documentation is available here: 

[ Vue JS Boostrap Components ](https://bootstrap-vue.org/docs/components) 

```sh

import Vue from 'vue'
import 'bootstrap-vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import { BootstrapVue } from 'bootstrap-vue'
import { BFormRating } from 'bootstrap-vue'
Vue.component('b-form-rating', BFormRating)
import { IconsPlugin } from 'bootstrap-vue'
Vue.use(IconsPlugin)
Vue.use(BootstrapVue)

```

6. Understanding the routing in VUE using CRUD


  <table align="center" >
  <tr>
  <th>Description</th>
    <th>GET</th>
    <th>POST</th>
    <th>PUT</th>
    <th>DELETE</th>
    
  </tr>
  <tr>  
    <td>Functions </td>
    <td>RESTgetRecipes()</td>
    <td>RESTcreateRecipe(payload)</td>
    <td>RESTupdateRecipe(payload, recipeId)</td>
    <td>RESTdeleteRecipe(id) </td>
   

  </tr>
  <tr>
    <td>Action</td>
    <td>Reads all recipes </td>
    <td>Creates new recipes by using a payload variable. These are variables which are mapped to the attribute variables in the database in order to create a new instance.</td>
    <td>Updates an existing recipe by using the recipe id to identify it and the payload to change specific values. Any values not changed remain the same. </td>
    <td>Deletes a recipe using the recipe id</td>
  </tr>
    <tr>
    <td>Responses</td>
    <td>x </td>
    <td>x</td>
    <td>x </td>
    <td>x</td>
  </tr>

</table>

<br>

7. Understanding the routing between pages or components in the app
  <table align="center" >
  <tr>
    <th>Function</th>
    <th>Description</th>

    
  </tr>
  <tr>  
    <td>gotohome()</td>
    <td>initForm()</td>
    <td>gonSubmit(evt)</td>
    <td>onSubmitUpdate(evt)</td>
    <td>deleteRecipe(recipe)</td>
    <td>editRecipe(recipe)</td>
    </tr>
     <tr>  
    <td>Switches back to the Home.vue page</td>
    <td>Initialized the forms using the HTML Modal Code</td>
    <td>event tracking of Submit Button to create a Recipe</td>
    <td>event tracking of Submit Button to edit a Recipe</td>
    <td>event tracking of Delete Button to delete a Recipe</td>
    <td>event tracking of Update to initialize update form </td>
    </tr>
</table>



## Implementing CI/CD
* Workflows stored as yml files 
* fullly integrated with GitHub
* Respond to GitHub events
* Live logs and visualized workflow execution 
* community powered workflows
* GitHub hosted or self-hosted runners
* Built-in secret store
  
To understand the infrastructure see the following diagram: 

<div align="center">
    <img style="border-radius:10px;" src="img\infra.jpg">
</div>

To see the infrastructure as code written in Bicep, refer to: [IaC](https://github.com/vtwoptwo/ie-IaC/issues)

Within the bicep file, in order to launch two webapps at once I implemented the following for loop: 
```sh
param names array = [ 'FE', 'BE' ]
```

```sh
  module appService 'modules/appModule.bicep' = [  for i in range(0,2): {
    name: 'appService${names[i]}'
    params: {
      location: location
      appServiceAppName:'${appServiceAppName}${names[i]}'
      appServicePlanName: appServicePlanName
      environmentType: environmentType
      dbhost: dbhost
      dbuser: dbuser
      dbpass: dbpass
      dbname: dbname
    }
  }]

 // output using loop

  output appServiceAppHostName array = [ for i in range(0,2): {
    name: 'appService${names[i]}'
    value: appService[i].outputs.appServiceAppHostName
  }]
 
```
See the [IaC Repository](https://github.com/vtwoptwo/ie-IaC) for more info.

## 2. GitHub Actions

### Frontend: 
For the [Frontend Workflow](https://github.com/vtwoptwo/ie-frontend/actions/runs/3734402296/workflow),  I had to figure out a way to push different environment variables to the .env file that vue.js reads automatically. 
Since both webapps were being deployed as a production slot, the `dev` webapp did not recognize the correct environment file. To fix this I implemented the following code in the yml workflow: 

```sh
      - name: Create .env for development
        if: github.ref == 'refs/heads/dev'
        run: |
          echo "${{ secrets.ENV_DEV_FILE }}" > .env.production
      - name: Create .env for production
        if: github.ref == 'refs/heads/main'
        run: |
          echo "${{ secrets.ENV_PROD_FILE }}" > .env.production
```

I set the <b>VUE_ENV_ROOT_URL={url of backend}</b> as two separate repository secrets in GitHub and call either file to be the official .env.production file based on which branched was pushed. 

To increase the deployment efficiency, I deployed using release.zip format. 
<div align="center">
    <img style="border-radius:10px;" src="img\dev-fe.JPG">
</div>
<div align="center">
    <img style="border-radius:10px;" src="img\prod-fe.JPG">
</div>


### Backend: 

For the [Backend Workflow](https://github.com/vtwoptwo/ie-backend/actions/runs/3727849287/workflow), I implemented a pytest job in the build of the application, and then conditional deployments depending on which branch was pushed. 

The testing was implemented as follows: 

```sh
    - name: Test with pytest
      run: |
        python -m pytest --cov=backend_api -v
```
<div align="center">
    <img style="border-radius:10px;" src="img\dev-be.JPG">
</div>
<div align="center">
    <img style="border-radius:10px;" style="border-radius:10px;" style="border-radius:10px;" src="img\prod-be.JPG">
</div>



See the [open issues](https://github.com/vtwoptwo/ie-backend/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

The idea is to create a nice and simple repo for CPP Basic Rules, information, definitions, best practices etc. Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.



If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vtwoptwo/ie-backend.svg?style=for-the-badge
[contributors-url]: https://github.com/vtwoptwo/ie-backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vtwoptwo/ie-backend.svg?style=for-the-badge
[forks-url]: https://github.com/vtwoptwo/ie-backend/network/members
[stars-shield]: https://img.shields.io/github/stars/vtwoptwo/ie-backend.svg?style=for-the-badge
[stars-url]: https://github.com/vtwoptwo/ie-backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/vtwoptwo/ie-backend.svg?style=for-the-badge
[issues-url]: https://github.com/vtwoptwo/ie-backend/issues
[license-shield]: https://img.shields.io/github/license/vtwoptwo/ie-backend.svg?style=for-the-badge
[license-url]: https://github.com/vtwoptwo/ie-backend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/vera-prohaska-31734b1b5/
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[CPP-url]: https://cplusplus.com/
[C++]: https://img.shields.io/badge/C++-blue
[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Postman]: https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white
[Postman-url]: https://www.postman.com/
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
