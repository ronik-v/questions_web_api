from requests import get
from requests.exceptions import HTTPError, InvalidURL
from asyncio import sleep

async def get_questions(number: int) -> list[dict[str, str]] | None:
	url = f'https://jservice.io/api/random?count={number}'
	try:
		await sleep(0.5)
		all_questions = list()
		data = get(url).json()
		for question in data:
			tmp_question = dict()
			tmp_question['question_id'] = question['id']
			tmp_question['question_text'] = question['question']
			tmp_question['answer_text'] = question['answer']
			tmp_question['create_date'] = question['created_at']
			all_questions.append(tmp_question)
		return all_questions
	except InvalidURL:
		return
	except HTTPError:
		return
