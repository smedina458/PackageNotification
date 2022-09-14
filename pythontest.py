import cgi

form = cgi.FieldStorage

username = form.getvalue("username")
carselection = form.getvalue("cars")

print(username)
print(carselection)