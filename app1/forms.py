from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'placeholder': ('Username')})
    self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})
    self.fields['password2'].widget.attrs.update(
      {'placeholder': ('Repeat password')})
