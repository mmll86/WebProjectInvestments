from django.db import models



# Уровни
class LevelRegister(models.Model):
	level = models.CharField(max_length=20, verbose_name='Уровни пайщиков')
	description = models.TextField(verbose_name='Описание')

	class Meta:
		verbose_name = 'Уровень'
		verbose_name_plural = 'Уровни'

	def __str__(self):
		return self.level



# Тарифы
class Rate(models.Model):
	rate = models.CharField(max_length=20, verbose_name='Тарифы')
	description = models.TextField(verbose_name='Описание')

	class Meta:
		verbose_name = 'Тариф'
		verbose_name_plural = 'Тарифы'

	def __str__(self):
		return self.rate



# Пайщики
class ShareholderRegister(models.Model):
	levelUser = models.ForeignKey('LevelRegister', verbose_name='Уровень',
	                              on_delete=models.CASCADE, max_length=250)
	lastname = models.CharField(max_length=30, verbose_name='Фамилия')
	name = models.CharField(max_length=30, verbose_name='Имя')
	patronymic =  models.CharField(max_length=30, verbose_name='Отчество')
	dateOfBirth = models.DateField(verbose_name='Дата рождения')
	rate = models.ForeignKey('Rate', verbose_name='Тариф', on_delete=models.CASCADE)
	uniqueNumber = models.IntegerField(verbose_name='Уникальный номер', db_index=True, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=100, verbose_name='Слаг', allow_unicode=True)
	following = models.ForeignKey('ShareholderRegister', verbose_name='Пригласитель',
	                              on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		verbose_name = 'Пайщика'
		verbose_name_plural = 'Пайщики'


	def __str__(self):
		return self.lastname
