import os

import pytest
from molecule.test.conftest import change_dir_to
from molecule.util import run_command

from molecule import logger

LOG = logger.get_logger(__name__)


def test_command_init_scenario(temp_dir):
    role_directory = os.path.join(temp_dir.strpath, "ansible-test-init")
    cmd = ["molecule", "init", "role", "ansible-test-init"]
    assert run_command(cmd).returncode == 0

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")
        cmd = [
            "molecule",
            "init",
            "scenario",
            "test-scenario",
            "--role-name",
            "ansible-test-init",
            "--driver-name",
            "ignite",
        ]
        assert run_command(cmd).returncode == 0

        assert os.path.isdir(scenario_directory)

        cmd = ["sudo", "molecule", "check", "-s", "test-scenario"]
        assert run_command(cmd).returncode == 0

        cmd = ["sudo", "molecule", "destroy", "-s", "test-scenario"]
        assert run_command(cmd).returncode == 0
