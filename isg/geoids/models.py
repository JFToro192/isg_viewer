from typing import Any
from django.db import models

"""
MODEL SERIES
"""
class ModelSeries(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Model Series"
        
"""
MODEL GROUP
"""
class ModelGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Model Groups"

"""
MODEL REFERENCES RELATION
"""
class ModelReferenceRelation(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Model Reference Relations"

"""
MODEL REFERENCE
"""
class ModelReference(models.Model):
    refRelation = models.ForeignKey(ModelReferenceRelation, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    citation = models.CharField(max_length=200)
    doi = models.CharField(max_length=200)
    attachment_path = models.CharField(max_length=200)
    presentation_path = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Model References"

"""
PERSON MODEL
"""
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "{self.last_name}, {self.first_name} {self.second_name}"
    
    class Meta:
        verbose_name_plural = "Authors"

class Responsible(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "{self.last_name}, {self.first_name} {self.second_name}"
    
    class Meta:
        verbose_name_plural = "Responsibles"

"""
GEOID TYPE
"""
class GeoidType(models.Model): 
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Typologies"

"""
GEOID METHOD
"""
class GeoidMethod(models.Model): 
    method = models.CharField(max_length=200)

    def __str__(self):
        return self.method

    class Meta:
        verbose_name_plural = "Methods"

"""
GEOID LICENCE
"""
class GeoidLicence(models.Model):
    licence = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.licence
    
    class Meta:
        verbose_name_plural = "Licences"

"""
GEOID STATUS
"""
class GeoidStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Status"

"""
GEOID MODEL
"""
class Geoid(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    modelGroup = models.ForeignKey(ModelGroup, on_delete=models.CASCADE)
    description = models.TextField()
    comments = models.TextField()
    type = models.ForeignKey(GeoidType, on_delete=models.CASCADE)
    method = models.ForeignKey(GeoidMethod, on_delete=models.CASCADE)
    crs = models.IntegerField()
    continent = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    lat_min = models.FloatField()
    lat_max = models.FloatField()
    lon_min = models.FloatField()
    lon_max = models.FloatField()
    delta_lat = models.FloatField()
    delta_lon = models.FloatField()
    bbox = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    status = models.ForeignKey(GeoidStatus, on_delete=models.CASCADE)
    wos = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    licence = models.ForeignKey(GeoidLicence, on_delete=models.CASCADE)
    file_path_isg = models.CharField(max_length=200)
    file_path_converted = models.CharField(max_length=200)
    file_extension = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    wms_endpoint = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Model"