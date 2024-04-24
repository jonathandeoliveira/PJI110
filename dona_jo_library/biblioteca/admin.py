from django.contrib import admin

from biblioteca.models import Books
from biblioteca.models import Loans
from biblioteca.models import Status
from biblioteca.models import Genres

# from biblioteca.models import Librarians
# from biblioteca.models import LoanLibrarians
# from biblioteca.models LoanResponsibles
# from biblioteca.models import Persons
# from biblioteca.models import Responsibles

admin.site.register(Books)
admin.site.register(Loans)
admin.site.register(Status)
admin.site.register(Genres)
