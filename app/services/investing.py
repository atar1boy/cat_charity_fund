from datetime import datetime

from app.models import BaseInvestmentFieldsModel


def investing(
        target: BaseInvestmentFieldsModel,
        sources: list[BaseInvestmentFieldsModel],
) -> list[BaseInvestmentFieldsModel]:
    modified = []
    for source in sources:
        investment = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount
        )
        target.invested_amount += investment
        source.invested_amount += investment
        if source.invested_amount == source.full_amount:
            source.fully_invested = True
            source.close_date = datetime.now()
        modified.append(source)
        if target.invested_amount == target.full_amount:
            target.fully_invested = True
            target.close_date = datetime.now()
            break
    return modified
