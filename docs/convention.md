# Source code structure

| Folder/Files              | Description                                                                                                                                                                                                                  |
| --------------------------| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| app(fd)                   | Common code which can be used by different app. eg: ```auth.py```                                                                                                                                |
| migration                 | Contains flask migration files                                                                                                                                |
| ```auth.py```             | Authorization decorators                                                                                           |
| ```doas.py```             | Database access object                                                                                           |
| ```services.py```         | Business logic                                                                                                                                                                                    |
| ```models.py```           | Database models |
| ```task_serialiser.py``   | Marshmallow schema serialisers
| tests                     | Contains app test cases                                                                                                                                                    |
|```urls.py```              | Contains app urls                                                                                                                                                                                                   |
