# tests/test_playground.py

import unittest
from unittest.mock import patch
from playground.__main__ import playground_up

class TestPlaygroundCommands(unittest.TestCase):

    @patch('playground.playground.subprocess.run')
    def test_playground_up(self, mock_subprocess_run):
        # Define the path to the docker-compose file
        compose_file = "path/to/playground_compose.yaml"
        
        # Call the function
        playground_up(compose_file)
        
        # Check that subprocess.run was called with the correct command
        mock_subprocess_run.assert_called_once_with(
            ["docker-compose", "--profile", "all", "-f", compose_file, "up", "-d"],
            check=True
        )

if __name__ == '__main__':
    unittest.main()
