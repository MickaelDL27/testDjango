from django.contrib import admin
from .models import Post
from .models import Voetbalspeler

admin.site.register(Post)
admin.site.register(Voetbalspeler)
class VoetbalspelerAdmin(admin.ModelAdmin):
     list_display = ('naam', 'actuele_voetbalclub', 'auteur', 'datum_invoer', 'datum_laatste_aanpassing')
     search_fields = ('naam', 'actuele_voetbalclub', 'auteur')
     list_filter = ('datum_invoer', 'datum_laatste_aanpassing')