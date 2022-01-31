from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
COLORS = [
    ('r', 'red'),
    ('g', 'green'),
    ('b', 'blue')
]


class note(models.Model):
    title = models.CharField(_("title"), max_length=50)
    text = models.TextField(_("text"))
    createdDate = models.DateTimeField(_("created date"),  auto_now_add=True)
    noteColor = models.CharField(
        _("note color"), max_length=10, choices=COLORS)
    isArchived = models.BooleanField(_("is archived"))

    class Meta:
        verbose_name = _("note")
        verbose_name_plural = _("notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.createdDate is not None:
            self.createdDate = timezone.now()
            print(self.createdDate)
        super(note, self).save(*args, **kwargs)
