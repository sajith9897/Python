
import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

if not os.path.isdir(downloads_path):
    print("Downloads folder not found!")

else:
    moved_count = 0

    for filename in os.listdir(downloads_path):

        file_path = os.path.join(downloads_path, filename)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        # Find the correct category
        category = "Others"

        for folder, extensions in file_types.items():
            if extension in extensions:
                category = folder
                break

        folder_path = os.path.join(downloads_path, category)
        os.makedirs(folder_path, exist_ok=True)

        destination = os.path.join(folder_path, filename)

        if os.path.exists(destination):
            print(f"Skipped duplicate file: {filename}")
            continue

        try:
            shutil.move(file_path, destination)
            print(f"Moved {filename} -> {category}")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {filename}: {error}")

    print(f"\nOrganization completed! Files moved: {moved_count}")
