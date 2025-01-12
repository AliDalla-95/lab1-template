from marshmallow import Schema, fields, validate

class PersonRequestSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int()
    address = fields.Str()
    work = fields.Str()

class PersonResponseSchema(PersonRequestSchema):
    id = fields.Int(required=True)