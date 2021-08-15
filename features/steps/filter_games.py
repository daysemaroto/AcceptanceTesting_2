from behave import *
from src.Game import *
from src.Catalogue import *

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("a set of games")
def step_impl(context):
	game_list = []

	for row in context.table:

		elenco = []
		idiomas = []
		game = Game(row['NAME'], row['RELEASE DATE'], row['DEVELOPER'], row['RATE'])
		game_list.append(game)

	context.games = game_list

@given('the user enters the name: {name}')
def step_impl(context, name):
	context.name = name

#rating
@given('the user enters the ratings: {ratings}')
def step_impl(context, ratings):
	context.ratings = ratings

#Developer
@given('the user enters the developer: {study}')
def step_impl(context, study):
		context.study = study

@when("the user search games by {criteria}")
def step_impl(context, criteria):
	if(criteria == 'name'):
		result, message = get_game_name(context.games, context.name)
		print(result)
		context.result = result
		context.message = message
	elif (criteria == 'study'):
		result, message = get_game_developer(context.games, context.study)
		context.result = result
		context.message = message
	elif (criteria == 'ratings'):
		result, message, error = get_game_rating(context.games, context.ratings)
		context.result = result
		context.message = message
		context.error = error

@then("{total} games will match")
def step_impl(context, total):
	assert len(context.result) == int(total)

@then("the names of these games are")
def step_impl(context):
	expected_games = True
	result_games = []
	for row in context.table:
		result_games.append(row['NAME'])
	for game in context.result:
		if game.name not in result_games:
			print("No game " + game.name)
			expected_games = False
	assert expected_games is True

@then("the following message is displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message