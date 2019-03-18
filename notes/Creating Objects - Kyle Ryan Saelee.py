class book(object):
    def __init__(self, author, title, price, illustrator, hardcover, current_page=0):
        self.author = author
        self.title = title
        self.price = price
        self.illustrator = illustrator
        self.hardcover = True
        self.current_page = current_page

    def next_page(self):
        self.current_page += 1
        print("You're currently on page %s" % self.current_page)

    def back_page(self):
        self.current_page -= 1
        print("You're currently on page %s" % self.current_page)

    def booktype(self):
        if self.hardcover:
            print("Your book type is a hardcover.")
        else:
            print("Your book type is paperback")




