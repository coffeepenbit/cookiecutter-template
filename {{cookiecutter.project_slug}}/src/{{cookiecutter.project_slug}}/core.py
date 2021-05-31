import logging

from . import cli


LOGGER = logging.getLogger(__package__)
LOGGING_FORMAT = "%(levelname)s:%(name)s:%(message)s"


def main():
    cli_args = cli.get_cli_args()
    configure_loggers(cli_args.loglevel, LOGGER, LOGGING_FORMAT)

    LOGGER.info("Launching program")

    conf_settings = utils.get_conf(cli_args.conf_path)

    print("Hello, world!")


def configure_loggers(loglevel, logger, logging_format):
    formatter = logging.Formatter(logging_format)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(loglevel)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(loglevel)
