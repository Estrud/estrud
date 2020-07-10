from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from estrud.base.views import signup, frontpage


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('admin/', admin.site.urls),
    path('app/', include('estrud.dashboard.urls')),
    path('vigas/', include('estrud.vigas.urls')),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
