from io import BytesIO

import requests

from PIL import Image


def display_remote_image(url: str) -> None:
    import unicornhathd

    response = requests.get(url)
    source = Image.open(BytesIO(response.content))

    unicornhathd.rotation(180)
    unicornhathd.brightness(0.2)

    width, height = unicornhathd.get_shape()

    image = source.resize((width, height), resample=Image.BILINEAR)

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])

            unicornhathd.set_pixel(x, y, r, g, b)

    unicornhathd.show()

    # except KeyboardInterrupt:
    #     unicornhathd.off()
