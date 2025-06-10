#get feidls from feature layer
for field in fl.properties.fields: #where f1 is the feature layer
    print(f"{field['name']}: {field['alias']}")
