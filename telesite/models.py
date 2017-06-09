from django.db import models

#Категории затрат
class payment_category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_fullname = models.CharField(max_length=255)
    cat_createtime = models.DateTimeField(auto_now_add=True,auto_now=False)
    cat_updatetime = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.cat_name, )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Затраты
class payment(models.Model):
    pay_type = models.NullBooleanField(null=True,blank=True)
    pay_sum = models.FloatField()
    pay_category = models.ForeignKey(payment_category)
    pay_datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    pay_comment = models.CharField(max_length=200)

    def __str__(self):
        return "%s - %s" % (self.pay_sum, self.pay_comment, )

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

