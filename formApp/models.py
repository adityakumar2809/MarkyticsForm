from django.db import models

# Create your models here.


class IncidentReport(models.Model):

    LOCATION_CHOICES = [(None, '---Select---'), ('Corporate Headoffice','Corporate Headoffice'), ('Regional Suboffice','Regional Suboffice'), ('Branch Office','Branch Office')]
    INITIAL_SEVERITY_CHOICES = [(None, '---Select---'), ('Mild','Mild'), ('Moderate','Moderate'), ('Extreme','Extreme')]

    location = models.CharField(max_length=255, choices=LOCATION_CHOICES)
    incident_description = models.TextField()
    date_of_incident = models.DateField()
    time_of_incident = models.TimeField()
    incident_location = models.TextField(blank=True, null=True)
    initial_severity = models.CharField(max_length=255, choices=INITIAL_SEVERITY_CHOICES)
    suspected_cause = models.TextField(blank=True, null=True)
    immediate_actions_taken = models.TextField(blank=True, null=True)
    sub_incident_environmental_incident = models.BooleanField(default=False)
    sub_incident_injury_illness = models.BooleanField(default=False)
    sub_incident_property_damage = models.BooleanField(default=False)
    sub_incident_vehicle = models.BooleanField(default=False)
    reported_by = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.location}-{self.date_of_incident}-{self.pk}'

    class meta():
        ordering = ['-pk']
