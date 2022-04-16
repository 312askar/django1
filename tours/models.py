from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
        (TOUR_STATUS_WAITING, 'Идет набор'),
        (TOUR_STATUS_START, 'Начался'),
        (TOUR_STATUS_COMPLETED, 'Завершен'),
        (TOUR_STATUS_REJECTED, 'Отменен'),
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
        return f"{self.tour.title} - {self.start.date()}"
        

class TourBooking(models.Model):
    STATUS_NEW = 'mew'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_FINISHED = 'finished'
    STATUS_REJECTED = 'rejected'
    BOOKING_STATUSES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_CONFIRMED, 'Подтвержден'),
        (STATUS_FINISHED, 'Завершен'),
        (STATUS_FINISHED, 'Отменен')
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    regular_tour = models.ForeignKey(RegulatTour, on_delete=models.DO_NOTHING)
    place_count = models.PositiveSmallIntegerField('Места')
    mobile = models.CharField('Номер телефона', max_length=10)
    statuses = models.CharField('Статус', max_length=9, choices=BOOKING_STATUSES, default=STATUS_NEW)
    is_paid = models.BooleanField('Оплачено', default=False)
    notice = models.CharField('Примечание', max_length=255, null=True, blank=True)
    created = models.DateTimeField('Создан', auto_now_add=True) #Создается только при создании
    updated = models.DateTimeField('Обновлен', auto_now=True)   #Меняется при каждом обновлении

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['-created']

    def __str__(self):
        return f'Бронь №: {self.id}'
