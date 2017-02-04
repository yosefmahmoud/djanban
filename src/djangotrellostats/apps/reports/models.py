from __future__ import unicode_literals

from django.db import models


# Movements the cards suffer
class CardMovement(models.Model):

    class Meta:
        verbose_name = u"Card movement"
        verbose_name_plural = u"Card movements"
        index_together = (
            ("board", "card", "datetime"),
            ("board", "type", "source_list", "destination_list"),
            ("board", "destination_list", "datetime"),
        )

    CARD_MOVEMENT_TYPES = (
        ("forward", "Forward"),
        ("backward", "Backward"),
    )

    board = models.ForeignKey("boards.Board", verbose_name=u"Board", related_name="card_movements")

    card = models.ForeignKey("boards.Card", verbose_name=u"Card", related_name="movements")

    type = models.CharField(verbose_name="Movement type", choices=CARD_MOVEMENT_TYPES, max_length=32)

    source_list = models.ForeignKey("boards.List", verbose_name=u"Source list", related_name="source_lists", null=True)

    destination_list = models.ForeignKey("boards.List", verbose_name=u"Destination list",
                                         related_name="destination_lists")

    datetime = models.DateTimeField(verbose_name="Date and time this card has been moved")

    member = models.ForeignKey("members.Member", verbose_name=u"Member", related_name="card_movements",
                               null=True, default=None)

    def __unicode__(self):
        return "{0} -> {1} (on {2})".format(self.source_list.name, self.destination_list.name, self.datetime)


# Reviews of a card
class CardReview(models.Model):
    board = models.ForeignKey("boards.Board", verbose_name=u"Board", related_name="card_reviews")
    card = models.ForeignKey("boards.Card", verbose_name=u"Card", related_name="reviews")
    description = models.TextField(verbose_name=u"Description of the review", default="", blank=True)
    reviewers = models.ManyToManyField("members.Member", verbose_name=u"Members", related_name="card_reviews")
    creation_datetime = models.DateTimeField(verbose_name="Date and time this card has been reviewed")

    @staticmethod
    def create(card_comment, reviewers, description=""):
        # Create the card review
        card = card_comment.card
        board = card.board
        card_review = CardReview(
            card=card, board=board, description=description,
            creation_datetime=card_comment.creation_datetime
        )
        card_review.save()

        # Assign the reviewers
        for reviewer in reviewers:
            card_review.reviewers.add(reviewer)
        return card_review

    @staticmethod
    def update(card_comment, reviewers, description=""):

        # Get the card review
        card_review = card_comment.review
        card_review.reviewers.clear()

        # Update the reviewers
        for reviewer in reviewers:
            card_review.reviewers.add(reviewer)

        # Update the description
        card_review.description = description
        card_review.save()
        return card_review

    @staticmethod
    def update_or_create(card_comment, reviewers, description=""):
        try:
            return CardReview.update(card_comment, reviewers, description)
        except CardReview.DoesNotExist:
            return CardReview.create(card_comment, reviewers, description)


# Stat report by list
class ListReport(models.Model):
    board = models.ForeignKey("boards.Board", verbose_name=u"Board", related_name="list_reports", null=True)
    list = models.OneToOneField("boards.List", verbose_name=u"List", related_name="list_reports", unique=True)
    forward_movements = models.PositiveIntegerField(verbose_name=u"Forward movements")
    backward_movements = models.PositiveIntegerField(verbose_name=u"Backward movements")
    avg_card_time = models.DecimalField(verbose_name=u"Average time cards live in this list", decimal_places=4,
                                        max_digits=12, default=None, null=True)
    std_dev_card_time = models.DecimalField(verbose_name=u"Average time cards live in this list", decimal_places=4,
                                            max_digits=12, default=None, null=True)


# Stat report by member
class MemberReport(models.Model):
    board = models.ForeignKey("boards.Board", verbose_name=u"Board", related_name="member_reports")
    number_of_cards = models.PositiveIntegerField(verbose_name=u"Number of assigned cards", default=0)
    member = models.ForeignKey("members.Member", verbose_name=u"Member", related_name="member_reports")
    forward_movements = models.PositiveIntegerField(verbose_name=u"Forward movements", default=0)
    backward_movements = models.PositiveIntegerField(verbose_name=u"Backward movements", default=0)
    avg_card_time = models.DecimalField(verbose_name=u"Average time a card lives in the board", decimal_places=4,
                                        max_digits=12, default=None, null=True)
    std_dev_card_time = models.DecimalField(verbose_name=u"Std. Dev. time a card lives in the board", decimal_places=4,
                                            max_digits=12, default=None, null=True)
    avg_card_spent_time = models.DecimalField(verbose_name=u"Average card spent time", decimal_places=4, max_digits=12,
                                              default=None, null=True)
    std_dev_card_spent_time = models.DecimalField(verbose_name=u"Std. Deviation card spent time", decimal_places=4,
                                                  max_digits=12,
                                                  default=None, null=True)
    avg_card_estimated_time = models.DecimalField(verbose_name=u"Average task estimated card completion time",
                                                  decimal_places=4,
                                                  max_digits=12, default=None, null=True)
    std_dev_card_estimated_time = models.DecimalField(verbose_name=u"Std. Deviation of the estimated card completion time",
                                                      decimal_places=4,
                                                      max_digits=12, default=None, null=True)

