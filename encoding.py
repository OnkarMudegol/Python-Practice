#encode a 5 letter word to have a # between everr pair
a = str(input())
new_a= ""
for i in a:
    new_a= (new_a+i+"#")
print(new_a[:-1])

