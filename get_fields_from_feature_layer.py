#get feidls from feature layer
for field in fl.properties.fields:
    print(f"{field['name']}: {field['alias']}")
