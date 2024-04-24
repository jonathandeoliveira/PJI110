from django.contrib import admin
from biblioteca.models import Books
from biblioteca.models import Loans

# from biblioteca.models import Librarians
# from biblioteca.models import LoanLibrarians
# from biblioteca.models LoanResponsibles
# from biblioteca.models import Persons
# from biblioteca.models import Responsibles

admin.site.register(Books)
admin.site.register(Loans)
# admin.site.register(Librarians)
# admin.site.register(Persons)
# admin.site.register(Responsibles)
# admin.site.register(LoanLibrarians)
# admin.site.register(LoanResponsibles)
