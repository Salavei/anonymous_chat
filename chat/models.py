from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )
    external_id = models.TextField(
        verbose_name='ID пользователя в соц сети',
        default="",
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'User: {self.external_id} Send: {self.text} '

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'