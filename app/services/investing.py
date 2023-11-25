from datetime import datetime

from app.models import ProjectAndDonationBaseModel


def investing(
        target: ProjectAndDonationBaseModel,
        sources: list[ProjectAndDonationBaseModel],
) -> list:

    required: int = target.full_amount
    modified = []

    while sources and required:
        source = sources.pop()
        available = source.full_amount - source.invested_amount

        if required >= available:
            required -= available
            source.invested_amount = source.full_amount
            source.fully_invested = True
            source.close_date = datetime.now()

        else:
            source.invested_amount += required
            required = 0

        modified.append(source)

    if required == 0:
        target.invested_amount = target.full_amount
        target.fully_invested = True
        target.close_date = datetime.now()
    else:
        target.invested_amount = target.full_amount - required

    modified.append(target)

    return modified
