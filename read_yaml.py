import yaml

with open('practice_yaml.yaml') as f:
    yam = yaml.load(f,Loader = yaml.FullLoader)

print(yam["long string2"])
print("HI")