
import socket


# ==================================
# 1. SERVER CONFIGURATION
# ==================================

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8000))

server.listen()

print("Server is listening on 127.0.0.1:8000")


# ==================================
# 2. FRONTEND DIRECTORY
# ==================================

frontend_folder = r"C:\Users\Den\Documents\Python Project\frontend"


# ==================================
# 3. URL ROUTING
# ==================================

routes = {
    "/": ("index.html", "text/html; charset=utf-8"),

    "/landing-page.js": (
        "landing-page.js",
        "text/javascript; charset=utf-8"
    ),

    "/yield.png": (
        "yield.png",
        "image/png"
    )
}


# ==================================
# 4. SERVER LOOP
# ==================================

while True:

    connection, address = server.accept()

    print("\nConnected client:", address)

    data = connection.recv(1024)

    if not data:
        connection.close()
        continue

    request = data.decode("utf-8")

    print(request)

    request_line = request.splitlines()[0]

    method, path, version = request_line.split(" ")

    print("Method:", method)
    print("Path:", path)
    print("Version:", version)


    # ==================================
    # 5. PROCESS REQUEST
    # ==================================

    if method == "GET" and path in routes:

        filename, content_type = routes[path]

        file_path = frontend_folder + "\\" + filename

        with open(file_path, "rb") as file:
            body = file.read()

        status = "200 OK"

    else:

        body = b"404 - Page Not Found"

        content_type = "text/plain; charset=utf-8"

        status = "404 Not Found"


    # ==================================
    # 6. BUILD HTTP RESPONSE
    # ==================================

    headers = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
    ).encode("utf-8")

    response = headers + body


    # ==================================
    # 7. SEND RESPONSE
    # ==================================

    connection.sendall(response)


    # ==================================
    # 8. CLOSE CLIENT CONNECTION
    # ==================================

    connection.close()
