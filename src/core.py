# standard library
import os
import tkinter as tk
from tkinter import filedialog

# 3rd party
import matplotlib as mpl
import matplotlib.pyplot as plt


class AssetManager:
    """
    Stores paths to asset files as attributes.
    Use in higher level modules to 'ask' for the path to each resource.
        ex: resource_path = AssetManager.resource
    Important b/c this behavior changes slightly when running as frozen (.exe)
    """

    # main assets folder name
    assets = "assets"

    # subfolder names
    icons = "icons"
    fonts = "fonts"
    templates = "templates"

    # define relative paths
    src_folder = os.path.dirname(os.path.abspath(__file__))
    assets_folder = os.path.join(src_folder, assets)
    app_icon = os.path.join(assets_folder, icons, "app.ico")
    file_icon = os.path.join(assets_folder, icons, "file.ico")
    font_file = os.path.join(assets_folder, fonts, "OpenSans-Regular.ttf")

    cmd_list_template = os.path.join(
        assets_folder, templates, "CommandList_TEMPLATE.txt"
    )
    out_template = os.path.join(assets_folder, templates, "OUT_TEMPLATE.out")

    # this is just a  test file, delete me later
    data_file = os.path.join(assets_folder, "data.csv")


# %% simple tkinter popup functions
def file_browse(multiple=False, filetypes=[("Image File", ("*.png", "*.jpg"))]):
    filetypes.append(("All Files", "*"))
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(AssetManager.file_icon)

    if multiple:
        path = filedialog.askopenfilenames(filetypes=filetypes)
    else:
        path = filedialog.askopenfilename(filetypes=filetypes)
    root.destroy()
    return path if path != "" else None


# get coordinates
def get_image_coords(image_path):
    image = plt.imread(image_path)
    title = "Left-Click on the image to add a point\nRight-Click to undo the last point\nMiddle-Click to finish"
    # disable plot toolbar - not sure if this is needed
    # with mpl.rc_context({"toolbar": "None"}):
    plt.imshow(image)
    plt.title(title)
    plt.tight_layout()
    coordinates = plt.ginput(n=-1, timeout=0)
    plt.close()
    return coordinates


def calc_distance(xy0, xy1):
    x0, y0 = xy0
    x1, y1 = xy1
    dx = x1 - x0
    dy = y0 - y1
    return (dx**2 + dy**2) ** 0.5


def calibrate_scale(image_path):
    image = plt.imread(image_path)
    title = "Left-Click on 2 points in the image\nRight-Click to undo the last point"

    # disable plot toolbar
    with mpl.rc_context({"toolbar": "None"}):
        plt.imshow(image)
    plt.title(title)
    plt.tight_layout()
    coordinates = plt.ginput(n=2, timeout=0)
    plt.close()

    pixel_distance = calc_distance(coordinates[0], coordinates[1])

    # make this a better input later
    full_scale_distance = float(input("Enter Full Scale Distance: "))
    pixels_per_unit = pixel_distance / full_scale_distance

    return pixels_per_unit


if __name__ == "__main__":
    image_path = file_browse()

    # coordinates = get_image_coords(image_path)
    # # print output
    # [
    #     print(f"Point {index}: ({value[0]:.2f}, {value[1]:.2f})")
    #     for index, value in enumerate(coordinates)
    # ]

    distance = print("Pixels Per Unit: ", calibrate_scale(image_path))
