emotions = {
    'Happy':7,
    'Surprised':6,
    'Calm':5,
    'Neutral':4,
    'Angry':3,
    'Disgust':2,
    'Sad':1,
    'Fearful':0,
}

prev_mood = 'Neutral'
curr_gif = 0
# dictionary stores index of each gif with its corresponding weight
gif_indices = range(40)
weights = { i : 1/40 for i in gif_indices }

def select_gif(prev_mood, curr_mood, curr_gif):
    # update weights: 1.5 * 情緒晉級程度
    weights[curr_gif] *= (emotions[curr_mood] - emotions[prev_mood]) * 1.5
    # return max
    return max(weights, key=weights.get)