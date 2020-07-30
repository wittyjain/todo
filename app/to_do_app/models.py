from app import db


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.String(120), primary_key=True)
    created_at = db.Column(
        db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())


class TaskItem(Base):
    __tablename__ = 'todo_task_list'
    name = db.Column(db.String(200))
    description = db.Column(db.String(500), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
