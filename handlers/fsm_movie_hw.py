from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import main_db


class Add_movie(StatesGroup):
    name = State()
    genre = State()
    year = State()
    description = State()
    rating = State()


router_add_movie = Router()


@router_add_movie.message(Command("form"))
async def start(message: Message, state: FSMContext):
    await message.answer("Введите название фильма: ")
    await state.set_state(Add_movie.name)


@router_add_movie.message(Add_movie.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите какой жанр: ")
    await state.set_state(Add_movie.genre)


@router_add_movie.message(Add_movie.genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("Введите год выхода: ")
    await state.set_state(Add_movie.year)


@router_add_movie.message(Add_movie.year)
async def add_year(message: Message, state: FSMContext):
    if not message.text or not message.text.isdigit():
        await message.answer("Год должен быть числом!")
        return

    await state.update_data(year=int(message.text))
    await message.answer("Коротко опишите фильм: ")
    await state.set_state(Add_movie.description)


@router_add_movie.message(Add_movie.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите рейтинг фильма (от 1 до 10): ")
    await state.set_state(Add_movie.rating)


@router_add_movie.message(Add_movie.rating)
async def add_rating(message: Message, state: FSMContext):
    try:
        rating = int(message.text)
    except (ValueError, TypeError):
        await message.answer("Введите число!")
        return

    if not 1 <= rating <= 10:
        await message.answer("Рейтинг должен быть от 1 до 10!")
        return

    await state.update_data(rating=rating)
    data = await state.get_data()

    await main_db.add_movie_db(name=data['name'], genre=data['genre'], rating=data['rating'],
                               year=data['year'], description=data['description'])

    await message.answer(f"Фильм сохранён!\n"
                         f"Название - {data['name']}\n"
                         f"Жанр - {data['genre']}\n"
                         f"Год - {data['year']}\n"
                         f"Описание - {data['description']}\n"
                         f"Рейтинг - {data['rating']}")
    await state.clear()


# Список фильмов — данные собираются из двух таблиц через INNER JOIN
@router_add_movie.message(Command("movies"))
async def get_movies(message: Message):
    movies = await main_db.get_movies_db()

    if not movies:
        await message.answer("Фильмов пока нет! Добавьте через /form")
        return

    for movie_id, name, rating, genre, year, description in movies:
        await message.answer(f"🎬 {name} ({year})\n"
                             f"Жанр - {genre}\n"
                             f"Описание - {description}\n"
                             f"Рейтинг - {rating}/10")
