from django.forms import CharField, Form, Textarea


class CommentForm(Form):
    content = CharField(widget=Textarea(attrs={'rows': 5, 'cols': 50}))