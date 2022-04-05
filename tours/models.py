from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to='tours/')
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлен', auto_now=True)
    is_active = models.BooleanField('Активный', default=False)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ['-created']

    def __str__(self):
        return self.title


class RegulatTour(models.Model):
    TOUR_STATUS_WAITING = 'waiting'
    TOUR_STATUS_START = 'start'
    TOUR_STATUS_COMPLETED = 'completed'
    TOUR_STATUS_REJECTED = 'rejected'
    TOUR_STATUSES = (
        ('Идет набор', TOUR_STATUS_WAITING),
        ('Начался', TOUR_STATUS_START),
        ('Завершен', TOUR_STATUS_COMPLETED),
        ('Отменен', TOUR_STATUS_REJECTED),
    )
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start = models.DateTimeField('Начало')
    end = models.DateTimeField('Конец')
    places_count = models.PositiveSmallIntegerField('Количество ')
    status = models.CharField(
        'Статус',
        choices=TOUR_STATUSES,
        default=TOUR_STATUS_WAITING,
        max_length=10
    )

    class Meta:
        verbose_name = 'Регулярный тур'
        verbose_name_plural = 'Регулярные туры'
        ordering = ['-start']

        def __str__(self):
            return f"{self.tour.title - self.start}"
        

