from django.contrib import admin

from .models import Books
from .models import Loans
from .models import Persons
from .models import Responsibles
from .models import Librarians
from .models import LoanLibrarians
from .models import LoanResponsibles


admin.site.register(Books)
admin.site.register(Loans)
admin.site.register(Librarians)
admin.site.register(Persons)
admin.site.register(Responsibles)
admin.site.register(LoanLibrarians)
admin.site.register(LoanResponsibles)
