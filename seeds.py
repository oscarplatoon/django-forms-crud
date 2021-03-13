from books.models import Book

# to run this file, enter in: "python manage.py shell < seeds.py" into your console

b1 = Book(title="Green Eggs And Ham", pages=72)
b1.save()

b2 = Book(title="Twilight", pages=498)
b2.save()

b3 = Book(title="Where The Sidewalk Ends", pages=309)
b3.save()