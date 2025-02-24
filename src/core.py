import os
import tkinter as tk
from tkinter import filedialog


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


# browser popup functions
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


if __name__ == "__main__":
    print(file_browse())
