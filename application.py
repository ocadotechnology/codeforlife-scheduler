"""
© Ocado Group
Created on 17/04/2025 at 09:40:11(+01:00).

A worker for the celery beat.
"""

import atexit
import subprocess

from codeforlife.server import Server as _Server


# pylint: disable-next=abstract-method
class Server(_Server):
    """Custom server for Celery beat."""

    def __init__(self):
        super().__init__(mode="celery", db_engine="sqlite")

    def run_celery_worker_as_subprocess(self):
        command = ["celery", f"--app={self.app_module}", "beat"]
        if self.log_level:
            command.append(f"--loglevel={self.log_level}")

            stdout, stderr = (None, None)  # Use defaults.
        else:
            stdout, stderr = (subprocess.DEVNULL, subprocess.DEVNULL)

        try:
            # pylint: disable-next=consider-using-with
            process = subprocess.Popen(command, stdout=stdout, stderr=stderr)

            atexit.register(process.terminate)

        except Exception as ex:  # pylint: disable=broad-exception-caught
            print(f"Error starting Celery beat: {ex}")


Server().run()
