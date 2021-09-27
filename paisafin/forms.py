from django.forms import ModelForm, widgets
from .models import All , Destination
class DestinationForm(ModelForm):
	class Meta:
		model = Destination
		fields=['username','header','url','description','money','moneyclick','moneyimpression','silver','silverclick','silverimpression']
		labels={
			'moneyclick':'Enter amount per click',
			'moneyimpression':'Enter amount per impression',
			'silverclick': 'Enter Silvers per click',
			'silverimpression': 'Enter silvers per impression',
		}
	def __init__(self,*args,**kwargs):
		super(DestinationForm,self).__init__(*args,**kwargs)
		self.fields['header'].required=True
		self.fields['money'].required=False
		self.fields['moneyclick'].required=False
		self.fields['moneyimpression'].required=False
		self.fields['silver'].required=False
		self.fields['silverclick'].required=False
		self.fields['silverimpression'].required=False
		
class AllForm(ModelForm):
	class Meta:
		model = All
		#fields='__all__'
		fields=['brandname','first_name','last_name','email','email2','number','number2','address','country','language','website','youtube','facebook','instagram','twitter','pinterest','type']
		labels={
			'brandname':'Brand Name',
		}
	def __init__(self,*args,**kwargs):
		super(AllForm,self).__init__(*args,**kwargs)
		#this is to show select in drop down instead of ----
		#self.fields['postions'].empty_label="Select"
		self.fields['email2'].required=False
		self.fields['number2'].required=False
		self.fields['website'].required=False
		self.fields['youtube'].required=False
		self.fields['facebook'].required=False
		self.fields['instagram'].required=False
		self.fields['twitter'].required=False
		self.fields['pinterest'].required=False
