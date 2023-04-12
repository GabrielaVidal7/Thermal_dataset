import yaml

data_yaml = dict(
    train = 'Dataset/test',
    val = 'Dataset/validation',
    nc = 1,
    names = ['person']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)