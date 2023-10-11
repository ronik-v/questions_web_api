from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Date, Text, String
Base = declarative_base()


class Question(Base):
	__tablename__: str = 'questions'
	__tableargs__: dict[str, str] = {
		'comment': 'Questions for quiz'
	}

	id = Column(
		Integer,
		nullable=False,
		unique=True,
		primary_key=True,
		autoincrement=True
	)

	question_id = Column(
		Integer,
		nullable=False
	)
	question_text = Column(
		Text,
		nullable=False,
		comment='Question text'
	)
	answer_text = Column(
		String,
		nullable=False,
		comment='Answer text'
	)
	create_date = Column(
		Date,
		nullable=False,
		comment='Date the question was created'
	)

	def __repr__(self) -> str:
		return f'{self.question_id} {self.create_date}'
