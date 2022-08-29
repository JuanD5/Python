from utils.file_operations import save_to_file, read_file


save_to_file("data.txt", "Juan")

if __name__ == "__main__":
    print(read_file("data.txt"))