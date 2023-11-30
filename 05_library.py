def check_book_limits(book_type, membership_level):
    book_limits = {
        'fiction': {
            'standard': 3,
            'premium': 5,
        },
        'non-fiction': {
            'standard': 4,
            'premium': 6,
        },
        'reference': {
            'standard': 2,
            'premium': 4
        }
    }
    
    if book_type in book_limits:
        if membership_level == 'standard':
            return book_limits[book_type][membership_level]
        elif membership_level == 'premium':
            return book_limits[book_type][membership_level]
        else:
            return "Invalid membership level"
    else:
        return "Invalid book type"

# Example usage
max_books_allowed = check_book_limits('fiction', 'premium')
print("Maximum books allowed:", max_books_allowed)
