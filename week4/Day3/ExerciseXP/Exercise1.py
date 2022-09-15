#1 Convert the two following lists, into dictionaries.
#Hint: Use the zip method
#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result =dict(zip(keys,values));
print ((result));