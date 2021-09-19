# yubaba
Yubaba makes your code shorter.

## Usage

### Logical operator

* And
* Or
* Xor
* Nand
* Nor
* Xnor

```python
x = a and b and c and d

# same as
x = And([a, b, c, d])
```

### Conditional Branch

* If
* Nif
* print_if


```python
if cond:
    func(arg1, arg2)
cond and func(arg1, arg2)

# same as
If(cond, F(func, arg1, arg2))
# or
If(cond, lambda: func(arg1, arg2))
```

Be careful that these are not same.

```python
# `r` will not be overwritten if the `cond` is False
if cond:
    r = func(arg1, arg2)

# `r` will be overwritten as None if the `cond` is False
r = If(cond, F(func, arg1, arg2))
```
