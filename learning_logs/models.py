from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """ Devolve uma representação em string do modelo. """
        return self.text
    
class Notes(models.Model):
    """ Algo especifico aprendido sobre um assunto (notas) """
    note = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """ Devolve uma representação em string do modelo. """
        return self.text[:50] + '...'
    
    class Meta:
        verbose_name_plural = 'entries' # caso o nome da classe fosse entry, ele subtituiria por entries, no caso coloquei Notes, então ele pega o plural de Notes como se fosse "entries".