# labels: name::mpt_30b author::transformers task::Generative_AI license::apache-2.0
from turnkeyml.parser import parse
from transformers import MptModel, AutoConfig
import torch

torch.manual_seed(0)

# Parsing command-line arguments
pretrained, batch_size, max_seq_length = parse(
    ["pretrained", "batch_size", "max_seq_length"]
)

# Model and input configurations
if pretrained:
    model = MptModel.from_pretrained("mosaicml/mpt-30b")
else:
    config = AutoConfig.from_pretrained("mosaicml/mpt-30b")
    model = MptModel(config)


inputs = {
    "input_ids": torch.ones(batch_size, max_seq_length, dtype=torch.long),
    "attention_mask": torch.ones(batch_size, max_seq_length, dtype=torch.float),
}


# Call model
model(**inputs)
