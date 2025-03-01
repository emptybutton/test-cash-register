from collections.abc import Iterable
from datetime import datetime
from decimal import Decimal

from django.conf import settings

from cash_register.checks.details.logger import Logger
from cash_register.checks.jinja2 import jinja2_check_tempate
from cash_register.items.models import Item


def check_html_when(
    *,
    check_number: str,
    check_creation_time: datetime,
    check_items: Iterable[Item],
    check_total_price: Decimal,
    log: Logger,
) -> str:
    html = jinja2_check_tempate.render(
        check_number=check_number,
        company_name=settings.CHECK_COMPANY_NAME,
        kkm=settings.CHECK_KKM,
        inn=settings.CHECK_INN,
        creation_time=check_creation_time,
        items=check_items,
        item_total_price=check_total_price,
    )
    log.debug("check html generated", check_number=check_number)

    return html
