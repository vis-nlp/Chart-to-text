# -*- coding: utf-8 -*-









from tokenizers import CharBPETokenizer

# Initialize a tokenizer
tokenizer = CharBPETokenizer()

# Then train it!
tokenizer.train([ "../C2T_data/train/trainOriginalSummary.txt", 
                 "../C2T_data/train/trainTitle.txt"])


# tokenizer.add_tokens(['<PAD>', '<SEP>','<SOS>', '<EOS>','<UNK>'])

# # Now, let's use it:
# encoded = tokenizer.encode("I can feel the magic, can you?")

# And finally save it somewhere
tokenizer.save("./" ,name="bpe_tokenizer")













