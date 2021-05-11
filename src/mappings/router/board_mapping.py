from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
import datetime

from src.services.board_services import (
    add_board,
    get_all_boards,
    get_by_id,
    count_all
)

from src.models.board_model import (
    BoardModel,
    ResponseCreate,
    SuccessGetAllResponse,
    SuccessResponse,
    ErrorResponse,
)

router = APIRouter()


@router.post('/boards', response_description='Create Board', tags=['boards'])
async def create_board(request: Request, board: BoardModel = Body(...)):

    if(board is None):
        raise HTTPException(
            status_code=404, detail="Vui lòng điền đẩy đủ thông tin")

    board = jsonable_encoder(board)

    if(board['registerDate'] is None):
        raise HTTPException(
            status_code=404, detail="Vui lòng nhập ngày đăng ký")

    if(board['title'] is None):
        raise HTTPException(status_code=404, detail="Vui lòng nhập tiêu đề")
    else:
        if(board['title'].strip() == ''):
            raise HTTPException(
                status_code=404, detail="Vui lòng không nhập khoảng trống cho tiêu đề"
            )
        else:
            len_title = len(board['title'])

            if(len_title > 100):
                raise HTTPException(
                    status_code=404, detail="Tiêu đề không vượt quá 100 ký tự"
                )

    if(board['name'] is None):
        raise HTTPException(status_code=404, detail="Vui lòng nhập tên")
    else:
        if(board['name'].strip() == ''):
            raise HTTPException(
                status_code=404, detail="Vui lòng không nhập khoảng trống cho tên"
            )
        else:
            len_name = len(board['name'])

            if(len_name > 50):
                raise HTTPException(
                    status_code=404, detail="Tên không vượt quá 50 ký tự"
                )

    if(board['text'] is None):
        raise HTTPException(status_code=404, detail="Vui lòng nhập nội dung")
    else:
        if(board['text'].strip() == ''):
            raise HTTPException(
                status_code=404, detail="Vui lòng không nhập khoảng trống cho nội dung"
            )
        else:
            len_text = len(board['text'])

            if(len_text > 1000):
                raise HTTPException(
                    status_code=404, detail="Nội dung không vượt quá 1000 ký tự"
                )

    new_board = await add_board(board, request.app.collection['boards'])

    return ResponseCreate(new_board, 'Đã đăng ký')


@router.get("/boards", response_description='List Board', tags=['boards'])
async def get_boards(request: Request, _start: int = 0, _end: int = 1000):

    data = await get_all_boards(request.app.collection['boards'], _start, _end)

    total = await count_all(request.app.collection['boards'])

    return SuccessGetAllResponse(data, total, 'Success')


@router.get('/boards/{id}', response_description='Get Board By Id', tags=['boards'])
async def getBoardById(id: str, request: Request):

    if(id is None):
        raise HTTPException(
            status_code=404, detail="Id not found"
        )

    data = await get_by_id(id, request.app.collection['boards'])

    return SuccessResponse(data, 'Success')
