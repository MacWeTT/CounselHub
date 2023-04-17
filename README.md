# CounselHub
## A one stop solution for all your court issues.
[![My Tech Stack](https://github-readme-tech-stack.vercel.app/api/cards?title=Tech%20Stack%20Used&lineCount=1&theme=cyberpunk&line1=django,django,00ff91;tailwindcss,tailwindcss,06B6D4;python,python,3776AB;html5,html5,E34F26;)](https://github-readme-tech-stack.vercel.app/api/cards?title=Tech%20Stack%20Used&lineCount=1&theme=cyberpunk&line1=django,django,00ff91;tailwindcss,tailwindcss,06B6D4;python,python,3776AB;html5,html5,E34F26;)

### What's this?
A one stop project that deals with all court related issues, and makes the job of the client and lawyer easy by storing all the data on the database, which can be accessed using the Django framework used to build this website.

### How does it work?

The project is built on Django backend framework which is powered by Python, an interpreted, object-oriented, high-level programming language with dynamic semantics.


### How to start the project?
The process to do so is very simple. All you have to do is:
1. Make sure you have Python installed on your PC. Preferable version : >3.9
2. Clone the repository to a folder of your choice using either ``` git clone ``` or ``` Github Desktop ```.
3. After cloning, you have to create a virtual enviroment. I like to call it **env**. You can call it anything you like. You can achieve this by running the following command: ``` python -m venv env ``` 
> All the required dependencies will be installed in this **env**.
4. The next step would be to run the virtual environment. You can do so by running the command ``` ./env/scripts/activate ```.
5. After the virtual environment starts running, run the command ```pip install -r requirements.txt ```.
> This command will install all the required dependencies one by one in your virtual environment.
6. Now, you have to initialize the database. Do so by running ``` python manage.py makemigrations ``` and then ```python manage.py migrate```.
7. Once the process is complete, your project is ready. Run it by typing ``` python manaage.py runserver ```. It will run the application on ```localhost:8000```.
8. You can now open the application which is hosted on ```port 8000``` on your PC.


## Sreenshots
![Home](/gitassets/Image (2).png)
![Login](/gitassets/Image (3).png)
![Signup](/gitassets/Image (4).png)
![Dashboard](/gitassets/Image (1).png)
