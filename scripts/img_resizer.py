from PIL import Image

BASE_DIR = '../assets/images/raft/'
imgs = list(map(lambda index: BASE_DIR + 'log_rep_{}.png'.format(index), range(1,6)))

for img_route in imgs:
    img = Image.open(img_route)
    w, h = img.size
    img.resize((w//2, h//2))
    img.save(img_route)
