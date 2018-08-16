from tkinter.filedialog import askopenfilename
import hashlib
import pathlib

filename = askopenfilename()

pathlib.Path('C:\\Outputs').mkdir(parents=True, exist_ok=True)

sha256_hash = hashlib.sha256()

with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    output = sha256_hash.hexdigest()
    print(output)
    save_file = open ("C:\\Outputs\\Hash_Output.txt", "w")
    save_file.write(output)
    save_file.close()
