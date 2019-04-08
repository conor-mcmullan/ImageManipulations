try:
    import os
    import sys
    from PIL import Image
    from image_types import *
except Exception as import_error:
    raise ImportError(f"{str(import_error)}")


class ImageHandler:

    def __init__(self):
        self.ORIGINAL_IMAGES_PATH = "images/original/"
        self.ALTERED_IMAGES_PATH = "images/altered/"
        self.BOX_IMAGES = self.ALTERED_IMAGES_PATH + "boxes/"

    @staticmethod
    def get_folder_contents(folder_path):
        return os.listdir(folder_path)

    @staticmethod
    def get_image_object(file_path):
        return Image.open(file_path)

    def get_original_files(self):
        return [self.ORIGINAL_IMAGES_PATH + fn for fn in self.get_folder_contents(self.ORIGINAL_IMAGES_PATH)]

    def get_altered_files(self):
        return [self.ALTERED_IMAGES_PATH + fn for fn in self.get_folder_contents(self.ALTERED_IMAGES_PATH)]

    def convert_file_via_path(self, file_path, new_type):
        image = self.get_image_object(file_path)
        idx_dot = file_path.rfind('.')
        old_type = file_path[idx_dot:]
        file_path = file_path.replace(old_type, new_type)
        file_path = file_path.replace(self.ORIGINAL_IMAGES_PATH, self.ALTERED_IMAGES_PATH)
        image.save(file_path)

    def get_image_information(self, file_path, attribute='All'):
        image = self.get_image_object(file_path)
        dimensions = width, height = image.size
        attributes_dict = dict()
        attributes_dict['dimensions'] = dimensions
        attributes_dict['width'] = width
        attributes_dict['height'] = height
        if attribute == 'All':
            return attributes_dict
        else:
            low_att = str(attribute).lower()
            att_keys = attributes_dict.keys()
            if low_att in att_keys:
                return attributes_dict[low_att]
            else:
                raise KeyError(f"{str(low_att)} not in "
                               f"accepted list {str(att_keys)}")


if __name__ == "__main__":

    COLS = 15
    ROWS = 10

    img_hand = ImageHandler()

    ORIGINAL_FILES = img_hand.get_original_files()
    ALTERED_FILES = img_hand.get_altered_files()

    print("\nOriginal Files:\t", ORIGINAL_FILES)
    print("\nAltered Files:\t", ALTERED_FILES)

    image_file_name_1 = ORIGINAL_FILES[0]
    print("\nFile 1:\t", image_file_name_1)

    image_1 = Image.open(image_file_name_1)
    # image_1.show()
    # img_hand.convert_file_via_path(image_file_name_1, PNG)
    # attributes = img_hand.get_image_information(image_file_name_1)

    # print(dir(image_1))
    # image_dict = image_1.__dict__

    # print("\nImage Information:\n")
    # for k, v in image_dict.items():
        # print(str(k), str(v))

    h = image_1.height
    print(h)

    w = image_1.width
    print(w)

    pieces = ROWS * COLS
    print("number of tiles = ", pieces)

    boxes_list = []

    piece_h = (h / ROWS) - 2  # 2 pixels
    piece_w = (w / COLS) - 2  # 2 pixels

    print("pieces height", piece_h)
    print("pieces width", piece_w)

    for r in range(ROWS):
        for c in range(COLS):
            upper = r * piece_h
            lower = upper + piece_h
            right_most = (c + 1) * piece_w
            left_most = c * piece_w
            Box = (left_most, upper, right_most, lower)
            cropped = image_1.crop(box=Box)
            cropped_fn = img_hand.BOX_IMAGES + f'{str(r)}_{str(c)}.jpg'
            boxes_list.append(cropped_fn)
            cropped.save(cropped_fn)

    print("Number Pieces:\t", len(boxes_list))
    print(boxes_list)

    # TODO - compress images + weight them and create list of groups
