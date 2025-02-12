import os

# Allow an environment variable to override the default
# location for the build cache
if os.environ.get("LEMONADE_CACHE_DIR"):
    DEFAULT_CACHE_DIR = os.path.expanduser(os.environ.get("LEMONADE_CACHE_DIR"))
else:
    DEFAULT_CACHE_DIR = os.path.expanduser("~/.cache/lemonade")


def checkpoint_to_model_name(checkpoint_name: str) -> str:
    """
    Get the model's name by stripping the author's name from the checkpoint name
    """

    return checkpoint_name.split("/")[1]


class Keys:
    MODEL = "model"
    PER_ITERATION_LATENCY = "per_iteration_latency"
    MEAN_LATENCY = "mean_latency"
    STD_DEV_LATENCY = "std_dev_latency"
    TOKEN_GENERATION_TOKENS_PER_SECOND = "token_generation_tokens_per_second"
    STD_DEV_TOKENS_PER_SECOND = "std_dev_tokens_per_second"
    SECONDS_TO_FIRST_TOKEN = "seconds_to_first_token"
    PREFILL_TOKENS_PER_SECOND = "prefill_tokens_per_second"
    STD_DEV_SECONDS_TO_FIRST_TOKEN = "std_dev_seconds_to_first_token"
    CHECKPOINT = "checkpoint"
    DTYPE = "dtype"
    PROMPT = "prompt"
    PROMPT_TOKENS = "prompt_tokens"
    RESPONSE = "response"
    RESPONSE_TOKENS = "response_tokens"
    RESPONSE_LENGTHS_HISTOGRAM = "response_lengths_histogram"
    CACHE_DIR = "cache_dir"
    DEVICE = "device"
    OGA_MODELS_SUBFOLDER = "oga_models_subfolder"
    MEMORY_USAGE_PLOT = "memory_usage_plot"
