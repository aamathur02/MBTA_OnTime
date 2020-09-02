from django.db import models
from . import mbta_api

#list of all Commuter Rail Lines
lines_list = mbta_api.create_lines_list("https://api-v3.mbta.com")

#model to represent a lint
class Line(models.Model):
    #list of all MBTA commuter rail lines
    lines_list = mbta_api.create_lines_list("https://api-v3.mbta.com")
    name = models.CharField(max_length = 300, choices=lines_list)

    def __str__(self):
        return self.name

class Starting_Stop(models.Model):
    name = models.CharField(max_length=150)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    index = models.IntegerField(default=2)

    def __str__(self):
        return self.name

class Ending_Stop(models.Model):
    name = models.CharField(max_length=150)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    index = models.IntegerField(default=2)


    def __str__(self):
        return self.name
    

#model to represent a basic trip on the MBTA
class TripInput(models.Model):
    name = models.CharField(max_length=50, default='New Trip')
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    starting_stop = models.ForeignKey(Starting_Stop, on_delete=models.CASCADE)
    starting_time = models.TimeField()
    ending_stop = models.ForeignKey(Ending_Stop, on_delete=models.CASCADE)
    ending_time = models.TimeField()

    def __str__(self):
        return (f'from {starting_stop} to {ending_stop}')



