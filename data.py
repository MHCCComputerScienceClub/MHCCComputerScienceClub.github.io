# Refactor this into a class
def Articles():
	articles = [
		{
			'id' : 1, 
			'title' : 'Article One',
			'Body' : 'Stuff',
			'author' : 'Person',
			'create_date' : '05-02-2018'
		}
	]

	return articles

def Projects():
	projects = [
		{
			'id' : 1,
			'title' : 'Project Name',
			'Body' : 'Project description',
			'contributors' : 'TODO Make this a list of people',
			'create_data' : '05-02-2018'
		},
		{
			'id' : 2,
			'title' : 'Project Name 2',
			'Body' : 'Project description 2',
			'contributors' : 'TODO Make this a list of people',
			'create_data' : '05-02-2018'
		},
		{
			'id' : 3,
			'title' : 'Project Name 3',
			'Body' : 'Project description 3',
			'contributors' : 'TODO Make this a list of people',
			'create_data' : '05-02-2018'
		},

	]
	return projects