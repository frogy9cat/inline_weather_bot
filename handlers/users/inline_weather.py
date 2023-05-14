import hashlib
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from loader import dp
from utils.weather import get_weather



@dp.inline_handler()
async def weather_tashkent(inline_query: InlineQuery):
    text = inline_query.query
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id = result_id,
        title = f"{text}",
        description = f"{text}...",
        thumb_url="https://img2.freepng.ru/20180414/pkq/kisspng-weather-computer-icons-weather-5ad204f41ba772.4298522015237132681133.jpg",
        input_message_content = InputTextMessageContent(get_weather(text))
    )
    await inline_query.answer(results=[item], cache_time=1)


    
    



