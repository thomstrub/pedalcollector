from django.db import models
from django.urls import reverse

GUITARS = (
    ('L', 'Gibson Les Paul'),
    ('T', 'Fender Telecaster'),
    ('S', 'Fender Stratocaster'),
    ('R', 'Rickenbacker')
)

AMPS = (
    ('M', 'Marshall JCM800'),
    ('F', 'Fender Twin'),
    ('V', 'Vox AC-30'),
    ('O', 'Orange AD30')
)

# Create your models here.
class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    # add absolute url instead of creating a success url in PedalClass view 
    def get_absolute_url(self):
        return reverse('pedals_detail', kwargs={'pk': self.id})

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    pedals = models.ManyToManyField(Pedal, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'board_id': self.id})

    

class Session(models.Model):
    date = models.DateField('session date')
    guitar = models.CharField(
        max_length=1,
        choices=GUITARS,
        default=GUITARS[0][1]
    )
    amp = models.CharField(
        max_length=1,
        choices=AMPS,
        default=AMPS[0][1]
    )
    notes = models.TextField(max_length=250)

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_guitar_display()} on {self.get_amp_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
