# contacts/pagination.py
from rest_framework.pagination import PageNumberPagination

class ContactPagination(PageNumberPagination):
    page_size = 5            # Number of contacts per page
    page_size_query_param = 'page_size'  # Allow client to set page_size in query params
    max_page_size = 50       # Max number of contacts per page
