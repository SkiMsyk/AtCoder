# setup
```
$ pip install online-judge-tools
$ npm -g install atcoder-cli
```

# login 

```
$ acc login
$ oj login https://atcoder.jp
```


# download contest files

```{shell}
$ acc new abc222
```

# test
solution is written in `main.py` and test-case are in `tests/`
```
$ oj t -c "python3 main.py" -d tests/
```

# submit

```
$ acc submit main.py
```