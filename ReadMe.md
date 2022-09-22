## Procurement System

### Requirement
 - python 3.9 or higher
 - pip install virtualenv
 - nodejs
-----------

### Setup
1. Create a python virtual environment
```
py -m virtualenv <env_name>
```
2. Activate virtual environment
```
<env_name>\Scripts\activate
```
3. Install required modules
```
pip install -r requirement.txt
```

or

```
py -m pip install -r requirement.txt
```

4. Modify `.env` variables

5. Change `NPM_BIN_PATH` to your nodejs installation

6. Start django serer
```
py manage.py runserver [port]
```

7. Start django tailwind
```
py manage.py tailwind start
```

----------------
