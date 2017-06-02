# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta

from django.db import models


# Recurrent cards are cards that have to be created
class RecurrentCard(models.Model):
    class Meta:
        verbose_name = "recurrent card"
        verbose_name_plural = "recurrent cards"

    POSITION_CHOICES = (
        ("top", "Top"),
        ("bottom", "Bottom")
    )
    creator = models.ForeignKey("members.Member", related_name="created_recurrent_cards", verbose_name=u"Created recurrent cards")
    board = models.ForeignKey("boards.Board", related_name="recurrent_cards", verbose_name=u"Recurrent cards")

    name = models.CharField(verbose_name="Recurrent card name", max_length=512)
    description = models.TextField(verbose_name=u"Description of the card", default="", blank=True)
    position = models.CharField(verbose_name=u"Position in the list", choices=POSITION_CHOICES,
                                default="top", max_length=8)

    estimated_time = models.DecimalField(
        verbose_name="Estimated spent time of this recurrent card",
        help_text="Estimated time that will be spent in this card",
        decimal_places=2, max_digits=10,
        default=None, null=True, blank=True
    )

    creation_list = models.ForeignKey("boards.List", related_name="recurrent_cards",
                                      verbose_name="Creation list for the recurrent cards")

    labels = models.ManyToManyField("boards.Label", related_name="recurrent_cards", blank=True)
    members = models.ManyToManyField("members.Member", verbose_name=u"Members", related_name="recurrent_cards", blank=True)
    is_active = models.BooleanField(
        verbose_name="Should its child cards be created?",
        help_text="If unchecked, no cards will be created that depends on this recurrent card",
        default=False
    )

    def full_name(self):
        return "{0} of {1}".format(self.name, self.board.name)


# Recurrent cards are cards that have to be created
class WeeklyRecurrentCard(RecurrentCard):
    create_on_mondays = models.BooleanField(verbose_name="Create card on mondays", default=False)
    create_on_tuesdays = models.BooleanField(verbose_name="Create card on tuesdays", default=False)
    create_on_wednesdays = models.BooleanField(verbose_name="Create card on wednesdays", default=False)
    create_on_thursdays = models.BooleanField(verbose_name="Create card on thursdays", default=False)
    create_on_fridays = models.BooleanField(verbose_name="Create card on fridays", default=False)
    create_on_saturdays = models.BooleanField(verbose_name="Create card on saturdays", default=False)
    create_on_sundays = models.BooleanField(verbose_name="Create card on sundays", default=False)

    move_to_list_when_day_ends = models.ForeignKey(
        "boards.List",
        verbose_name="Automatically move the card to this list when the day ends",
        related_name="moved_recurrent_cards", default=None, null=True, blank=True
    )


