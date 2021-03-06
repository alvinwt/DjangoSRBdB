from django.contrib import admin
from srb.models import Library, Interval, Sequencing_Run, Read_alignment, Genome_Build

class LibAdmin(admin.ModelAdmin):
    list_display = ('library_id',)
    # search_fields = ('library_id')

class IntAdmin(admin.ModelAdmin):
    list_display = ('IntervalSerialNumber','NeatName', 'chr','start','stop','IntervalSize','Link','Tags','Annotations')
    search_fields =('NeatName', 'IntervalSerialNumber','Tags','Annotations')

class AlignmentAdmin(admin.ModelAdmin):
    list_display=('chr','start','stop','sequence','read_counts','genomic_hits','strand','library_id')
    # ordering=('avg_counts')
#class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'publisher', 'publication_date')
#     list_filter = ('publication_date',)
#     date_hierarchy = ('publication_date')
#     ordering = ('-publication_date',)
#     # fields = ('title','authors','publisher',)
#     filter_horizontal = ('authors',)
#     raw_id_fields = ('publisher',)
    
admin.site.register(Library,LibAdmin)
admin.site.register(Genome_Build)
admin.site.register(Sequencing_Run)
admin.site.register(Read_alignment,AlignmentAdmin)
admin.site.register(Interval,IntAdmin)
#admin.site.register(Author, AuthorAdmin)
