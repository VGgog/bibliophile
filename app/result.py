import aiohttp
from app.database import session
from app import fragment


async def get_result(phrase):
    """Return result of searching fragment"""
    async with aiohttp.ClientSession() as client:
        for i in range(100):
            with session() as db:

                book = fragment.get_book(db)
                result = await get_result_of_searching(client, phrase, book)
                
                if result:
                    return result

        return "Отрывок не найден..."


async def send_request(client, url):
    """Send get request on web-site with text"""
    async with client.get(url) as response:
        return await response.text()


async def get_result_of_searching(client, phrase, book):
    """Return fragment if fragment found else none"""

    url = fragment.get_text_link(book)

    html_text = await send_request(client, url)
                
    text = fragment.get_text(html_text)
    result = fragment.search_fragment_in_text(phrase, text)
     
    return result
