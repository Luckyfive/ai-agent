import os
from .config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # Build absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target path stays within working directory
        if not abs_target_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Validate is a regular file
        if not os.path.isfile(abs_target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read with truncation
        try:
            with open(abs_target_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(MAX_CHARS + 1)
        except Exception as e:
            return f"Error: {str(e)}"

        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except Exception as e:
        return f"Error: {str(e)}"
