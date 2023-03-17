# Notes

`python manage.py shell`
`from accounts.models import CustomUser`
`from deciderator.models import Task`
`from deciderator.models import Task, SubTask, ImportantConcept`

`owner = CustomUser.objects.get(id=1)`

`t = Task.objects.create(owner=owner, description="This is a totally new task")`
`t.save()`

`t.get_next_special_order()`

`t.sort_and_assign_special_order()`