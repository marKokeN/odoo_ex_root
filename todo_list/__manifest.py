{
    'name': 'Todo List',
    'version': '1.0',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/todo_list_views.xml',
    'views/todo_tag_views.xml',
    'data/todo_tag_data.xml',
    'views/todo_list_views.xml',
    'views/todo_menu.xml'
    ],
    'installable': True,
    'auto_install': False,
}
