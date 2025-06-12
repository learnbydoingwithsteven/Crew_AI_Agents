"""Script to remove null bytes from source files."""

import os
import sys

def fix_file(filepath):
    """Remove null bytes from a file."""
    try:
        # Read file content
        with open(filepath, 'rb') as file:
            content = file.read()
        
        # Check if file contains null bytes
        if b'\x00' in content:
            print(f"Fixing {filepath}")
            # Remove null bytes
            fixed_content = content.replace(b'\x00', b'')
            
            # Write back to file
            with open(filepath, 'wb') as file:
                file.write(fixed_content)
            
            return True
        
        return False
    except Exception as e:
        print(f"Error fixing {filepath}: {str(e)}")
        return False

def scan_directory(directory):
    """Scan directory for Python files with null bytes."""
    fixed_count = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    fixed_count += 1
    
    return fixed_count

if __name__ == "__main__":
    target_dir = "."
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    
    fixed_count = scan_directory(target_dir)
    print(f"Fixed {fixed_count} files with null bytes.")
