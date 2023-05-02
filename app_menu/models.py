from django.db import models

class Menu(models.Model):
    # Поле с названием меню
    objects = None
    title = models.CharField(max_length=50, default='main_menu')
    # Поле с названием элемента меню
    name = models.CharField(max_length=50)
    # Поле с ссылкой элемента меню
    url = models.CharField(max_length=200)
    # Поле, связывающее элемент меню с его родительским элементом
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
