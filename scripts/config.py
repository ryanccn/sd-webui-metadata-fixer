import gradio as gr
from modules import script_callbacks
from modules import shared


def on_ui_settings():
    section = ("metadata_fixer", "Metadata fixer")
    shared.opts.add_option(
        "metadata_fixer_prefix",
        shared.OptionInfo(
            default="", label="Prefix", component=gr.Text, section=section
        ),
    )

    shared.opts.add_option(
        "metadata_fixer_suffix",
        shared.OptionInfo(
            default="", label="Suffix", component=gr.Text, section=section
        ),
    )


script_callbacks.on_ui_settings(on_ui_settings)
