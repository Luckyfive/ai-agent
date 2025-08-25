import os
import subprocess
from typing import List

def run_python_file(working_directory: str, file_path: str, args: List[str] = []):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_target_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_target_path):
            return f'Error: File "{file_path}" not found.'

        if not abs_target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        cmd = ["python", abs_target_path, *args]
        try:
            completed = subprocess.run(
                cmd,
                cwd=abs_working_dir,
                capture_output=True,
                text=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            return "Error: executing Python file: process timed out after 30 seconds"
        except Exception as e:
            return f"Error: executing Python file: {e}"

        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
        parts = []
        if stdout.strip():
            parts.append(f"STDOUT:\n{stdout}".rstrip())
        if stderr.strip():
            parts.append(f"STDERR:\n{stderr}".rstrip())
        if completed.returncode != 0:
            parts.append(f"Process exited with code {completed.returncode}")
        if not parts:
            return "No output produced."
        return "\n".join(parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"
