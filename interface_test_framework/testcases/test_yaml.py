import yaml


def test_yaml_1(data,filename_yaml):
    env = {
        "default": "dev",
        "testing-studio":
            {
                "dev": "127.0.0.1",
                "test": "127.0.0.2"
            }
    }
    with open("filename_yaml", "w") as f:

        yaml.safe_dump(data=data,stream=f)