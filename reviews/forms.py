from django import forms

from reviews.models import Review


# class  ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100 ,error_messages={
#         'required':'Please enter your name',
#         'max_length': 'please enter your name short'
#     })
#     review_text = forms.CharField(label="Your FeedBack", widget=forms.Textarea , max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Please enter your name",
                "max_length": "Is Too Short Or Long",
            }
        }
