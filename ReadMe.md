## Procurement System

### Requirement
 - python 3.9 or higher
 - pip install virtualenv (if venv fail)
 - nodejs (for development)
-----------

### Setup
1. Create a python virtual environment
```
py -m virtualenv <env_name>
```

or

```
py -m venv <env_name>
```

2. Activate virtual environment
```
<env_name>\Scripts\activate
```
3. Install required modules
```
pip install -r requirement.txt
```

4. Rename `env` to `.env` and modify variables

5. Change `NPM_BIN_PATH` to your nodejs installation (for development only)

6. Start django serer
```
py manage.py runserver [port]
```

7. Start django tailwind (for development only)
```
py manage.py tailwind start
```

----------------
