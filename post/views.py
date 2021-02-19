from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Statistic


class HomeView(TemplateView):
    template_name = 'post/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.order_by("?").first()
        context['post'] = post

        last_seen_posts = Statistic.objects.order_by('updated_at')[:5]
        context['last_seen_posts'] = last_seen_posts
        return context


class AddToStatisticsAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        post_id = request.data.get('post_id')
        obj, created = Statistic.objects.get_or_create(post_id=post_id)
        obj.used_times += 1
        obj.save()
        
        if created:
            return Response({
                'message': 'Post added to statistics'
            })
        else:
            return Response({
                'message': "Post's statistics updated"
            })