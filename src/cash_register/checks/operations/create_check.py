from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from cash_register.checks.details.check_html import check_html_when
from cash_register.checks.details.check_storage import (
    png_qrcode_to_stored_check_when,
    store_check,
)
from cash_register.checks.details.item_storage import (
    items_and_item_price_sum_when,
)
from cash_register.checks.details.logger import logger


@dataclass(kw_only=True, frozen=True, slots=True)
class Output:
    png_qrcode: bytes


def create_check(item_ids: list[int]) -> Output:
    log = logger()
    log.debug("check creation started", check_item_ids=item_ids)

    items, item_price_sum = items_and_item_price_sum_when(
        item_ids=item_ids, log=log
    )
    check_number = uuid4().hex
    log.debug("check received number", check_number=check_number)

    check_html = check_html_when(
        check_number=check_number,
        check_creation_time=datetime.now(UTC),
        check_items=items,
        check_total_price=item_price_sum,
        log=log,
    )

    store_check(check_number=check_number, check_html=check_html, log=log)
    png_qrcode = png_qrcode_to_stored_check_when(
        check_number=check_number, log=log
    )

    log.info("check created", check_number=check_number)

    return Output(png_qrcode=png_qrcode)
