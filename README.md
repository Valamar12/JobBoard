# T-WEB-501-TLS_10

## BASE CONFIGURATION

### 1. Create a virtual environment

Go in the directory where you want to import the JobBoard app

Install venv : 

```bash
sudo apt install python3-venv 
```

Create a virtual environment : 

```bash
python3 -m venv myenv
```

Activate the virtual environment : 

```bash
source myenv/bin/activate
```

### 2. Clone git repository

Go in the directory where you created your environment and clone the app

```bash
git clone git@github.com:EpitechMscProPromo2026/T-WEB-501-TLS_10.git
```

### 2. install requirements.txt

Go in the cloned folder and install the requirements for the app :
```bash
pip install -r requirements.txt
```

## BACKEND

### 1.Create the database

If you don't have postgres, install it using the following command :
```bash
sudo apt install postgresql postgresql-contrib
```

in your terminal, type 
```bash
sudo -i -u postgres
```
Enter psql mode

```bash
psql
```
in psql type :
```bash
CREATE DATABASE jobboard;
```

### 2.Change postgres password

Still in psql, type :
```bash
ALTER USER postgres WITH PASSWORD 'postgres';
```

### 3.Execute django migration

First, we need to reset the migrations, move to the backend folder and type :

(there is two backend folder, it's the one containing the file manage.py)

```bash
python3 manage.py migrate database zero
```
```bash
rm -rf ./database/migrations
```

Then redo the migration : 

```bash
python3 manage.py makemigrations database 
```
```bash
python3 manage.py migrate database 
```

### 4.Populate the database

still in the backend folder, populate the database using fixture :
```bash
python3 manage.py loaddata database/fixtures/fixtures.json
```

### 5.launch the server

to launch the server use : 
```bash
python3 manage.py runserver
```

Now the server is lauched on :

[Backend link](http://localhost:8000)

## FRONTEND

### 1. Install the svelte app
go into the frontend folder and type :
  
```bash
npm install
```

### 2. Run the server

```bash
npm run dev
```

The frontend server is now opened on :

[Frontend link](http://localhost:5173)


