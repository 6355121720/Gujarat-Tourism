from django import forms

class signup(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    re_password=forms.CharField(max_length=20)

class login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)


CITY_CHOICES = [
    ('all','All Cities'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Vadodara', 'Vadodara'),
    ('Gandhinagar', 'Gandhinagar'),
    ('Kutch', 'Kutch'),
    ('Surat','Surat'),
    ('Dwarka','Dwarka'),
    ('Somnath','Somnath'),
    ('Junagadh','Junagadh'),
    ('Patan','Patan'),
    ('Gir Somnath','Gir Somnath'),
    ('Saputara','Saputara'),
    ('Dang','Dang'),
    ('Bhuj','Bhuj'),
    ('Navsari','Navsari'),
    ('Anand','Anand'),
    ('Panchmahal','Panchmahal'),
    ('Mehsana','Mehsana'),
    ('Dahod','Dahod'),
    ('Tapi','Tapi'),
    ('Valsad','Valsad'),
    ('Narmada','Narmada'),
    ('Kheda','Kheda'),
    ('Banaskantha','Banaskantha'),
    ('Rajkot','Rajkot'),
    ('Surendranagar','Surendranagar'),
    ('Bhavnagar','Bhavnagar'),
]

TYPE_CHOICES = [
    ('all','All'),
    ('Historical', 'Historical'),
    ('Cultural', 'Cultural'),
    ('Architectural', 'Architectural'),
    ('Nature', 'Nature'),
    ('Shopping', 'Shopping'),
    ('Entertainment', 'Entertainment'),
    ('Spiritual', 'Spiritual'),
    ('Adventure', 'Adventure'),
]

SEASON_CHOICES = [
    ('all', 'All Year'),
    ('Winter', 'Winter'),
    ('Summer', 'Summer'),
]

class recommend(forms.Form):
    city = forms.ChoiceField(choices=CITY_CHOICES, label="Select City")
    type = forms.ChoiceField(choices=TYPE_CHOICES, label="Select Type")
    season = forms.ChoiceField(choices=SEASON_CHOICES, label="Select Season")