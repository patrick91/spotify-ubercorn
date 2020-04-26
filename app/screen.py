from io import BytesIO

import requests

from PIL import Image, ImageEnhance


def display_remote_image(url: str, brightness: float = 0.3) -> None:
    import unicornhathd

    response = requests.get(url)
    source = Image.open(BytesIO(response.content))

    unicornhathd.rotation(0)
    unicornhathd.brightness(brightenss)

    width, height = unicornhathd.get_shape()

    sat_booster = ImageEnhance.Color(source)
    img = sat_booster.enhance(1.25)

    # increase contrast of image
    contr_booster = ImageEnhance.Contrast(img)
    img = contr_booster.enhance(1.2)

    # reduce the number of colors used in picture
    img = img.convert("P", palette=Image.ADAPTIVE, colors=10)

    img = source.resize((width, height), resample=Image.BICUBIC)

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])

            unicornhathd.set_pixel(x, y, r, g, b)

    unicornhathd.show()

    # except KeyboardInterrupt:
    #     unicornhathd.off()
