from app import app
from app.to_do_app.views import TaskItem

task_item = TaskItem.as_view('tasks')

app.add_url_rule('/tasks', defaults={'task_id': None},
                 view_func=task_item, methods=['GET']
                 )
app.add_url_rule('/tasks',
                 view_func=task_item, methods=['POST']
                 )
app.add_url_rule('/tasks/<string:task_id>', view_func=task_item,
                 methods=['GET', 'PUT', 'DELETE']
                 )
