**<h2>API with FastAPI</h2>**

###

A brief description of FastAPI and how to use it.

---

An API developed with `FastAPI` that returns information based on names via the `/name` route.

###

**<h2>Dependency Installation</h2>**

###

1️⃣- Clone the repository:

###
```powershell
git clone https://github.com/Kauan19-hub/Projects.git
```

2️⃣- Enter the cloned repository:

###
```powershell
cd Projects
```

3️⃣- Create and activate the Virtual Environment `env`:

###

Windows

###

```powershell
python -m venv env  ### Creates the env
```

###
```powershell
.\env\Scripts\activate ### Activates the env
```

MacOS/Linux

###

```powershell
python3 -m venv env
```

###

```powershell
source env/bin/activate
```

4️⃣- Install the dependencies:

###
```powershell
pip install fastapi uvicorn ### install FastAPI and Uvicorn directly (if you don't have requirements.txt)
```

**<h2>Running the Application</h2>**

###

After following the steps above, type:

###

```powershell
uvicorn main:app --reload
```

The application will be available at:

###

```powershell
http://127.0.0.1:8000/name
```

---

**<h2>Cloning for Tests</h2>**

###
```powershell
git clone [your-repository-url]
```

###
```powershell
cd [your-repository-folder]
```

###
```powershell
python -m venv env
```

###
```poweshell
.\env\Scripts\activate  # or source env/bin/activate
```

###
```powershell
pip install -r requirements.txt
```

###
```powershell
uvicorn main:app --reload
```

To test your API, you can use one of these Software applications: 

---

<div align="left">
  <a href="https://www.postman.com/" target="blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=black&style=for-the-badge" height="30" alt="postman logo" title="Download Postman" />
  </a>
  <img width="3" />
  <a href="https://insomnia.rest/download" target="blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/insomnia-5E00D3?logo=insomnia&logoColor=white&style=for-the-badge" height="40" alt="insomnia logo"  title="Download Insomnia" /> 
  </a>
</div>







