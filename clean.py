import sys

def clean(json_file_path, marker, sorted_file_name):
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
            
        
        with open(sorted_file_name, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        
        print(f"Successfully cleaned {json_file_path}")
    
    except Exception as e:
        print(f"Error cleaning file: {e}")

def compare(following, followers):
    try:
        with open(following, 'r', encoding='utf-8') as ing:
            inglines = ing.readlines()
        with open(followers, 'r', encoding='utf-8') as ers:
            erslines = ers.readlines()

        diff = []
        ersindex = 0
        ingindex = 0

        while ingindex < len(inglines):
             # if ran out of ers, add all inglines
            if ersindex == len(erslines):
                diff.append(inglines[ingindex])
                ingindex += 1
            # this ing does not exist in ers
            elif inglines[ingindex] < erslines[ersindex]:
                diff.append(inglines[ingindex])
                ingindex += 1
            # catch ers up to ing
            elif inglines[ingindex] > erslines[ersindex]:
                ersindex += 1
            # they are equal
            else:
                ersindex += 1
                ingindex += 1
        

        with open('diff.json', 'w', encoding='utf-8') as f:
            f.writelines(diff)
        
        print("Successfully wrote difference to diff.json")



    except Exception as e:
        print(f"Error comparing files: {e}")
        

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python clean.py <following file> <followers file>")
        sys.exit(1)

    sorteding = "sorteding.json"
    sorteders = "sorteders.json"

    clean(sys.argv[1], '"title": ', sorteding)
    clean(sys.argv[2], '"value": ', sorteders)
    print(f"Finding usernames in {sys.argv[1]} not in {sys.argv[2]}...")
    compare(sorteding, sorteders)
