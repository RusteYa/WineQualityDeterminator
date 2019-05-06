from django import forms


class WinePropertiesForm(forms.Form):
    fixed_acidity = forms.DecimalField(label="Фиксированная кислотность", min_value=0, max_value=100)
    volatile_acidity = forms.DecimalField(label="Летучая кислотность", min_value=0, max_value=100)
    residual_sugar = forms.DecimalField(label="Остаточные сахара", min_value=0, max_value=100)
    chlorides = forms.DecimalField(label="Хлориды", min_value=0, max_value=100)
    total_sulfur_dioxide = forms.DecimalField(label="Общие диоксиды серы", min_value=0, max_value=100)
    sulphates = forms.DecimalField(label="Сульфаты", min_value=0, max_value=100)
    alcohol = forms.DecimalField(label="Содержание алкоголя", min_value=0, max_value=100)