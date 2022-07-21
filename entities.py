from tecton import Entity


user = Entity(
    name='user',
    join_keys=['USER_ID'],
    description='A user of the platform',
    owner='matt@tecton.ai',
    tags={'release': 'production'}
)
