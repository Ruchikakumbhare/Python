#................................dict{}Methods................................

info = {
    "fname":"ruchi",
    "lname":'kumbhrare',
    "contact":987
}

print(info)
print(len(info))
print(info['fname'])

info.pop('fname')
print(info)
# info.clear()
# print(info)
info.update({'no':123})
print(info)
info.update({'contact':12345})
print(info)
print(info.get("contact"))

