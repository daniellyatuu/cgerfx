from django.views.generic import View
from django.shortcuts import render

class HomePageView(View):

    template_name = 'main/home_page.html'

    def get(self, request, *args, **kwargs):

        context = {}
        context['title'] = 'Cgerfx'
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
