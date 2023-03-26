from modules import txt2img
from modules.shared import opts

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

    if opts.metadata_fixer_prefix:
        original = opts.metadata_fixer_prefix + " " + original
    if opts.metadata_fixer_suffix:
        original = original + " " + opts.metadata_fixer_suffix

    return original


txt2img.processing.create_infotext = new_infotext
