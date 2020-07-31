from marshmallow import Schema, fields


class TaskItemSchema(Schema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    is_completed = fields.Bool()
    created_at = fields.DateTime()
