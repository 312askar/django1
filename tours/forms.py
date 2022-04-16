from django import forms
from .models import TourBooking, RegulatTour

class TourBookingForm(forms.ModelForm):
    regular_tour = forms.ModelChoiceField(
        queryset=RegulatTour.objects.filter(status=RegulatTour.TOUR_STATUS_WAITING),
        widget=forms.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = TourBooking
        fields = ['regular_tour', 'place_count', 'mobile', 'notice']
        widgets = {
            'place_count': forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'mobile':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'notice':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }


