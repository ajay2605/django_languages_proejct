

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paragidms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]
