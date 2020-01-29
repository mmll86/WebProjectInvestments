from django.db import models


LEVEL = 1

# Тарифы
class Rate(models.Model):
	rate = models.CharField(max_length=20, verbose_name='Тарифы')
	level = models.IntegerField(verbose_name='Уровень')
	sumRate = models.FloatField(verbose_name='Первоначальный взнос')
	interest = models.FloatField(verbose_name='Проценты')

	class Meta:
		verbose_name = 'Тариф'
		verbose_name_plural = 'Тарифы'

	def __str__(self):
		return self.rate


# Пайщики
class ShareholderRegister(models.Model):
	lastname = models.CharField(max_length=30, verbose_name='Фамилия')
	name = models.CharField(max_length=30, verbose_name='Имя')
	patronymic = models.CharField(max_length=30, verbose_name='Отчество')
	dateOfBirth = models.DateField(verbose_name='Дата рождения')
	phone = models.CharField(max_length=10, verbose_name='Телефон', null=True)

	rate = models.ForeignKey('Rate', verbose_name='Тариф', on_delete=models.CASCADE)
	level = models.IntegerField(verbose_name='Level', blank=True, null=True)
	uniqueNumber = models.IntegerField(verbose_name='Уникальный номер', db_index=True, unique=True)

	sumInveted = models.FloatField(verbose_name='Сумма тарифа', blank=True, null=True)
	sumRevenue = models.FloatField(verbose_name='Доход', blank=True, null=True, default=0)
	interest = models.FloatField(verbose_name='Проценты', blank=True, null=True)

	invitee = models.ForeignKey('ShareholderRegister', verbose_name='Пригласитель',
	                              on_delete=models.CASCADE, related_name='+',  blank=True, null=True)
	invited = models.ForeignKey('ShareholderRegister', verbose_name='Приглашенный',
	                              on_delete=models.CASCADE, related_name='+', blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=100, verbose_name='Слаг', allow_unicode=True)

	checkUpdate = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Пайщика'
		verbose_name_plural = 'Пайщики'

	def save(self, *args, **kwargs):
		if self.rate is not None:
			rates = Rate.objects.get(rate=self.rate)
			self.sumInveted = rates.sumRate
			self.interest = rates.interest

		if self.invitee is None:
			self.level = LEVEL
		else:
			test = ShareholderRegister.objects.get(slug__iexact=self.invitee)
			self.level = test.level + LEVEL

			# Сервис вознагр
			# if self.checkUpdate is False:
			# 	self.checkUpdate = True
			# 	test.sumRevenue += test.sumInveted
			# 	test.save()

			if self.level > 5:
				self.level = 5
		super(ShareholderRegister, self).save(*args, **kwargs)

	def __str__(self):
		return self.slug


