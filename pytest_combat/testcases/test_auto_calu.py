import yaml

with open("D:\pycharm\pythonproject\pytest_combat\data\calc.yaml") as f:
    datas = yaml.safe_load(f)
    print(datas)