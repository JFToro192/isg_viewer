from django.contrib import admin

from .models import (
                        ModelSeries,
                        ModelReference,
                        Author,
                        Responsible,
                        GeoidType,
                        GeoidMethod,
                        GeoidLicence,
                        GeoidStatus,
                        Geoid
                    )

admin.site.register([
                        ModelSeries,
                        ModelReference,
                        Author,
                        Responsible,
                        GeoidType,
                        GeoidMethod,
                        GeoidLicence,
                        GeoidStatus,
                        Geoid
                    ])