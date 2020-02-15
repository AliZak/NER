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


def make_batch(sample, batch_size, max_len):
	for i in range(batch_size - len(sample)):
		sample.append(process_sent([], max_len))
	return sample


def predict_tags(tags, y_pred):
	out = []
	for i in range(len(y_pred)):
		out_i = []
		for j in range(len(y_pred[i])):
			out_i.append(tags[y_pred[i][j]])
		out.append(out_i)
	return out


if __name__ == "__main__":
	pass