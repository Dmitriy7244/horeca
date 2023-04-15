import io
import secrets
from typing import Union

import aiohttp
from PIL import Image


class TelegraphImage:
    SERVICE_URL = 'https://telegra.ph'

    def __init__(self, session, file_url: str, new_ratio: Union[int, float]):
        self.session = session
        self.file_url = file_url
        self.new_ratio = new_ratio
        self._pillow_image = None

    async def get_image_bytes(self):
        async with self.session.get(self.file_url) as response:
            return io.BytesIO(await response.content.read())

    async def get_pillow_image(self):
        if not self._pillow_image:
            image_bytes = await self.get_image_bytes()
            self._pillow_image = Image.open(image_bytes)
        return self._pillow_image

    def calculate_new_width(self, image):
        new_width = image.height * self.new_ratio

        if image.width < new_width:
            raise ValueError('Photo is too narrow!')

        return new_width

    async def get_new_pillow_image(self):
        image = await self.get_pillow_image()
        extra_widths = (image.width - self.calculate_new_width(image)) / 2
        left_edge, right_edge = extra_widths, image.width - extra_widths
        box = left_edge, 0, right_edge, image.height
        return image.crop(box)

    async def get_new_image_bytes(self) -> bytes:
        image = await self.get_new_pillow_image()
        fp = io.BytesIO()
        image.save(fp, 'JPEG')
        return fp.getvalue()

    async def get_new_image_url(self) -> str:
        """Upload photo to telegraph, return new url"""
        form = aiohttp.FormData(quote_fields=False)

        name = secrets.token_urlsafe(8)
        image_bytes = await self.get_new_image_bytes()
        form.add_field(name, image_bytes, filename=name)

        async with self.session.post(f'{self.SERVICE_URL}/upload', data=form) as r:
            result = await r.json()

        return f'{self.SERVICE_URL}{result[0]["src"]}'
