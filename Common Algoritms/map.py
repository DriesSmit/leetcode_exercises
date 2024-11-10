def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

# Note: The computation is performed lazily and only when required.
print([val for val in x])