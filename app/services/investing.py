from datetime import datetime

from app.models import BaseInvestmentFieldsModel


def investing(
        target: BaseInvestmentFieldsModel,
        sources: list[BaseInvestmentFieldsModel],
) -> tuple[BaseInvestmentFieldsModel, list[BaseInvestmentFieldsModel]]:
    modified = []
    for source in sources:
        required = target.full_amount - target.invested_amount
        available = source.full_amount - source.invested_amount
        investment = 0
        if required > available:
            investment += available
        if required <= available:
            investment += required
        target.invested_amount += investment
        source.invested_amount += investment
        close_investment(target, source)
        modified.append(source)
    return target, modified


def close_investment(*objs: BaseInvestmentFieldsModel):
    for obj in objs:
        if obj.invested_amount == obj.full_amount:
            obj.fully_invested = True
            obj.close_date = datetime.now()
