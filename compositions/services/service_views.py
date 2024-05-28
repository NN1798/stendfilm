from typing import Optional
from datetime import datetime
from django.utils import timezone
from django_filters import rest_framework as filters

from ..models import Composition, Comment


def check_comment_frequency(last_comment_time: datetime) -> bool:
    """Проверяет, прошло ли достаточно времени с момента последнего комментария пользователя.

    Args:
        last_comment_time (datetime.datetime): Время последнего комментария пользователя.

    Returns:
        bool: Возвращает True, если прошло достаточно времени с момента последнего комментария,
              и False в противном случае.
    """

    if last_comment_time:
        min_comment_interval = timezone.timedelta(minutes=1)
        time_since_last_comment = timezone.now() - last_comment_time
        return time_since_last_comment >= min_comment_interval
    return True


def get_last_comment(user_id: int, queryset: Optional[list[Comment]] = None) -> Optional[Comment]:
    """Выдает последний комментарий пользователя.

    Args:
        user_id (int): ID пользователя.
        queryset (Optional[list[Comment]]): Список комментариев для фильтрации.

    Returns:
        Optional[Comment]: Последний комментарий пользователя или None, если список пустой.
    """

    if queryset is None:
        return None

    return list(filter(lambda comment: comment.user.id == user_id, queryset))[-1]


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CompositionFilter(filters.FilterSet):
    company = CharFilterInFilter(field_name='company__title', lookup_expr='in')
    country = CharFilterInFilter(field_name='country__title', lookup_expr='in')
    genre = CharFilterInFilter(field_name='genre__title', lookup_expr='in')

    class Meta:
        model = Composition
        fields = ['type', 'company', 'release_year', 'country', 'genre']
