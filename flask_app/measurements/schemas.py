from marshmallow import Schema, validates_schema, fields, ValidationError


class MeasurementGet(Schema):
    id = fields.Int(required=True, allow_none=False)
    temperature = fields.Int(required=True, allow_none=False)
    air_quality = fields.Int(required=True, allow_none=False)
    humidity = fields.Int(required=True, allow_none=False)
    created_datetime = fields.DateTime(required=True, allow_none=False)

    @validates_schema
    def validate_get(self, data, **kwargs):
        print("test")
        if data["humidity"] < 0 or data["humidity"] > 100:
            raise ValidationError("humidity")
        if data["temperature"] < 0:
            raise ValidationError("temperature")
        if data["air_quality"] < 0 or data["air_quality"] > 100:
            raise ValidationError("air_quality")
        if data["id"] < 100:
            raise ValidationError("id")


# --------------------- POST -------------------------
class MeasurementPost(Schema):
    temperature = fields.Int(required=True, allow_none=False)
    air_quality = fields.Int(required=True, allow_none=False)
    humidity = fields.Int(required=True, allow_none=False)

    @validates_schema
    def validate_post(self, data, **kwargs):
        if data["temperature"] < 0:
            raise ValidationError("temperature")
        if data["humidity"] < 0 or data["humidity"] > 100:
            raise ValidationError("humidity")
        if data["air_quality"] < 0 or data["air_quality"] > 100:
            raise ValidationError("air_quality")
