from collections.abc import Iterable
from datetime import datetime
from decimal import Decimal

from django.conf import settings

from checks.jinja2 import jinja2_check_tempate
from items.models import Item


def check_html_when(
    *,
    check_number: str,
    check_creation_time: datetime,
    check_items: Iterable[Item],
    check_total_price: Decimal,
) -> str:
    return jinja2_check_tempate.render(
        check_number=check_number,
        company_name=settings.CHECK_COMPANY_NAME,
        kkm=settings.CHECK_KKM,
        inn=settings.CHECK_INN,
        creation_time=check_creation_time,
        items=check_items,
        item_total_price=check_total_price,
    )
