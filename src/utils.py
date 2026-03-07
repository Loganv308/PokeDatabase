from pathlib import Path

class utils:
    def has_Files(dirPath: str):
        p = Path(dirPath)
        
        if not p.is_dir():
            print(f"Error: {dirPath} is not a valid directory or does not exist.")
            return False
        else:
            return any(entry.is_file() for entry in p.iterdir())