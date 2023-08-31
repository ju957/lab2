class Author:
    def __init__(self, name, booklist): # Creates 2 variables, the author's name and what books the author has published
                                        # booklist is intended to be a list.
        self.name = name
        self.booklist = booklist

    def __str__(self):
        list = '' # Creates an empty string to add books from booklist to, to remove the [].
        for x in range(len(self.booklist)): # Changes booklist to an integer than be used in a for loop
            list += self.booklist[x] + ', ' ## Appends the books one by one into a string
        return f'{self.name} has published: {list}' # Formats a new string to include the author who published them.

    def publish(self, bookName): # publish method to add a new book to an Author object's booklist
        if bookName in self.booklist: # Checks if the book has already been published
            print("This author has already published a book by that name.") # If it has, prints an "error" message
        else:
            self.booklist.append(bookName) # If it hasn't been, adds the new book at the end of the list.


def main():

    a1 = Author('Marvin Marx', ['Rock\'em', 'Sock\'em']) # Author example 1
    a2 = Author('Tess Tau Thor', ['Strange Phenomenon', 'Universal Stars', 'Deserts and Forests']) # Author example 2
    a3 = Author('Andy Nonymous', ['Disappearing and You', 'VPNs Explained']) #Author example 3

    authorList = {a1.name: a1, a2.name: a2, a3.name: a3} # Creates a dictionary of authors with their object so the user
                                                         # can search by name for the author they want to publish for.

    while input("Do you want a book published y/n? ").lower() == 'y':
        for x in authorList.keys(): # Loops for each key in the authorList dictionary
            print(authorList[x]) # Prints each author and their published books.
        name = input("What author do you want to publish for? ") # Asks the user which author list to append to.
        bookName = input("Please type the book you want to publish. ").title() # Formats the book title properly
                                                                        # and asks for a book name
        authorList[name].publish(bookName) # Runs the publish method under the author class

    print('\n') # Creates a gap from previous inputs and the new, final list of authors and their published books.
    for x in authorList.keys(): # Loops for each key in the authorList dictionary
        print(authorList[x]) # Creates a line for each author in the dictionary

main() # Runs the main method