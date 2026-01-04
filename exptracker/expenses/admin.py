from django.contrib import admin

# Register your models here.
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'amount', 'date')
    list_filter = ('category', 'date')
    search_fields = ('description', 'category')
    ordering = ('-date',)