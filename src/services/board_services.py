from bson.objectid import ObjectId
from fastapi import Request
import datetime
import asyncstdlib as a
from datetime import timezone

# convert response


def convert_responses(board, index) -> dict:

    register_date = board['registerDate']

    date_format = register_date.replace(tzinfo=datetime.timezone.utc)

    return {
        "id": str(board["_id"]),
        "registerDate": date_format,
        "title": board["title"],
        "name": board["name"],
        "text": board["text"],
        "index": index,
    }


def convert_response(board) -> dict:

    register_date = board['registerDate']

    date_format = register_date.replace(tzinfo=datetime.timezone.utc)

    return {
        "id": str(board["_id"]),
        "registerDate": date_format,
        "title": board["title"],
        "name": board["name"],
        "text": board["text"],
    }

# get all boards


async def get_all_boards(collection, skip, limit):
    boards = []

    limit = limit - skip

    async for index, item in a.enumerate(collection.find({"deleted": False}).sort("registerDate", -1).skip(skip).limit(limit)):
        boards.append(convert_responses(item, index))

    return boards

# create board


async def add_board(board_data: dict, collection) -> dict:
    dateRegister = board_data['registerDate']

    dateFormat = datetime.datetime.fromisoformat(dateRegister)

    board_data['registerDate'] = dateFormat

    board = await collection.insert_one(board_data)

    new_board = await collection.find_one({"_id": board.inserted_id})

    return convert_response(new_board)


# Retrieve a student with a matching ID
async def get_by_id(id: str, collection) -> dict:
    board = await collection.find_one({"_id": ObjectId(id)})

    if board:
        return convert_response(board)


async def count_all(collection) -> dict:
    count_docs = await collection.count_documents({'deleted': False})

    return count_docs
