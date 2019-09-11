from glove import *

def check_cosine_similarity(words, word_to_vec_map):
	# Test consine_similarity

	# cosine_similarity(father, mother) =  0.890903844289
	# cosine_similarity(ball, crocodile) =  0.274392462614
	# cosine_similarity(france - paris, rome - italy) =  -0.675147930817

	father = word_to_vec_map["father"]
	mother = word_to_vec_map["mother"]
	ball = word_to_vec_map["ball"]
	crocodile = word_to_vec_map["crocodile"]
	france = word_to_vec_map["france"]
	italy = word_to_vec_map["italy"]
	paris = word_to_vec_map["paris"]
	rome = word_to_vec_map["rome"]

	print("cosine_similarity(father, mother) = ", cosine_similarity(father, mother))
	print("cosine_similarity(ball, crocodile) = ",cosine_similarity(ball, crocodile))
	print("cosine_similarity(france - paris, rome - italy) = ",cosine_similarity(france - paris, rome - italy))	


def check_complete_analogy(words, word_to_vec_map):
	# Analgoies of words with complete_analogy function

	# italy -> italian :: spain -> spanish
	# india -> delhi :: japan -> tokyo
	# man -> woman :: boy -> girl
	# small -> smaller :: large -> larger

	triads_to_try = [('italy', 'italian', 'spain'), ('india', 'delhi', 'japan'), ('man', 'woman', 'boy'), ('small', 'smaller', 'large')]
	for triad in triads_to_try:
		print ('{} -> {} :: {} -> {}'.format( *triad, complete_analogy(*triad,word_to_vec_map)))


def printing_baised_words(words, word_to_vec_map):
	# [-0.087144    0.2182     -0.40986    -0.03922    -0.1032      0.94165
	#  -0.06042     0.32988     0.46144    -0.35962     0.31102    -0.86824
	#   0.96006     0.01073     0.24337     0.08193    -1.02722    -0.21122
	#   0.695044   -0.00222     0.29106     0.5053     -0.099454    0.40445
	#   0.30181     0.1355     -0.0606     -0.07131    -0.19245    -0.06115
	#  -0.3204      0.07165    -0.13337    -0.25068714 -0.14293    -0.224957
	#  -0.149       0.048882    0.12191    -0.27362    -0.165476   -0.20426
	#   0.54376    -0.271425   -0.10245    -0.32108     0.2516     -0.33455
	#  -0.04371     0.01258   ]

	g = word_to_vec_map['woman'] - word_to_vec_map['man']
	print(g)
	print()


	# List of names and their similarities with constructed vector:
	# john -0.23163356146
	# marie 0.315597935396
	# sophie 0.318687898594
	# ronaldo -0.312447968503
	# priya 0.17632041839
	# rahul -0.169154710392
	# danielle 0.243932992163
	# reza -0.079304296722
	# katy 0.283106865957
	# yasmin 0.233138577679

	print ('List of names and their similarities with constructed vector:')

	# girls and boys name
	name_list = ['john', 'marie', 'sophie', 'ronaldo', 'priya', 'rahul', 'danielle', 'reza', 'katy', 'yasmin']

	for w in name_list:
		print (w, cosine_similarity(word_to_vec_map[w], g))	

	print()

	# Other words and their similarities:
	# lipstick 0.276919162564
	# guns -0.18884855679
	# science -0.0608290654093
	# arts 0.00818931238588
	# literature 0.0647250443346
	# warrior -0.209201646411
	# doctor 0.118952894109
	# tree -0.0708939917548
	# receptionist 0.330779417506
	# technology -0.131937324476
	# fashion 0.0356389462577
	# teacher 0.179209234318
	# engineer -0.0803928049452
	# pilot 0.00107644989919
	# computer -0.103303588739
	# singer 0.185005181365

	print('Other words and their similarities:')
	word_list = ['lipstick', 'guns', 'science', 'arts', 'literature', 'warrior','doctor', 'tree', 'receptionist', 
	             'technology',  'fashion', 'teacher', 'engineer', 'pilot', 'computer', 'singer']
	for w in word_list:
		print (w, cosine_similarity(word_to_vec_map[w], g))

	print()


def check_neutralize(words, word_to_vec_map):
	# cosine similarity between receptionist and g, before neutralizing:  0.330779417506
	# cosine similarity between receptionist and g, after neutralizing:  -4.08872263257e-17

	g = word_to_vec_map['woman'] - word_to_vec_map['man']

	e = "receptionist"
	print("cosine similarity between " + e + " and g, before neutralizing: ", cosine_similarity(word_to_vec_map["receptionist"], g))

	e_debiased = neutralize("receptionist", g, word_to_vec_map)
	print("cosine similarity between " + e + " and g, after neutralizing: ", cosine_similarity(e_debiased, g))


def check_equalize(words, word_to_vec_map):
	# cosine similarities before equalizing:
	# cosine_similarity(word_to_vec_map["man"], gender) =  -0.117110957653
	# cosine_similarity(word_to_vec_map["woman"], gender) =  0.356666188463

	# cosine similarities after equalizing:
	# cosine_similarity(e1, gender) =  -0.700436428931
	# cosine_similarity(e2, gender) =  0.700436428931

	g = word_to_vec_map['woman'] - word_to_vec_map['man']

	print("cosine similarities before equalizing:")
	print("cosine_similarity(word_to_vec_map[\"man\"], gender) = ", cosine_similarity(word_to_vec_map["man"], g))
	print("cosine_similarity(word_to_vec_map[\"woman\"], gender) = ", cosine_similarity(word_to_vec_map["woman"], g))
	print()
	e1, e2 = equalize(("man", "woman"), g, word_to_vec_map)
	print("cosine similarities after equalizing:")
	print("cosine_similarity(e1, gender) = ", cosine_similarity(e1, g))
	print("cosine_similarity(e2, gender) = ", cosine_similarity(e2, g))	