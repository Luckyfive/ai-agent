import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_target_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure parent directory exists
        parent_dir = os.path.dirname(abs_target_path)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except Exception as e:
                return f"Error: {str(e)}"

        try:
            with open(abs_target_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            return f"Error: {str(e)}"

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
