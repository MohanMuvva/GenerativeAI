def read_file_in_chunks(file_path, chunk_size):
    try:
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:  # If chunk is empty, we have reached the end of the file
                    break
                print(f"Chunk:\n{chunk}\n")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the file path directly in the code
file_path = "C:/Users/ASUS/Documents/sample_text.txt"  # Adjust this to your actual file path
chunk_size = 100  # You can adjust this value as needed

# Call the function to read and chunk the file
read_file_in_chunks(file_path, chunk_size)
