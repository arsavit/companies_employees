"""
Модуль для сигналов приложения Компании
"""

from typing import Any

from django.core.exceptions import ValidationError
from django.db.models.base import ModelBase
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from backend.apps.companies.models import Company


@receiver(m2m_changed, sender=Company.partners_companies.through)
def prevent_duplicate_tags_from_group(
    sender: ModelBase,
    instance: Company,
    action: str,
    reverse: bool,
    model: ModelBase,
    pk_set: set,
    **kwargs: Any,
) -> None:
    """Запрещаем Компании 'сотрудничать' с собой"""
    if action == "pre_add":
        if instance.pk in pk_set:
            raise ValidationError("Вы не можете сотрудничать с собой((")
