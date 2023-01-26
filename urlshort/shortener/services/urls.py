from hashlib import md5

from django.db.models import F

from shortener.models import URL


def create_shortened_url(original_url: str) -> URL:
    url, created = URL.objects.get_or_create(original_url=original_url)
    if created:
        url.short_url = make_short_url_part(original_url)
        url.save(update_fields=('short_url',))
    return url


def get_url(short_url: str) -> URL:
    """Get URL object by short url, increase the follows"""
    url = URL.objects.get(short_url=short_url)
    url.follow_count = F('follow_count') + 1
    url.save()
    return url


def make_short_url_part(original_url: str) -> str:
    """Sequence of 6 symbols"""
    return md5(original_url.encode()).hexdigest()[:6]
