from app import app
from app.to_do_app.views import TaskList

task_list = TaskList.as_view('tasks')

app.add_url_rule('/tasks', defaults={'task_id': None},
                 view_func=task_list, methods=['GET', 'POST']
                 )
app.add_url_rule('/tasks/<string:task_id>', view_func=task_list,
                 methods=['GET', 'PUT', 'DELETE']
                 )
