from modules import script_callbacks
import gradio as gr
from PIL import Image
import numpy as np
from imgutils.detect import detect_halfbody, detect_heads

def on_ui_tab_called():
    with gr.Blocks() as transparent_interface:
        with gr.Row():
            with gr.Tabs():
                with gr.TabItem("CropHead"):
                    image_upload_input = gr.Image(label="Upload Image", source="upload",type="pil")
                    button = gr.Button(label="Convert")
                    image_upload_output = gr.Image(label="Output Image",type="numpy")
                    
                    def convert_image(image:Image.Image):
                        """
                        Converts the image to apng
                        The black color (with some threshold) will remain, others will be transparent
                        """
                        # first convert to RGB
                        # warn : APNG transparent channels should be converted as white
                        if image.mode == "RGBA":
                            # convert transparent pixels to white
                            white_image = Image.new("RGB", image.size, (255, 255, 255))
                            white_image.paste(image, mask=image.split()[3])
                            image = white_image
                        else:
                            image = image.convert("RGB")
                        result = detect_heads(image)
                        new_image = image.crop(result[0][0])
                        return new_image # return the new image
                    button.click(convert_image, inputs=[image_upload_input], outputs=[image_upload_output])
    return (transparent_interface, "CropHead", "script_crophead_interface"),

script_callbacks.on_ui_tabs(on_ui_tab_called)