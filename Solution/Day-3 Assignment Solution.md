```python
# Find the data type of a if a=9
a=9
print(type(a))
```

    <class 'int'>
    


```python
#Find the data type of a if a='9.'
a='9'
print(type(a))
```

    <class 'str'>
    


```python
#. Find the data type of a if a=(9)
a=(9)
print(type(a))
```

    <class 'int'>
    


```python
#Find the data type of a if a=False
a=False
print(type(a))
```

    <class 'bool'>
    


```python
#Find the data type of a if a=[1,2,3]
a=[1,2,3]
print(type(a))
```

    <class 'list'>
    


```python
#Find the data type of a if a=(1,2,3)
a=(1,2,3)
print(type(a))
```

    <class 'tuple'>
    


```python
#Find the data type of a if a={'key': 9}
a={'key':9}
print(type(a))
```

    <class 'dict'>
    


```python
#. Find the data type of a if a=1  +  9j
a=1  +  9j
print(type(a))
```

    <class 'complex'>
    


```python
#Set a=1  and   b=2. What data type is a/b?
a=1
b=2
print(type(a/b))
```

    <class 'float'>
    


```python
#Create a dictionary numbers =  {'one':1, 'two':2, 'three':3}. Pull out the number '2' by   calling the key 'two'
numbers =  {'one':1, 'two':2, 'three':3}
print(numbers['two'])
```

    2
    


```python
#Create a tuple with the numbers 8, 9, and   10?
numbers=(8,9,10)
print(type(numbers))
```

    <class 'tuple'>
    


```python
#1.  Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:

d = {one:1, two:2, three:3} 
d['one']

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-41afad7026d9> in <module>
          1 #1.  Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
          2 
    ----> 3 d = {one:1, two:2, three:3}
          4 d['one']
    

    NameError: name 'one' is not defined


NameError is occur when we try to access variable which is not defined. Here we not define "one" . we use it inside the dictionary "d" as "key". We declare it inside the ' ' because it is string. like 'one','two','three'


```python
d = {'one':1, 'two':2, 'three':3} 
print(d['one'])
```

    1
    


```python
#Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:

f = false not f
```


      File "<ipython-input-25-c2a4039e173f>", line 3
        f = false not f
                      ^
    SyntaxError: invalid syntax
    



```python
#Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:

lst = [1,3,5] 
lst[3]

```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-23-5c3ac3007a2e> in <module>
          2 
          3 lst = [1,3,5]
    ----> 4 lst[3]
    

    IndexError: list index out of range


IndexError generated when we try to access value out of index. Here max. index value is 2 and we try to access value store at index 3.


```python
lst = [1,3,5] 
lst[2]
```




    5


