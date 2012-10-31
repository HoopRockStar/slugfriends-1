# coding: utf8

#db.define_table('Users',
#    Field('id', db.auth_user),
#    Field('name', 'string'),
#    Field('username', 'string'),
#    Field('photo', 'upload'),
#    Field('email', 'string'),
#    Field('password', 'password'),
#    Field('description', 'text'),
#    )
    
db.define_table('Groups',
    Field('photo', 'upload'),
    Field('name', 'string'),
    Field('description', 'text'),
    )

db.define_table('Events',
    Field('title', 'string'),
    Field('date', 'date'),
    Field('time', 'time'),
    Field('location', 'string'),
    Field('group_id', db.Groups),
    Field('description', 'text'),
    )

db.define_table('Group_Members',
    Field('group_id', db.Groups),
    Field('member', db.auth_user, default=auth.user_id),
    Field('administrator', 'boolean'),
    Field('rating', 'integer'),
    )
   
           
db.define_table('Attendees',
    Field('event', db.Events),
    Field('attendee', db.Group_Members),
    Field('administrator', 'boolean'),
    )
   
db.define_table('Comments',
    Field('event', db.Events),
    Field('member', db.Group_Members),
    Field('comment', 'text'),
    )
   
db.define_table('Keywords',
    Field('keyword', 'string'),
    )

db.define_table('User_Interests',
    Field('user', db.auth_user, default=auth.user_id),
    Field('interest', db.Keywords),
    )        
   
db.define_table('Search',
    Field('keyword_id', db.Keywords),
    Field('group_id', db.Groups),
    )

#db.Users.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'Users.email')]
