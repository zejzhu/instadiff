import json
import sys

def clean(json_file_path, marker):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified_lines = []

        # remove white space, identify lines with marker, remove marker
        for line in lines:
            stripped = line.strip()
            if stripped.startswith(marker):
                # Remove '"title": ' from the beginning
                modified_line = stripped.replace(marker, '', 1)
                modified_lines.append(modified_line + '\n')

        # sort usernames
        modified_lines.sort()
            
        
        with open(json_file_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        
        print(f"Successfully processed {json_file_path}")
    
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python clean.py <following file> <followers file>")
        sys.exit(1)
    
    clean(sys.argv[1], '"title": ')
    clean(sys.argv[2], '"value": ')

# TODO: add comparison step to python script, so long as it doesn't require package installs