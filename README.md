# feapson

Same as json.dumps or json.loads, feapson support feapson.dumps and feapson.loads

Example:

```python
>>> import feapson
>>> feapson.dumps({"a": True, "b": False, "c": [1, 2, 3]})
'{"a": True, "b": False, "c": [1, 2, 3]}'

>>> feapson.dumps({"a": True, "b": False, "c": [1, 2, 3]}, indent=4, ensure_ascii=False)
'''{
    "a": True,
    "b": False,
    "c": [
        1,
        2,
        3
    ]
}'''

>>> feapson.loads('{"a": True, "b": False, "c": [1, 2, 3]}')
{'a': True, 'b': False, 'c': [1, 2, 3]}

>>> feapson.loads('{"a": true, "b": false, "c": [1, 2, 3]}')
{'a': True, 'b': False, 'c': [1, 2, 3]}
```

Install:

```shell
pip install feapson 
```