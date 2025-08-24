import os

def get_files_info(working_directory, directory="."):
    """
    List the contents of a directory with file size and type information.
    
    Args:
        working_directory (str): The base directory that limits where we can access
        directory (str): Relative path within working_directory to list
        
    Returns:
        str: Formatted string with directory contents or error message
    """
    try:
        # Create the full path by joining working_directory and directory
        full_path = os.path.join(working_directory, directory)
        
        # Get absolute paths for security validation
        # Make working_directory relative to current working directory
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(full_path)
        
        # Security check: ensure target directory is within working directory
        # Normalize paths to handle .. and . properly
        abs_working_dir = os.path.normpath(abs_working_dir)
        abs_target_dir = os.path.normpath(abs_target_dir)
        
        if not abs_target_dir.startswith(abs_working_dir + os.sep) and abs_target_dir != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if the path exists and is a directory
        if not os.path.exists(abs_target_dir):
            return f'Error: "{directory}" does not exist'
        
        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'
        
        # List directory contents
        contents = os.listdir(abs_target_dir)
        
        # Build the result string
        result_lines = []
        for item in sorted(contents):  # Sort for consistent output
            item_path = os.path.join(abs_target_dir, item)
            
            # Get file size
            try:
                file_size = os.path.getsize(item_path)
            except OSError:
                file_size = 0  # If we can't get size, default to 0
            
            # Check if it's a directory
            is_directory = os.path.isdir(item_path)
            
            # Format the line
            line = f" - {item}: file_size={file_size} bytes, is_dir={is_directory}"
            result_lines.append(line)
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: {str(e)}"