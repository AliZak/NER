def sent2words(sents):
	words = []
	for p in sents:
		words.append(p[0])
	return words


def sent2tags(sents):
	tags = []
	for p in sents:
		tags.append(p[1])
	return tags


def process_data(data, tag2idx, max_len):
	sents = []
	tags = []
	for s in data:
		sent_i = []
		tags_i = []
		for i in range(max_len):
			try:
				tags_i.append(tag2idx[s[i][1]])
				sent_i.append(s[i][0])
			except:
				tags_i.append(tag2idx["O"])
				sent_i.append("PAD")
		tags.append(tags_i)
		sents.append(sent_i)
	return sents, tags


def process_sent(s, max_len):
	sent = []
	for i in range(max_len):
		try:
			sent.append(s[i])
		except:
			sent.append("PAD")
	return sent


def make_batch(sample, batch_size):
	for i in range(batch_size - len(sample)):
		sample.append(process_sent([], max_len))
	return sample


if __name__ == "__main__":
	pass