[![GitHub version](https://img.shields.io/static/v1?label=Version&message=v1.0.2&color=blueviolet&style=flat-square)](https://github.com/maickom88/where_watch_backend_TDD_AND_CLEAN_ARCHITECTURE/releases/tag/v1.0.2)
[![GitHub doc](https://img.shields.io/static/v1?label=Documentation&message=Swagger&color=blueviolet&style=flat-square)](https://where-watch.herokuapp.com/docs)

![](https://github.com/maickom88/where_watch_backend_TDD_AND_CLEAN_ARCHITECTURE/blob/develop/photos/banner.png?raw=true)
## Where Watch<br><br> 🎬  Application to find movies and series and find out where and on which platforms they are available.


<img align="center" alt="Rafa-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">This application was made in python using scraper techniques using Seleniu

### ⚠️ Heads up
This api is not official, the data taken comes directly from the website [Just Watch](https://www.justwatch.com/)
See website for more details <br>
You can have the url in production on Heroku by clicking here and have access to documentation.
> Wait a few minutes, Heroku sleeps the application if there are no requests at the time

### 🥳 Let's get started 
👇🏼 Clone the repository on the develop branch. This branch contains all the features and you don't need to do anything other than run the command below!

```python
pip install -r requirements.txt
```
👇🏼 Soon after runs the command to start the server
```python
uvicorn main:app --reload 
```
For now the app is only accepting the following providers
- dnp (Disney Plus)
- gop (Globo Play)
- nfx (Netflix)
- prv (Prime Video)
