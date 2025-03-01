from collections.abc import Iterable
from decimal import Decimal

from cash_register.items.models import Item


def items_and_item_price_sum_when(
    *, item_ids: list[int]
) -> tuple[Iterable[Item], Decimal]:
    stmt = """
        SELECT
            items_item.id,
            items_item.price,
            items_item.title,
            price_sum_rel.price_sum
        FROM items_item
        CROSS JOIN (
            SELECT sum(price) AS price_sum
            FROM items_item WHERE items_item.id = ANY(%s)
        ) AS price_sum_rel
        WHERE items_item.id = ANY(%s)
        """
    items_with_price_sum = Item.objects.raw(stmt, [item_ids, item_ids])

    if items_with_price_sum:
        item_price_sum = items_with_price_sum[0].price_sum
    else:
        item_price_sum = Decimal("0")

    return items_with_price_sum, item_price_sum
