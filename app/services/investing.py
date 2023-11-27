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
        for obj in target, source:
            obj.invested_amount += investment
            if obj.invested_amount == obj.full_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()
        modified.append(source)
        if target.fully_invested:
            break
    return modified
