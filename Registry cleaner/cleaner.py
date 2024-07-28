import os
import shutil
import winreg

def clean_temp_files():
    temp_folders = [os.environ.get('TEMP'), os.environ.get('TMP')]
    
    for folder in temp_folders:
        if folder:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    try:
                        file_path = os.path.join(root, dirs, file)
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file}: {e}")

def clean_registry():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU", 0, winreg.KEY_ALL_ACCESS)
        num_values = winreg.QueryInfoKey(registry_key)[1]
        
        for i in range(num_values):
            value_name = winreg.EnumValue(registry_key, i)[0]
            winreg.DeleteValue(registry_key, value_name)
            print(f"Deleted: {value_name}")
            
        winreg.CloseKey(registry_key)
    except Exception as e:
        print(f"Error cleaning registry: {e}")

def clean_browser_cache(browser):
    if browser == "chrome":
        cache_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Cache")
    elif browser == "edge":
        cache_path = os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Edge", "User Data", "Default", "Cache")
    else:
        print("Unsupported browser.")
        return
    
    if os.path.exists(cache_path):
        for file in os.listdir(cache_path):
            file_path = os.path.join(cache_path, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")
    else:
        print("Cache path not found.")

def main():
    print("Starting cleaning process...")
    clean_temp_files()
    clean_registry()
    clean_browser_cache("chrome")
    clean_browser_cache("edge")
    print("Cleaning process completed.")

if __name__ == "__main__":
    main()
