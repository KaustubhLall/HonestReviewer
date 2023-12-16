from django.db import models


class Product(models.Model):
    asin = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    embedding = models.JSONField(null=True)

    def __str__(self):
        return self.asin


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    overall = models.FloatField()
    vote = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField()
    review_text = models.TextField()
    summary_text = models.TextField()
    helpfulness_classification = models.JSONField(blank=True, null=True)
    def __str__(self):
        return f'({self.product.asin}) - {self.summary_text}'

    def get_review(self):
        template = (f' Review: {self.summary_text} - "{self.review_text}"'
                    f'| Verified Purchase: {self.verified} | Likes: {self.vote} | User Rating: {self.overall}')
        return template
