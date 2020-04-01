# Total

## Build virtual environment

```
    >python -m venv {virtual name}

```
* Mac
  
```
    >source {virtual name}/bin/activate
```
* Windows

```
    >{virtual name}\Scripts\active
```
## Install requirements

```
    >install -r requirments.txt
```

## Run server

* Run the command below to start this code.

``` 
    >cd project
    >python manage.py runserver
```

## Test case

* status

```
    status_code : 200
```

* head

```
    Content-Type application/json

```

* body

```jason
{
    'total':6
}
```

## Run Test

```
    >cd tests
    >pytest test_total.py 
```
