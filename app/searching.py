import aiohttp
from app.database import session
from app.fragment import GetFragment


async def searching(phrase):
    """Searching fragment."""
    fragment_text = None
    step = 0

    async with aiohttp.ClientSession() as cl_session:
        while not fragment_text and step < 100:
            try:
                db = session()
                book = GetFragment(phrase, db)
                url = book.get_text_link()

                async with cl_session.get(url) as response:
                    html_text = await response.text()
                    text = book.get_text(html_text)
                    fragment_text = book.search_fragment_in_text(text)
                    if fragment_text:
                        return fragment_text

            finally:
                db.close()
            step += 1

        return "Отрывок не найден..."
