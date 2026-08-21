file = input("File name: ").casefold().lstrip().rstrip()

if file.endswith(".gif") or file.endswith(".GIF"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG"):
    print("image/jpeg")
elif file.endswith(".png") or file.endswith(".PNG"):
    print("image/png")
elif file.endswith(".pdf") or file.endswith(".PDF"):
    print("application/pdf")
elif file.endswith(".txt") or file.endswith(".TXT"):
    print("text/plain")
elif file.endswith(".zip") or file.endswith(".ZIP"):
    print("application/zip")
else:
    print("application/octet-stream")
