# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import debug_toolbar

urlpatterns = [
    # Health checks
    url(r'^status/', include('health_check.urls')),    

    # Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),

    # Admin interface
    path('admin/', admin.site.urls),

    path("", include("authentication.urls")),  # add this
    path("", include("app.urls"))  # add this
]
