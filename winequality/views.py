from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View

from winequality.forms import WinePropertiesForm
from winequality.wine_quality_determinator import WineQualityDeterminator


class HomeView(TemplateView):
    template_name = 'winequality/home.html'


class WineQualityDeterminateView(FormView):
    template_name = 'winequality/determinate.html'
    form_class = WinePropertiesForm
    success_url = reverse_lazy('result')

    def form_valid(self, form):
        properties = [[form.cleaned_data['fixed_acidity'],
                       form.cleaned_data['volatile_acidity'],
                       form.cleaned_data['residual_sugar'],
                       form.cleaned_data['chlorides'],
                       form.cleaned_data['total_sulfur_dioxide'],
                       form.cleaned_data['sulphates'],
                       form.cleaned_data['alcohol'],
                       ]]
        quality = WineQualityDeterminator.determinate(properties)
        self.request.session['quality'] = quality
        return super().form_valid(form)


class WineQualityView(View):
    template_name = 'winequality/result.html'

    def get(self, request):
        quality = self.request.session['quality']
        result = ''
        if quality == '0':
            result = 'Наши соболезнования. Вам не повезло, вам попалось низкокачественное вино.'
        elif quality == '1':
            result = 'Вам попалось вино среднего качество, оно в целом неплохое, но не более.'
        elif quality == '2':
            result = 'Наши поздравления. У вас вино прекрасного качества!'
        return render(request, self.template_name, {'result': result})