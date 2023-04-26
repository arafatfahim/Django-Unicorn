from django.urls import include, path
from django.contrib import admin
from movies.views import MovieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path('', MovieView.as_view()),
]
