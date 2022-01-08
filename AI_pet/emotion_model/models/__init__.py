from .dnn import LSTM, CNN1D

def make(config, n_feats : int):
    if config.model == 'cnn1d':
        model = CNN1D.make(
            input_shape = n_feats,
            n_kernels = config.n_kernels,
            kernel_sizes = config.kernel_sizes,
            hidden_size = config.hidden_sizes,
            dropout = config.dropout,
            n_classes = len(config.observed_emotions),
            learning_rate = config.learning_rate
        )
    elif config.model == 'lstm':
        model = LSTM.make(
            input_shape = n_feats,
            rnn_size = config.rnn_size,
            hidden_size = config.hidden_size,
            dropout = config.dropout,
            n_classes = len(config.observed_emotions),
            learning_rate = config.learning_rate
        )
    
    return model

__MODELS = {
    'cnn1d' : CNN1D,
    'lstm' : LSTM
}

def load(config):
    return __MODELS[config.model].load(
        path = config.checkpoint_path,
        name = config.checkpoint_name
    )