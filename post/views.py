from django.views.generic import TemplateView
from .models import Post, Statistic


class HomeView(TemplateView):
    template_name = 'post/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.order_by("?").first()
        context['post'] = post

        last_seen_posts = Statistic.objects.order_by('update_at')[:5]
        context['last_seen_posts'] = last_seen_posts
        return context
