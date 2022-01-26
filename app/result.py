import aiohttp
from app.database import session
from app import searching


async def get_result(phrase):
    """Return result of searching fragment"""
    async with aiohttp.ClientSession() as client:
        # Bibliophile search a fragment in 100 book text.
        for i in range(100):
            with session() as db:

                book = searching.get_book(db)
                result = await get_the_search_result(client, phrase, book)
                
                if result:
                    return {"fragment": result,
                            "author": book.author,
                            "book_title": book.book_title}

        return None


async def get_the_search_result(client, phrase, book):
    """Return fragment if fragment found else none"""

    url = searching.get_text_link(book)

    html_text = await send_request(client, url)
                
    text = searching.get_text(html_text)
    result = searching.search_fragment_in_text(phrase, text)
     
    return result


async def send_request(client, url):
    """Send get request on web-site with text"""
    async with client.get(url) as response:
        return await response.text()
