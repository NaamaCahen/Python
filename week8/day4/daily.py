class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self._current_page = 1
        length=len(self.items)
        self.__total_pages = int(length / page_size) if length % page_size == 0 else int(length / page_size)+1

    def get_visible_items(self):
        current_index = (self._current_page - 1) * self.page_size
        print(self.items[current_index:current_index + self.page_size])

    def next_page(self):
        self._current_page += 1
        return self

    def prev_page(self):
        self._current_page -= 1
        return self

    def first_page(self):
        self._current_page = 1
        return self

    def last_page(self):
        self._current_page = self.__total_pages
        return self

    def go_to_page(self, page_num):
        if 0 < page_num < self.__total_pages:
            self._current_page = page_num
        elif page_num <= 0:  # go to the first page
            self._current_page = 1
        else:  # go to the last page
            self._current_page = self.__total_pages
        return self


alphabetList = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

p = Pagination(alphabetList, 4)
p.get_visible_items()
p.next_page()
p.get_visible_items()
p.next_page().next_page().get_visible_items()
p.last_page().get_visible_items()
p.prev_page().get_visible_items()
p.go_to_page(10)
p.go_to_page(0)
p.get_visible_items()
