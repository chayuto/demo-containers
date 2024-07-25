from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    print("Received a POST request")

    # Collecting request metadata
    metadata = {
        "remote_addr": request.remote_addr,
        "method": request.method,
        "url": request.url,
        "base_url": request.base_url,
        "url_root": request.url_root,
        "headers": dict(request.headers),
        "form": request.form.to_dict(),
        "args": request.args.to_dict()
    }

    # Handling file uploads
    files = request.files
    file_contents = {}
    if files:
        for filename, file in files.items():
            print(f"Processing file: {filename}")
            file_content = file.read()
            file_length = len(file_content)
            file_contents[filename] = {
                "length": file_length,
                "content": file_content
            }
            file.seek(0)  # Reset file pointer for potential further operations
    else:
        print("No files found in the request")

    metadata["files"] = file_contents

    # Printing request metadata
    print("Request Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
        if key == "files":
            for fname, fdata in value.items():
                print(f"File: {fname}, Length: {fdata['length']}")
                print(f"Content: {fdata['content']}")

    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
