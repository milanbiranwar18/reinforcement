# Create a class to handle paginated content in a website.
# A pagination is used to divide long lists of content in a series of pages.
#
# Example:
# The pagination class will accept 2 parameters:
#     1.items (default: []): A list of contents to paginate.
#     2. pageSize (default: 10): The amount of items to show in each page.
#
# So for example we could initialize our pagination like this:
# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
#
#     p = Pagination(alphabetList, 4)
#
# And then use the method getVisibleItems to show the contents of the paginated list.
#
#     p.getVisibleItems() # ["a", "b", "c", "d"]
#
# You will have to implement various methods to go through the pages such as:
#
#     prevPage(), nextPage(), firstPage(), lastPage(), goToPage()
#
# Here's a continuation of the example above using nextPage and lastPage:
#
#     p.getVisibleItems()
#     # ["a", "b", "c", "d"]
#
#     p.nextPage()
#
#     p.getVisibleItems()
#     # ["e", "f", "g", "h"]
#
#     p.lastPage()
#
#     p.getVisibleItems()
#     # ["y", "z"]
#


class Pagination:
    def __init__(self, item, page_size=10):
        self.item = item
        self.page_size = page_size
        self.current_page = 1

    def get_visible_items(self):
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.item[start:end]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1

    def next_page(self):
        if self.current_page < self.num_pages():
            self.current_page += 1

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.num_pages()

    def go_to_page(self, page):
        if (page >= 1) and (page <= self.num_pages()):
            self.current_page = page

    def num_pages(self):
        return (len(self.item) + self.page_size - 1) // self.page_size


if __name__ == '__main__':
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)
    print(p.get_visible_items())

    p.next_page()
    print(p.get_visible_items())

    p.prev_page()
    print(p.get_visible_items())

    p.first_page()
    print(p.get_visible_items())

    p.go_to_page(4)
    print(p.get_visible_items())

    print()
    print(p.num_pages())

