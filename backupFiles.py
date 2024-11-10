import os

def copy_files(source, destination):
    if not os.path.exists(source):
        print("Użytkownik nie wskazał folderu źródłowego")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    for root, dirs, files in os.walk(source):
        for file in files:
            src = os.path.join(root, file)

            relative_path = os.path.relpath(root, source)
            destination_path = os.path.join(destination, relative_path)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            with open(src, 'rb') as src_file:
                with open(os.path.join(destination_path, file), 'wb') as dest_file:
                    dest_file.write(src_file.read())
            
            print(f"Skopiowano: {src} -> {os.path.join(destination_path, file)}")

    print("Kopiowanie zakończone!")

# Przykład
source_folder = "H:\\test\\a"
destination_folder = "H:\\test\\b"

copy_files(source_folder, destination_folder)
