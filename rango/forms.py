from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.Max_Length_title, help_text="Please enter category name.") 
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm (forms.ModelForm):
   

    title = forms.CharField(max_length=Page.Max_Length_title, help_text="Please enter the tile of the page.")
    url = forms.URLField(max_length=Page.Max_Length_url, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta :
        model=Page
        exclude = ('category',)


