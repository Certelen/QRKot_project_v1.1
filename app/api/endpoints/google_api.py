from http import HTTPStatus

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud import project_crud
from app.services.google_api import (set_user_permissions, spreadsheets_create,
                                     spreadsheets_update_value)

router = APIRouter()


@router.post(
    '/',
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    try:
        spreadsheet_id, spreadsheet_url = await spreadsheets_create(
            wrapper_services)
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Ошибка при создании отчета!',
        )
    try:
        await set_user_permissions(
            spreadsheet_id, wrapper_services)
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='Превышен лимит по созданию отчетов за короткое время!',
        )
    try:
        await spreadsheets_update_value(
            spreadsheet_id,
            wrapper_services,
            await project_crud.get_projects_by_completion_rate(session))
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Ошибка при внесении данных в отчет!',
        )
    return f'Ссылка на документ: {spreadsheet_url}'
