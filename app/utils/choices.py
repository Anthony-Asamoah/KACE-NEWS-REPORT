ROLE_CHOICES = [
    ('EDITOR', 'Editor'),
    ('REPORTER', 'Reporter'),
    ('DESK_HEAD', 'Desk Head'),
    ('REGIONAL_EDITOR', 'Regional Editor'),
    ('NATIONAL_EDITOR', 'National Editor'),
]
STAFF_TYPE_TO_GROUP = {
    'EDITOR': 'Editors',
    'REPORTER': 'Reporters',
    'DESK_HEAD': 'Desk Heads',
    'REGIONAL_EDITOR': 'Regional Editors',
    'NATIONAL_EDITOR': 'National Editors',
}

STATUS_CHOICES = [
    ('DRAFT', 'Draft'),
    ('PUBLISHED', 'Published'),
    ('REJECTED', 'Rejected'),
]