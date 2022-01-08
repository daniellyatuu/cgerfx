from django.views.generic import View
from django.shortcuts import render

class HomePageView(View):

    template_name = 'main/home_page.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Cgerfx'
        return render(request, self.template_name, context)

class AboutUsView(View):

    template_name = 'main/about_us.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'About Cgerfx'
        return render(request, self.template_name, context)


class LearnMoreDerivView(View):

    template_name = 'main/learn_more_deriv.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Deriv'
        return render(request, self.template_name, context)


class LearnMoreXMView(View):

    template_name = 'main/learn_more_xm.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'XM'
        return render(request, self.template_name, context)


class BrokerListView(View):

    template_name = 'main/broker_list.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Brokers in Tanzania'
        return render(request, self.template_name, context)


class ForexDocumentsListView(View):

    template_name = 'main/forex_document_list.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Forex Books And PDF'
        return render(request, self.template_name, context)


class BlogPostListView(View):

    template_name = 'main/blog_post_list.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Blog Post'
        return render(request, self.template_name, context)


class TutorialVideoListView(View):

    template_name = 'main/video_list.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Tutorial Videos'
        return render(request, self.template_name, context)


class BeginnerGuideView(View):

    template_name = 'main/beginner_guide.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Beginner Guide'
        return render(request, self.template_name, context)
