import yaml


def get_conf(conf_filepath):
    try:
        with open(conf_filepath, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Configuration file was not found at: \"{conf_filepath}.\""
        )
