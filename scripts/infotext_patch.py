from modules import txt2img
from modules.shared import cmd_opts

original_infotext = txt2img.processing.create_infotext


def new_infotext(
    p,
    all_prompts,
    all_seeds,
    all_subseeds,
    comments=[],
    iteration=0,
    position_in_batch=0,
):
    original = original_infotext(
        p,
        all_prompts,
        all_seeds,
        all_subseeds,
        comments,
        iteration,
        position_in_batch,
    )

    if cmd_opts.metadata_prefix:
        original = cmd_opts.metadata_prefix + " " + original
    if cmd_opts.metadata_suffix:
        original = original + " " + cmd_opts.metadata_suffix

    return original


txt2img.processing.create_infotext = new_infotext

print(
    f"Patched txt2img.processing.create_infotext() with prefix {cmd_opts.metadata_prefix} and suffix {cmd_opts.metadata_suffix}"
)
