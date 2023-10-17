import imageio
from PIL import Image, ImageDraw, ImageFont

frames = []

# Загрузка изображений и добавление их в список кадров.
for frame_number in range(2001, 2022):
    frame = Image.open(f'data/mosaic_{frame_number}.png')
    frames.append(frame)

# Создание плавной анимации путем линейной интерполяции между каждой парой кадров.
smooth_frames = []
for i in range(len(frames) - 1):
    for alpha in range(0, 101, 2):  # Увеличьте шаг для более плавного перехода
        blended_frame = Image.blend(frames[i], frames[i + 1], alpha / 100.0)

        draw = ImageDraw.Draw(blended_frame)
        font_path = "TNR.ttf"  # Укажите полный путь к вашему ttf-шрифту
        font_size = 100
        font = ImageFont.truetype(font_path, font_size)

        current_year = 2000 + i + 3
        text = f'Fire. Year: {current_year}'
        text_position = (1000, 1800)  # Позиция текста на кадре
        draw.text(text_position, text, fill="white", font=font)

        smooth_frames.append(blended_frame)

# Сохранение анимации в формате MP4.
fps = 30  # Количество кадров в секунду
video_output_path = 'video/fire.mp4'
imageio.mimsave(video_output_path, [frame for frame in smooth_frames], fps=fps, format='mp4')
