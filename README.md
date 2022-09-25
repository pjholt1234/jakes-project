# Module Requirements

```
python -m pip install python-dotenv
```

```
python -m pip install mysql-connector
```

```
python -m pip install bcrypt
```

# Additionally Files
.env


# MySQL Setup
Install MySql

Install db schema
```
mysql -u [root_user] -p -v --default-character-set=utf8 < "[Location of schema.sql]"
```

FIX for mysql command not found
```
SET PATH=%PATH%; C:\Program Files\MySQL\MySQL Server 8.0\bin
```