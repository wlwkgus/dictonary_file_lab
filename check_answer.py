import pickle

def check_answer(city_name, person_name, answer):
	with open('answer_dict_of_{0}.pickle'.format(city_name), 'rb') as f:
		answer_dict = pickle.load(f)
		return answer_dict[person_name] == answer

if __name__ == '__main__':
	f = open('answer', 'r')
	lines = f.readlines()
	answer_list = lines[0].split(',')
	if check_answer('seoul', 'Jessica', int(answer_list[0]) ) and check_answer('busan', 'Jessica', int(answer_list[1])):
		print("Good Job!")
	else:
		print("Wrong answer!")
