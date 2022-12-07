from django import forms
from .models import Care, Review, Comment

CARING_ANIMAL = [ 
    ('고양이', '고양이'), 
    ('강아지', '강아지'),
    ]

CARING_TIME = [
    ('4시간이하', "4시간이하"),
    ("1일이하", "1일이하"),
    ("3일이하", "3일이하"),
    ("7일이하", "7일이하"),
    ("7일초과", "7일초과"),
]

ETC = [
    ('사전만남 가능', '사전만남가능'),
    ('반려동물 있음', '반려동물 있음'),
    ('노견/노묘 케어 가능', '노견/노묘 케어 가능'),
    ('픽업 가능', '픽업 가능'),
    ('산책 가능', '산책 가능'),
    ('돌봄 경력 있음', '돌봄 경력 있음'),
]

class Careform(forms.ModelForm):
    caring_animal = forms.MultipleChoiceField(
    choices=CARING_ANIMAL,
    widget=forms.CheckboxSelectMultiple()
    )

    caring_time = forms.MultipleChoiceField(
    choices=CARING_TIME,
    widget=forms.CheckboxSelectMultiple()
    )

    etc = forms.MultipleChoiceField(
    choices=ETC,
    widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Care
        fields = [
            "title",
            "area",
            "pet_gender",
            "content",
            "image",
            "caring_animal",
            "caring_time",
            "etc",
        ]
        labels = {
            "title": "제목",
            "area": "지역",
            "content": "내용",
            "image": "이미지",
            "pet_gender": "돌봐주실 분 성별",
        }
    
    # def save(self, commit=True):
    #     care = self.instance
    #     care_list = '/'.join([qs.care_list for qs in self.cleaned_data['caring_animal']])
    #     care.list = care_list
    #     care.save()
    #     print(care.title, care.content, care.caring_animal)
    #     return care


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
