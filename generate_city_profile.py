import names
import pickle
from collections import defaultdict

def generate_random_name_list_file(city_name):
	f = open('name_list_of_{0}.csv'.format(city_name), 'w')
	answer_dict = defaultdict(int)
	for _ in range(10000):
		name = names.get_first_name()
		answer_dict[name] += 1
		f.write(name + '\n')
	with open('answer_dict_of_{0}.pickle'.format(city_name), 'wb') as f:
		pickle.dump(answer_dict, f)
	f.close()


if __name__ == '__main__':
	generate_random_name_list_file('seoul')
	generate_random_name_list_file('busan')
