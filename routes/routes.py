from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Any
from data.database import engine
from models.model import Question
from api.jservice_api import get_questions
api = APIRouter()


class QuestionPost(BaseModel):
	questions_num: int


async def filter_questions(questions_num) -> dict[str, str]:
	added_count = questions_num
	questions_service = None
	while added_count != 0:
		questions_service = await get_questions(questions_num)
		if questions_service:
			questions_objects = list()
			for question in questions_service:
				db_tuple = Question(
					question_id=question['question_id'],
					question_text=question['question_text'],
					answer_text=question['answer_text'],
					create_date=question['create_date']
				)
				questions_objects.append(db_tuple)

			with Session(autoflush=False, bind=engine) as db:
				for question_obj in questions_objects:
					if db.query(Question.question_text).filter_by(question_text=question_obj.question_text).first():
						pass
					else:
						db.add(question_obj)
						db.commit()
						added_count -= 1
		else:
			break
	return questions_service[len(questions_service) - 1]


@api.post('/questions_api')
async def questions(questions_num: QuestionPost = 1) -> dict[str, Any]:
	try:
		last = await filter_questions(questions_num.questions_num)
		return {'status': 400, 'result': last}
	except:
		return {'status': 200, 'result': ''}