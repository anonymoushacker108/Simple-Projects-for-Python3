import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# --- Normalize books so we always have lowercase fields ---
def normalize_book(b):
    if isinstance(b, dict):
        b['title'] = str(b.get('title', ''))
        b['author'] = str(b.get('author', ''))
        b['title_lower'] = b['title'].lower()
        b['author_lower'] = b['author'].lower()
        return b
    else:
        # object with attributes
        title = str(getattr(b, 'title', ''))
        author = str(getattr(b, 'author', ''))
        setattr(b, 'title_lower', title.lower())
        setattr(b, 'author_lower', author.lower())
        return b

bookshelf = [normalize_book(b) for b in bookshelf]

# (optional) show original order
for book in bookshelf:
    print(book['title'] if isinstance(book, dict) else getattr(book, 'title', ''))

def comparison_function(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

# Just for ASCII reference
print(ord("a"))  # 97
print(ord(" "))  # 32
print(ord("A"))  # 65

# --- Comparison: True if first title is "greater than" second (so swap) ---
def by_title_ascending(book_a, book_b):
    a_title = book_a['title_lower'] if isinstance(book_a, dict) else getattr(book_a, 'title_lower', '')
    b_title = book_b['title_lower'] if isinstance(book_b, dict) else getattr(book_b, 'title_lower', '')
    return a_title > b_title

# --- Call bubble_sort safely whether it returns the list or sorts in place ---
maybe_result = sorts.bubble_sort(bookshelf, comparison_function)
sorted_books = maybe_result if maybe_result is not None else bookshelf

# --- Print sorted result ---
for book in sorted_books:
    print(book['title'] if isinstance(book, dict) else getattr(book, 'title', ''))
