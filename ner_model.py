from keras.models import Model, Input
from keras.layers.merge import add
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional, Lambda
import tensorflow as tf
import tensorflow_hub as hub


ELMo_address = "../Assets/Model/3"


def ElmoEmbedding(x, batch_size, max_len):
	elmo_model = hub.Module(ELMo_address, trainable=True)
	return elmo_model(inputs={
							"tokens": tf.squeeze(tf.cast(x, 'string')),
							"sequence_len": tf.constant(batch_size*[max_len])
						},
						signature="tokens",
						as_dict=True)["elmo"]


def NER_Model(batch_size, max_len, n_tags):
	input_text = Input(shape=(max_len,), dtype='string')
	embedding = Lambda(ElmoEmbedding, output_shape=(max_len, 1024), arguments = {"batch_size":batch_size, "max_len":max_len})(input_text)
	x = Bidirectional(LSTM(units=512, return_sequences=True,
							recurrent_dropout=0.2, dropout=0.2))(embedding)
	x_rnn = Bidirectional(LSTM(units=512, return_sequences=True,
								recurrent_dropout=0.2, dropout=0.2))(x)
	x = add([x, x_rnn])  # residual connection to the first biLSTM
	out = TimeDistributed(Dense(n_tags, activation="softmax"))(x)

	return Model(input_text, out) 


if __name__ == "__main__":
	pass