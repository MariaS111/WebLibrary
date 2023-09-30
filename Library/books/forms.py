from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import CharField, Form, Textarea, IntegerField, NumberInput
from books.models import BookRating, Comment


class CommentForm(Form):
    content = CharField(widget=Textarea(attrs={'rows': 5, 'cols': 50, 'maxlength': '200'}))

    class Meta:
        model = Comment
        fields = ['content']


class RateForm(Form):
    rating = IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 10}),
                          validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        model = BookRating
        fields = ['rating']
