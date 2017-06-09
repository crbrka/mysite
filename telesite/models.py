from django.db import models

# Create your models here.

class payment(models.Model):
    pay_type = models.NullBooleanField(null=True,blank=True)
    pay_sum = models.FloatField()
    pay_datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    pay_comment = models.CharField(max_length=200)

    def __str__(self):
        return "%s - %s" % (self.pay_sum, self.pay_comment, )

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'



