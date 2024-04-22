#!/usr/bin/python3


import argparse
import logging
import os


_LOG = logging.getLogger(__name__)


def get_system_info(cnt: int):
    _LOG.info("System info: %s", os.uname())
    current_dir = os.getcwd()
    _LOG.info("We are in: %s", current_dir)
    content = os.listdir(current_dir)
    _LOG.info("List of dirs: %s", content)
    test_dir = "test_dir"
    _LOG.info("Creating dir: %s", test_dir)
    os.mkdir(test_dir)
    
    for i in range(cnt):
        dir_name = f"dir_{i}"
        dir_path = os.path.join(test_dir, dir_name)
        _LOG.info("Creating dir: %s", dir_path)
        os.mkdir(dir_path)
        _LOG.info("List of dirs: %s", os.listdir(test_dir))
    cmd = f"rm -rf {test_dir}"
    _LOG.warning("Deleting dir: %s", test_dir)
    os.system(cmd)


def _parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--count",
        action="store",
        required=True,
        help="Pass the amount of dirs to create"
    )
    return parser


if __name__ == "__main__":
    args = _parse().parse_args()
    cnt = int(args.count)
    get_system_info(cnt)