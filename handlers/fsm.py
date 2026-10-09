from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Add_movie(StatesGroup):
    name = State()
    genre = State()
    rating = State()

router_add_movie = Router()

@router_add_movie.message(Command("form"))
async def start(message: Message, state: FSMContext):
    await message.answer("Введите название фильма: ")
    await state.set_state(Add_movie.name)

@router_add_movie.message(Add_movie.name)
async def add_movie(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите какой жанр: ")
    await state.set_state(Add_movie.genre)

@router_add_movie.message(Add_movie.genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("Введите рейтинг фильма: ")
    await state.set_state(Add_movie.rating)

@router_add_movie.message(Add_movie.rating)
async def add_rating(message: Message, state: FSMContext):

    try:
        rating = int(message.text)
    except ValueError:
        await message.answer("Введите число!")
        return

    await state.update_data(rating=rating)

    data = await state.get_data()

    await message.answer( f"Данные фильма:\n"
                         f"Название - {data['name']}\n"
                         f"Жанр - {data['genre']}\n"
                         f"Рейтинг - {data['rating']}")
    await state.clear()
