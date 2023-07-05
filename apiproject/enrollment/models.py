from django.db import models

class FunnelStatus(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    status = models.ForeignKey(FunnelStatus, on_delete=models.CASCADE, default=None)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    status_before = models.ForeignKey(FunnelStatus, related_name="logs_before", on_delete=models.CASCADE)
    status_after = models.ForeignKey(FunnelStatus, related_name="logs_after", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.timestamp}"