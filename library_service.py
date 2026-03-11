from xmlrpc.server import SimpleXMLRPCServer

books = {
    121: {"name": "Harry Potter", "status": "Available"},
    122: {"name": "The Alchemist", "status": "Issued"},
    123: {"name": "Wings of Fire", "status": "Available"},
    124: {"name": "Rich Dad Poor Dad", "status": "Issued"},
    125: {"name": "The Lord of the Rings", "status": "Issued"},
    126: {"name": "The Little Prince", "status": "Available"},
    127: {"name": "Paper Things", "status": "Available"}
}

def check_book(book_id):
    book_id = int(book_id)
    if book_id in books:
        book = books[book_id]
        return f"Book Name: {book['name']}, Status: {book['status']}"
    return "Book not available in library"

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(check_book, "check_book")

print("Library Service running on port 8000...")
server.serve_forever()
